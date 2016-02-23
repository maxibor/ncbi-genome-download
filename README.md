# NCBI bacterial genome download helper
**Python script for downloading bacterial genomes from NCBI ftp**

 - Before the first launch, please download the assembly summary file from NCBI and put it in the same directory as the program :
 `wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt`

 - **Usage** : python bacterial_genome_download.py genomes.txt

 - genomes.txt must contain one bacterial specie name per line
 
 *Example :*
 
	```
Escherichia coli
Mycobacterium tuberculosis
```
