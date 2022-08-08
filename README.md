# NCBI genome download helper

**Python script for downloading genomes from NCBI ftp**


## Usage

```bash
$ ncbi-genome-download --help
usage: ncbiGenomeDownload [-h] [-r REFSEQ] [-o OUTPATH] [--version] species_taxid_list

Download genomes from NCBI REFSEQ

positional arguments:
  species_taxid_list  path to species taxid list file. One species taxid per line

optional arguments:
  -h, --help          show this help message and exit
  -r REFSEQ           path to assembly_summary_refseq.txt
  -o OUTPATH          path to existing output directory
  --version           show program's version number and exit
```

## Installation 

With pip, from Github

```bash
pip install git+https://git@github.com/maxibor/ncbi-genome-download.git@master
```


## Notes

### RefSeq file

To update the RefSeq file, please download the assembly summary file from NCBI :

```bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt
```

### genomes list file

This file must contain one species TAXID per line

 *Example :*

```bash
$ cat test/data/taxid.txt
28985
562
```
