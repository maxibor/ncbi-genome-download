import argparse
from ncbigenomedownload  import main, __version__

def _get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        prog=f'ncbiGenomeDownload v{__version__}',
        description='Download genomes from NCBI Assembly databases (RefSeq/Genbank)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-t',
        dest='taxid', 
        default=None,
        help="path to species taxid list file. One species taxid per line"
        )
    parser.add_argument(
        '-a',
        dest='accession', 
        default=None,
        help="path to genome accession list file. One genome accession per line"
        )
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
        help="path to assembly_summary_refseq.txt")
    parser.add_argument(
        '-g',
        dest="genbank",
        help="path to assembly_summary_genbank.txt")
    parser.add_argument(
        '-o',
        dest="outpath",
        default=".",
        help="path to existing output directory")
    parser.add_argument('--version', action='version',
                    version=f"ncbigenomedownload v{__version__}")

    args = parser.parse_args()

    taxids = args.taxid
    accs = args.accession
    refseq = args.refseq
    genbank = args.genbank
    mode = args.mode
    nb = args.n
    outpath = args.outpath

    return(taxids, accs, refseq, genbank, mode, nb, outpath) 


def cli():
    TAXIDS, ACCS, REFSEQ, GENBANK, MODE, NB, OUTPATH = _get_args()
    main(TAXIDS, ACCS, MODE, NB, OUTPATH, rs_summary_file=REFSEQ, gb_summary_file=GENBANK)
