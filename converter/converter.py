""" Convert pdf files in the corpus folder to text files"""

import os
import re
import time
import pdftotext

# import PyPDF2
from pprint import pprint

# from downloader.constants import YEARS


def convert_pdf_to_text():
    """Convert PDF files in the corpus folder to text files."""
    for file in os.listdir("./corpus/pdf"):
        if file.endswith(".pdf"):
            with open(f"./corpus/pdf/{file}", "rb") as pdf_file:
                pdf = pdftotext.PDF(pdf_file)
                # number_of_pages = len(pdf)
                year = file[:4]
                # if year.isdigit() and int(year) in YEARS:
                with open(f"./corpus/text/{file[:-4]}.txt", "w") as text_file:
                    for page in pdf:
                        text_file.write(page)
                        # for page_number in range(number_of_pages):
                        #     page = read_pdf.getPage(page_number)
                        #     page_content = page.extractText()
                        # text_file.write(page_content)
                # else:
                #     print(f"Invalid year: {year}")

                print(f"{file} converted to text file successfully.")


if __name__ == "__main__":
    start_time = time.time()
    convert_pdf_to_text()
    print(f"--- {time.time() - start_time} seconds ---")
