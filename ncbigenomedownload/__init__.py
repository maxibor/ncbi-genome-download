import os
import csv
from pathlib import Path
from ncbigenomedownload.fieldnames import fieldnames
from pprint import pprint
from tqdm.contrib.concurrent import thread_map
from functools import partial
import logging
from urllib import request
import shutil
import time
import random


__version__ = "0.1"

def download_file(entry, outdir):
    os.makedirs(outdir, exist_ok=True)
    specname, taxid, url = entry
    acc = "_".join(Path(url).name.split("_")[0:2])
    fname = f"{taxid}_{specname}_{acc}.fna.gz"
    
    output_file = os.path.join(outdir, fname)
    print(output_file, url)
    with request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    time.sleep(random.randint(1,2))

def download_files(entries, outdir):
    download_file_partial = partial(download_file, outdir = outdir)
    thread_map(download_file_partial, entries, max_workers=5)

def parse_species_taxid_list(taxid_list_file):
    taxids = []
    with open(taxid_list_file, 'r') as f:
        for line in f:
            taxids.append(line.strip())
    return taxids

def parse_refseq_summary(rs_ass_sum):
    '''This function parses the assembly_summary_refseq.txt 
    '''
    rs_dict = dict()
    with open(rs_ass_sum, 'r') as csv_file:
        reader = csv.DictReader(
            filter(lambda row: row[0]!='#', csv_file), 
            fieldnames=fieldnames, 
            delimiter='\t'
            )
        for row in reader:
            if row['species_taxid'] not in rs_dict:
                rs_dict[row['species_taxid']] = [row]
            else :
                rs_dict[row['species_taxid']].append(row)
    return rs_dict

def get_genome_url(taxid, rs_dict):
    '''This function returns a list of urls to download
    '''
    try:
        entries = rs_dict[taxid]
    except KeyError as e:
        logging.error(f"No entry found for taxid {taxid}")
        raise(e)
    if len(entries) == 1:
        ftp_root_path = entries[0]['ftp_path']
        ftp_path = os.path.join(ftp_root_path, f"{Path(ftp_root_path).name}_genomic.fna.gz")
        return tuple([
            entries[0]['organism_name'].lower().replace(" ","_"), 
            taxid,
            ftp_path
        ])
    else:
        for entry in entries:
            if entry['refseq_category'] == "representative genome":
                ftp_root_path = entry['ftp_path']
                ftp_path = os.path.join(ftp_root_path, f"{Path(ftp_root_path).name}_genomic.fna.gz")
                return tuple([
                    entry['organism_name'].lower().replace(" ","_"), 
                    taxid,
                    ftp_path
                ])


def get_genome_urls(rs_dict, taxids):
    '''This function returns a list of urls to download
    '''
    get_genome_url_partial = partial(get_genome_url, rs_dict = rs_dict)
    urls = thread_map(get_genome_url_partial, taxids)
    return urls

def main(refseq_summary_file, taxid_list_file , outdir):
    rss = parse_refseq_summary(refseq_summary_file)
    taxids = parse_species_taxid_list(taxid_list_file)
    entries = get_genome_urls(rss, taxids)
    download_files(entries, outdir)
