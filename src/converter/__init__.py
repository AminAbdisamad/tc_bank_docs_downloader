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
    "2004-2.pdf",
    "2004-7.pdf",
    "2004-14.pdf",
    "2004-18.pdf",
    "2004-25.pdf",
    "2004-26.pdf",
    "2004-28.pdf",
    "2004-31.pdf",
    "2004-37.pdf",
    "2004-39.pdf",
    "2004-40.pdf",
    "2004-43.pdf",
    "2004-42.pdf",
]
pdfs = [
    "2002-15.pdf",
    "2002-21.pdf",
    "2002-54.pdf",
]


# Remove exesting text files in corpus/text that are similar to the pdf files in corpus/pdf


def remove_text_files(file: str):
    if os.path.exists(f"corpus/text/{file[:-4]}.txt"):
        os.remove(f"corpus/text/{file[:-4]}.txt")


def main(files):
    # converter = Converter()
    for file in files:
        # remove_text_files(file)
        # converter.ocr_pdf_to_text(f"corpus/pdf/{file}", f"corpus/text/{file[:-4]}.txt")
        prepareTextFile(f"corpus/pdf/{file}", f"corpus/test/{file[:-4]}.txt")
        print(f"Converted {file} to text")


if __name__ == "__main__":
    start_time = time.time()
    main(pdfs)
    print(f"--- {time.time() - start_time} seconds ---")
