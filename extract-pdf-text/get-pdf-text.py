# This approach to using 'pypdf' to extract text from PDF files 
# often works well for me. It is from the pypdf docs. 
# https://pypdf.readthedocs.io/en/stable/user/extract-text.html
# pypdf errors are documented in:  
# https://github.com/py-pdf/pypdf/blob/main/pypdf/errors.py
# 
# ToDo: Add some text cleanup via post-processing.
# The link below lists a few examples of what can be done as well 
# as a community recipie that can be used as a best-practice 
# general purpose post processing step.
# https://pypdf.readthedocs.io/en/stable/user/post-processing-in-text-extraction.html
from pypdf import PdfReader
import sys

text = ""
separator = "= = = = = = = = = = = = = = = = = = = = = = = ="


def openpdf(filename):
    try:
        pdfreader = PdfReader(filename)     #"rammed-earth-walls-for-buildings-1926.pdf")
    except Exception as e:
        print(f"Problem with PdfReader. Did you specify a valid filename? {e}")
        sys.exit()
    return pdfreader


def get_text_from_pdfreader(reader):
    try:
        for page in reader.pages:
            text = page.extract_text()
            print(f"{text}")
            print(f"\r\n")
    except Exception as e:
        print(f"Problem extracting text. Error: {e}")
        sys.exit()


def print_separator(msgstring):
    print(f"{separator}")
    print(f"{msgstring}")
    print(f"{separator}")


def main():
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {sys.argv[0]} <input_pdf_filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if filename != None:
        reader = openpdf(filename)
        print_separator(f"Start {filename} text")
        get_text_from_pdfreader(reader)
        print_separator(f"End {filename} text")
        sys.exit()


if __name__ == '__main__':
    main()
