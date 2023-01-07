import os
import time
from converter import Converter


def prepareTextFile(pdf_file_destination, text_file_destination):
    """This function prepares data"""
    # Initialize converter object

    if pdf_file_destination.endswith(".pdf"):
        PDF = Converter()
        PDF.pdfToImage(pdf_file_destination)
        PDF.imageToText(text_file_destination)
        PDF.removeImages()
    else:
        print("Unknown Extension we only except [png,jpg,jpeg and pdf] extensions")


pfdf_files = [
    "2005-08.pdf",
    "2005-12.pdf",
    "2005-17.pdf",
    "2005-18.pdf",
    "2005-24.pdf",
    "2005-29.pdf",
    "2005-32.pdf",
    "2005-34.pdf",
    "2005-38.pdf",
]


# Remove exesting text files in corpus/text that are similar to the pdf files in corpus/pdf


def remove_text_files(file: str):
    if os.path.exists(f"corpus/text/{file[:-4]}.txt"):
        os.remove(f"corpus/text/{file[:-4]}.txt")


def main(files):
    for file in files:
        remove_text_files(file)
        prepareTextFile(f"corpus/pdf/{file}", f"corpus/text/{file[:-4]}.txt")
        print(f"Converted {file} to text")


if __name__ == "__main__":
    start_time = time.time()
    main(pfdf_files)
    print(f"--- {time.time() - start_time} seconds ---")
