# NCBI genome download helper

**Python script for downloading genomes from NCBI ftp**


## Usage

```bash
$ ncbi-genome-download --help
usage: ncbiGenomeDownload [-h] [-t TAXID] [-a ACCESSION] [-m {representative,n,all}] [-n N] [-r REFSEQ] [-o OUTPATH] [--version]

Download genomes from NCBI REFSEQ

options:
  -h, --help            show this help message and exit
  -t TAXID              path to species taxid list file. One species taxid per line (default: None)
  -a ACCESSION          path to genome accession list file. One genome accession per line (default: None)
  -m {representative,n,all}
                        Method to retrieve reference genones. Only representative, N randonly subsampled genones, or all (default: representative)
  -n N                  Number of genomes to download if --mode n (default: None)
  -r REFSEQ             path to assembly_summary_refseq.txt (default: assembly_summary_refseq.txt)
  -o OUTPATH            path to existing output directory (default: .)
  --version             show program's version number and exit
gitpod /workspace/ncbi-genome-download (master) $ 
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

### taxid list file

This file must contain one species TAXID per line

 *Example :*

```bash
$ cat test/data/taxid.txt
28985
562
```

### genome accession list file

This file must contain one species accession per line

 *Example :*

```bash
$ cat test/data/accs.txt 
GCF_000001985.1
GCF_000002035.6
```
