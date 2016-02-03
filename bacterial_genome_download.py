import csv
import sys
import os
try :
    with open(sys.argv[1],"r") as name_list :
        with open("assembly_summary_refseq.txt", "r") as genome_list_file :
            genomes_list = csv.reader(genome_list_file, delimiter = "\t")

            for name in name_list :
                name = name.rstrip()
                for genome in genomes_list :
                    if name == genome[7] :
                        strain_name = genome[0]+"_"+genome[15]
                        file_name = strain_name+"_genomic.fna.gz"
                        link = genome[-1]
                        break
                cmd = "wget "+link+"/*.fna.gz &> /dev/null"
                print "Downloading the genome of "+name+" strain "+strain_name+" ..."
                os.system(cmd)
                cmd = "mv "+file_name+" ./"+name.split(" ")[0]+"_"+name.split(" ")[1]+"_"+file_name
                os.system(cmd)
                print "Finished Downloading "+name.split(" ")[0]+"_"+name.split(" ")[1]+"_"+file_name
except IndexError :
    print '''
    ==NCBI BACTERIAL GENOME DOWNLOAD==

    -> Usage : python bacterial_genome_download.py genomes.txt

    -> genomes.txt must contain one bacterial specie name per line

    Before the first launch of this program, please download the assembly summary file from NCBI and put it in the same directory as the program : \n\twget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt

    '''
except IOError :
    print '''
    ==NCBI BACTERIAL GENOME DOWNLOAD==

    -> Usage : python bacterial_genome_download.py genomes.txt

    -> genomes.txt must contain one bacterial specie name per line

    Before the first launch of this program, please download the assembly summary file from NCBI and put it in the same directory as the program : \n\twget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt
    '''
