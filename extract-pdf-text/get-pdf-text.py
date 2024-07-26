# This approach to using 'pypdf' to extract text from PDF files 
# often works well-enough for me. It is from the pypdf docs. 
# https://pypdf.readthedocs.io/en/stable/user/extract-text.html
# pypdf can extract a range of PDF components: 
# https://pypdf2.readthedocs.io/en/3.0.0/_modules/PyPDF2/_reader.html
# pypdf errors are documented in:  
# https://github.com/py-pdf/pypdf/blob/main/pypdf/errors.py
# 
# As needed: Add some text cleanup via post-processing.
# The link below lists a few examples of what can be done as well 
# as a community recipie that can be used as a best-practice 
# general purpose post processing step.
# https://pypdf.readthedocs.io/en/stable/user/post-processing-in-text-extraction.html
# 
# or adopt a more full featured toolkit for PDF Content Extraction:  
# https://github.com/opendatalab/PDF-Extract-Kit
import pypdf
import os
import sys
import time


def open_pdf(filename: str) -> bytes:
    try:
        if not os.path.exists(filename):
            raise Exception(f"File path \"{filename}\" does not \
appear to exist, or there may be a permission issue.")
        pdfreader = pypdf.PdfReader(filename)
    except Exception as e:
        print(f"Problem with PdfReader and \"{filename}\". \
Did you specify a valid PDF file? {e}")
        sys.exit()
    return pdfreader


def get_text_from_pdfreader(reader: bytes) -> str:
    try:
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            # Add some whitespace between pages
            text += (f"\r\n\r\n")
    except Exception as e:
        print(f"Problem extracting text inside \"get_text_from_pdfreader\(\)\". Error: {e}")
        sys.exit()
    return text


# This function is from the pypdf documentation:  
# https://pypdf.readthedocs.io/en/stable/user/post-processing-in-text-extraction.html#ligature-replacement
def replace_ligatures(text: str) -> str:
    ligatures = {
        "ﬀ": "ff",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
        "ﬅ": "ft",
        "ﬆ": "st",
        "ß": "ss",
        # "⻖": "(Unicode U+2ED6)",
        # "阝": "(Unicode U+961D)",
        # "ഭ": "(Malayalam script Consonant bha Unicode U+0D2D)",        
        # "Ä": "A", 
        # "Ö": "O",
        # "Ü": "U",
        # "Ꜳ": "AA",
        # "Æ": "AE",
        # "ꜳ": "aa",
        # "»": ">>",
        # "«": "<<",
        # "✓": "(check)",
    }
    for search, replace in ligatures.items():
        text = text.replace(search, replace)
    return text


def current_local_time() -> str:
    # Specifying time this way involves risks.
    # The local time may be inaccurate, which may be intentional
    # to mislead those who receive the output.
    # It is, though, an appropriate risk in my use case.
    # format codes from: https://strftime.org/
    now = time.strftime("%c %Z")
    return now


def print_separator(msgstring: str):
    separator = "= = = = = = = = = = = = = = = = = = = = = = = ="
    print(f"# {separator}")
    print(f"# {msgstring}")
    print(f"# {separator}")


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    filename = sys.argv[1]
    if filename != None:
        reader = open_pdf(filename)
        print_separator(f"Start \"{filename}\" text.\r\n# Extracted on: {current_local_time()}")
        extracted_text = get_text_from_pdfreader(reader)
        # Add post-processing function(s) here 
        print(f"{replace_ligatures(extracted_text)}")
        print_separator(f"End \"{filename}\" text.\r\n# Extracted on: {current_local_time()}")
        sys.exit()


if __name__ == '__main__':
    main(2, 'USAGE: python3 script_name <input_pdf_filename>')
