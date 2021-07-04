"""Combine pdf files from selected directory into a single pdf. Saves result as specified.

Usage:
  merge.py <dir> <output>
  merge.py (-h | --help)

Arguments:
  <dir>  Input dir

Options:
  -h, --help     Show this screen.

"""
from typing import List
import glob

from PyPDF2 import PdfFileMerger
from docopt import docopt


def combine(pdfs: List[str], output_loc: str):
    """

    Parameters
    ----------
    pdfs : list[str]
        List of strings contianing pdfs to merge.
    output_loc : str
        Location for output file (including filename and extension)
    Returns
    -------

    """
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(str(pdf))

    merger.write(output_loc)
    merger.close()


if __name__ == "__main__":
    arguments = docopt(__doc__)
    pdfs = glob.glob(f"{arguments['<dir>']}/*.pdf")
    combine(pdfs, arguments["<output>"])