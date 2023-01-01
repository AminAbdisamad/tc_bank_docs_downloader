""" Convert pdf files in the corpus folder to text files"""

import os
import re
import time
import pdftotext
from PyPDF2 import PdfReader


def convert_pdf_to_text():
    """Convert PDF files in the corpus folder to text files."""
    for file in os.listdir("./corpus/pdf"):
        if file.endswith(".pdf"):
            with open(f"./corpus/pdf/{file}", "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                with open(f"./corpus/text/{file[:-4]}.txt", "w") as text_file:
                    for page in reader.pages:
                        text = page.extract_text()
                        text_file.write(text)
                        # text_file.write(page)
                print(f"{file} converted to text file successfully.")


if __name__ == "__main__":
    start_time = time.time()
    # convert_pdf_to_text()

    print(f"--- {time.time() - start_time} seconds ---")


# Display all text files that has 0 bytes
for file in os.listdir("./corpus/text"):
    if file.endswith(".txt"):
        if os.stat(f"./corpus/text/{file}").st_size == 0:
            print(file)
