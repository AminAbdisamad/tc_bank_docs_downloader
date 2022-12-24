import os
import time
from pprint import pprint
from constants import YEARS
import requests
from bs4 import BeautifulSoup

# Set the URL of the website containing the PDF files

START_URL = "https://www.tcmb.gov.tr"
# END_URL = "/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Enflasyon/Enflasyon+Verileri/Enflasyon+Verileri+Yillik/"
END_URL = "/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/"


def prepare_pdf_links(url: str) -> list[str]:
    pdf_links = []
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    href_links = soup.find_all(
        "a",
        href=lambda x: x and "CACHEID" in x,
    )
    for href_link in href_links:
        pdf_links.append(f"{START_URL}{href_link['href']}")
    return pdf_links


def get_all_pdf_links() -> list[str]:
    """Get all PDF links from the website."""
    pdf_links = []
    for year in YEARS:
        URL = f"{START_URL}{END_URL}{year}"
        pdf_links.extend(prepare_pdf_links(URL))
    return pdf_links


def save_pdf(links):
    for link in links:
        pdf_name = link.split("/")[-1][3:14]
        # Wait for 30 seconds before next request
        # time.sleep(1)
        response = requests.get(link, timeout=10)
        if response.status_code == 200:
            with open(f"./corpus/{pdf_name}", "wb") as pdf:
                pdf.write(response.content)
            print(f"{pdf_name} saved successfully.")
        else:
            print("Failed to download PDF.")


# specify the PDF link and the save path
# link = "https://www.tcmb.gov.tr/wps/wcm/connect/8e3be759-1cf8-4673-8e9d-86bfed321749/ANO2002-01.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8e3be759-1cf8-4673-8e9d-86bfed321749-m3fxC6l"
# save_path = os.path.join(os.getcwd(), "ANO2002-01.pdf")

if __name__ == "__main__":
    print("Please wait while the PDF files are being extracted and saved...")
    links = get_all_pdf_links()
    try:
        save_pdf(links)
    except Exception as e:
        print(f"Error: {e}")
    print("Hoorrah!!! PDF files extracted and saved successfully!")
