import os
from pprint import pprint
from constants import YEARS
import re


def count_total_pdf_files() -> int:
    """Count number of PDF files in the corpus folder."""
    count = 0
    for file in os.listdir("./corpus"):
        if file.endswith(".pdf"):
            count += 1
    return count


def count_pdf_files_by_year() -> dict:
    """Count number of PDF files in the corpus folder."""
    years = {}
    count = 0
    for file in os.listdir("./corpus"):
        year = file[:4]
        if file.endswith(".pdf") and year.isdigit() and int(year) in YEARS:
            if year in years:
                years[year] += 1
            else:
                years[year] = 1

    return years


pdf_files_count = count_total_pdf_files()
pdf_files_by_year_count = count_pdf_files_by_year()

print(f"Number of PDF files in the corpus folder: {pdf_files_count}")
pprint(pdf_files_by_year_count)
