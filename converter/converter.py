""" Convert pdf files in the corpus folder to text files"""

import os
import re
import time
import pdftotext
from pprint import pprint


def convert_pdf_to_text():
    """Convert PDF files in the corpus folder to text files."""
    for file in os.listdir("./corpus/pdf"):
        if file.endswith(".pdf"):
            with open(f"./corpus/pdf/{file}", "rb") as pdf_file:
                pdf = pdftotext.PDF(pdf_file)
                with open(f"./corpus/text/{file[:-4]}.txt", "w") as text_file:
                    for page in pdf:
                        text_file.write(page)
                print(f"{file} converted to text file successfully.")


if __name__ == "__main__":
    start_time = time.time()
    # convert_pdf_to_text()

    print(f"--- {time.time() - start_time} seconds ---")
