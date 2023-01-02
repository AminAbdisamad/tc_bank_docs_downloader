import os
from pprint import pprint

# from . import constants
import re


def count_total_pdf_files() -> int:
    """Count number of PDF files in the corpus folder."""
    count = 0
    for file in os.listdir("./corpus/pdf"):
        if file.endswith(".pdf"):
            count += 1
    return count


def count_pdf_files_by_year() -> dict:
    """Count number of PDF files in the corpus folder."""
    years = {}
    count = 0
    for file in os.listdir("./corpus/pdf"):
        year = file[:4]
        if file.endswith(".pdf") and year.isdigit() and int(year):
            if year in years:
                years[year] += 1
            else:
                years[year] = 1

    return years


def count_text_files_by_year() -> dict:
    """Count number of text files in the corpus folder."""
    years = {}
    count = 0
    for file in os.listdir("./corpus/text"):
        year = file[:4]
        if file.endswith(".txt") and year.isdigit():
            if year in years:
                years[year] += 1
            else:
                years[year] = 1

    return years


pdf_files_count = count_total_pdf_files()
pdf_files_by_year_count = count_pdf_files_by_year()
count_total_text_files = count_text_files_by_year()
print(f"Number of PDF files in the corpus folder: {pdf_files_count}")
print("PDF Files by year : ")
pprint(pdf_files_by_year_count)
print("Text Files by year :")
pprint(count_total_text_files)
