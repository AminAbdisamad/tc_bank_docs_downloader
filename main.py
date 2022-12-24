import os
from pprint import pprint
from constants import YEARS
import requests
from bs4 import BeautifulSoup

# Set the URL of the website containing the PDF files

START_URL = "https://www.tcmb.gov.tr"


def prepare_pdf_links(url: str) -> list[str]:
    pdf_links = []
    response = requests.get(URL, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    href_links = soup.find_all(
        "a",
        href=lambda x: x and "CACHEID" in x,
    )
    for href_link in href_links:
        pdf_links.append(f"{START_URL}{href_link['href']}")
    return pdf_links


for year in YEARS:
    URL = f"https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/{year}"
    pdf_links = prepare_pdf_links(URL)
    with open(f"./data/{year}.txt", "w") as f:
        f.write("\n".join(pdf_links))
    pprint(pdf_links)


# pprint(pdf_links)


# for link in pdf_links:
#     year = link["href"].split("/")[-1][:4]

#     if not os.path.exists(year):
#         os.makedirs(year)
#     pdf_data = requests.get(link["href"]).content
#     with open(f"{year}/{link.text}.pdf", "wb") as f:
#         f.write(pdf_data)

# print("PDF files extracted and saved successfully!")
