import argparse
from ncbigenomedownload  import main, __version__

def _get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        prog='ncbiGenomeDownload',
        description='Download genomes from NCBI REFSEQ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'species_taxid_list', help="path to species taxid list file. One species taxid per line")
    parser.add_argument(
        '-m',
        dest='mode',
        choices=['representative', 'n', 'all'],
        default="representative",
        help="Method to retrieve reference genones. Only representative, N randonly subsampled genones, or all"
    )
    parser.add_argument(
        '-n',
        dest='n',
        type=int,
        default=None,
        help='Number of genomes to download if --mode n'
    )
    parser.add_argument(
        '-r',
        dest="refseq",
        default="assembly_summary_refseq.txt",
        help="path to assembly_summary_refseq.txt")
    parser.add_argument(
        '-o',
        dest="outpath",
        default=".",
        help="path to existing output directory")
    parser.add_argument('--version', action='version',
                    version=f"sam2lca v{__version__}")

    args = parser.parse_args()

    taxids = args.species_taxid_list
    refseq = args.refseq
    mode = args.mode
    nb = args.n
    outpath = args.outpath

    return(taxids, refseq, mode, nb, outpath) 


def cli():
    TAXIDS, REFSEQ, MODE, NB, OUTPATH = _get_args()
    main(REFSEQ, TAXIDS, MODE, NB, OUTPATH)
