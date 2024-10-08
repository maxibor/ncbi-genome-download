import os
import csv
from pathlib import Path
from ncbigenomedownload.fieldnames import refseq_fieldnames, genbank_fieldnames
from pprint import pprint
from tqdm.contrib.concurrent import thread_map
from functools import partial
import logging
from urllib import request
import shutil
import time
import random


__version__ = "0.3"

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

def parse_summary(ass_sum, fieldnames):
    '''This function parses the assembly_summary_refseq.txt 
    '''
    rs_dict = dict()
    rs_acc_dict = dict()
    with open(ass_sum, 'r') as csv_file:
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

            if row['assembly_accession'] not in rs_acc_dict:
                rs_acc_dict[row['assembly_accession']] = row
    return rs_dict, rs_acc_dict

def get_genome_url(taxid, rs_dict, mode, nb):
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
        return [tuple([
            entries[0]['organism_name'].lower().replace(" ","_"), 
            taxid,
            ftp_path
        ])]
    else:
        rep_ret = []
        ret = []
        for entry in entries:
            if entry['refseq_category'] == "representative genome":
                ftp_root_path = entry['ftp_path']
                ftp_path = os.path.join(ftp_root_path, f"{Path(ftp_root_path).name}_genomic.fna.gz")
                rep_ret = [tuple([
                    entry['organism_name'].lower().replace(" ","_"), 
                    taxid,
                    ftp_path
                ])]
            elif mode in ['n', 'all']:
                ftp_root_path = entry['ftp_path']
                ftp_path = os.path.join(ftp_root_path, f"{Path(ftp_root_path).name}_genomic.fna.gz")
                ret.append(tuple([
                    entry['organism_name'].lower().replace(" ","_"), 
                    taxid,
                    ftp_path
                    ])
                )
        if mode == 'n' and nb and nb <= len(ftp_path):
            ret = random.sample(ret, nb)
        return rep_ret + ret

def get_url_from_acc(acc, accession_dict):
    """
    Get entry from genome accessions:
    
    Args:
        acc(str): genome_accessions
        accession_dict(dict): refseq summary dict with accession as key
    Returns:
        tuple([str, str, str]): specname, taxid, url
    """
    
    try:
        specname = accession_dict[acc]['organism_name'].lower().replace(" ","_")
        taxid = accession_dict[acc]['species_taxid']
        url = accession_dict[acc]['ftp_path']
        url = os.path.join(url, f"{Path(url).name}_genomic.fna.gz")

        return(tuple([specname, taxid, url]))
    except KeyError:
        print(f"Error with accession {acc}")
        pass



def get_genome_urls(rs_dict, taxids, mode, nb):
    '''This function returns a list of urls to download
    '''
    get_genome_url_partial = partial(get_genome_url, rs_dict = rs_dict, mode = mode, nb = nb)
    urls = thread_map(get_genome_url_partial, taxids)
    urls = [entry for taxid in urls for entry in taxid]
    pprint(urls)
    return urls

def read_acc_list(acc_list_file):
    acc_list = []
    with open(acc_list_file, 'r') as f:
        for line in f:
            acc_list.append(line.rstrip())

    return acc_list


def main(taxid_list_file, acc_list_file, mode, nb, outdir, rs_summary_file=None, gb_summary_file=None):
    print(rs_summary_file, gb_summary_file)
    if rs_summary_file:
        summary_file = rs_summary_file
        fieldnames = refseq_fieldnames
    elif gb_summary_file:
        summary_file = gb_summary_file
        fieldnames = genbank_fieldnames
    else:
        raise ValueError("You must provide either a refseq or genbank summary file")
    rss, rss_acc = parse_summary(summary_file, fieldnames)
    if acc_list_file:
        acc_list = read_acc_list(acc_list_file)
        entries = [get_url_from_acc(acc = acc, accession_dict=rss_acc) for acc in acc_list]
    else:
        taxids = parse_species_taxid_list(taxid_list_file)
        entries = get_genome_urls(rss, taxids, mode, nb)
    download_files(entries, outdir)
