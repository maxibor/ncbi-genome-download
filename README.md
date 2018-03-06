# NCBI genome download helper

**Python script for downloading genomes from NCBI ftp**


# Usage
```
./ncbiGenomeDownload -r assembly_summary_refseq.txt  genomes.txt
```

# Help
```
maxime@gph:~NCBI_genome_download$ ./ncbiGenomeDownload --help
usage: ncbiGenomeDownload [-h] [-r REFSEQ] specie_list

Download genomes from NCBI REFSEQ

positional arguments:
  specie_list  path to specie list file. One specie per line

optional arguments:
  -h, --help   show this help message and exit
  -r REFSEQ    path to assembly_summary_refseq.txt

```

# Notes

## RefSeq file

To update the RefSeq file, please download the assembly summary file from NCBI and put it in the same directory as the program :

`wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt`

## genomes list file

 This file must contain one bacterial specie name per line

 *Example :*

```
maxime@gph:~NCBI_genome_download$ cat genomes.txt
Escherichia coli
Mycobacterium tuberculosis
```
