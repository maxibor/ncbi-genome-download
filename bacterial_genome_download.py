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
                        print genome
                        link = genome[-1]
                        break
                cmd = "wget "+link+"/*.fna.gz &> /dev/null"
                print "Downloading the genome of "+name+" strain "+strain_name+" ..."
                os.system(cmd)
                print "Finished Downloading "+file_name
except IndexError :
    print '''
    ==NCBI BACTERIAL GENOME DOWNLOAD==

    -> Usage : python bacterial_genome_download.py genomes.txt

    -> genomes.txt must contain one bacterial specie name per line
    '''
except IOError :
    print '''
    ==NCBI BACTERIAL GENOME DOWNLOAD==

    -> Usage : python bacterial_genome_download.py genomes.txt

    -> genomes.txt must contain one bacterial specie name per line
    '''
