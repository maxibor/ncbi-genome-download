# NCBI genome download helper

**Python script for downloading genomes/assemblies from NCBI ftp**


## Usage

```bash
$ ncbi-genome-download --help
usage: ncbiGenomeDownload v0.3 [-h] [-t TAXID] [-a ACCESSION] [-m {representative,n,all}] [-n N] [-r REFSEQ] [-g GENBANK] [-o OUTPATH] [--version]

Download genomes from NCBI Assembly databases (RefSeq/Genbank)

options:
  -h, --help            show this help message and exit
  -t TAXID              path to species taxid list file. One species taxid per line (default: None)
  -a ACCESSION          path to genome accession list file. One genome accession per line (default: None)
  -m {representative,n,all}
                        Method to retrieve reference genones. Only representative, N randonly subsampled genones, or all (default: representative)
  -n N                  Number of genomes to download if --mode n (default: None)
  -r REFSEQ             path to assembly_summary_refseq.txt (default: None)
  -g GENBANK            path to assembly_summary_genbank.txt (default: None)
  -o OUTPATH            path to existing output directory (default: .)
  --version             show program's version number and exit
```

## Installation 

With pip, from Github

```bash
pip install git+https://git@github.com/maxibor/ncbi-genome-download.git@master
```


## Notes

### Summary file

To update the RefSeq summary file:

```bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt
```

To update the Genbank summary file:

```bash
wget https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt
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
$ cat test/data/rs_accs.txt 
GCF_000001985.1
GCF_000002035.6
```
