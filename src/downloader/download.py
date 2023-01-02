import os
import time
from pprint import pprint
import tempfile
import PyPDF2

# from downloader.constants import YEARS, START_URL, END_URL
import requests
from bs4 import BeautifulSoup

# Constants
YEARS = [
    # 2022,
    # 2021,
    # 2020,
    # 2019,
    # 2018,
    # 2017,
    # 2016,
    # 2015,
    # 2014,
    # 2013,
    # 2012,
    # 2011,
    # 2010,
    # 2009,
    # 2008,
    # 2007,
    # 2006,
    # 2005,
    # 2004,
    # 2003,
    2002,
]


START_URL = "https://www.tcmb.gov.tr"
# END_URL = "/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Enflasyon/Enflasyon+Verileri/Enflasyon+Verileri+Yillik/"
END_URL = "/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/"


class Download:
    def prepare_pdf_links(self, url: str) -> list[str]:
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

    def get_all_pdf_links(self) -> list[str]:
        """Get all PDF links from the website."""
        pdf_links = []
        for year in YEARS:
            URL = f"{START_URL}{END_URL}{year}"
            pdf_links.extend(self.prepare_pdf_links(URL))
        return pdf_links

    def save(self, extention: str = "pdf"):
        for link in self.get_all_pdf_links():
            name = link.split("/")[-1][3:10]
            response = requests.get(link, timeout=10)
            if response.status_code == 200 and extention == "pdf":
                with open(f"./corpus/{name}.pdf", "wb") as pdf:
                    pdf.write(response.content)
                print(f"{name} saved successfully.")
            elif response.status_code == 200 and extention == "txt":
                # Save the text file

                with open(f"./corpus/text/{name}.txt", "wb") as text:
                    text.write(response.content)
                print(f"{name} saved successfully.")
            else:
                print("Failed to download files.")

    def save_text_file(self):
        for link in self.get_all_pdf_links():
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                name = link.split("/")[-1][3:10]
                with tempfile.TemporaryFile() as file:
                    file.write(response.content)
                    file.seek(0)
                    reader = PyPDF2.PdfReader(file)
                    with open(f"./corpus/text/{name}.txt", "w") as text_file:
                        for page in reader.pages:
                            text = page.extract_text()
                            text_file.write(text)
                            print(f"{name} saved successfully.")
            else:
                print("Failed to download files.")


# specify the PDF link and the save path
# link = "https://www.tcmb.gov.tr/wps/wcm/connect/8e3be759-1cf8-4673-8e9d-86bfed321749/ANO2002-01.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8e3be759-1cf8-4673-8e9d-86bfed321749-m3fxC6l"
# save_path = os.path.join(os.getcwd(), "ANO2002-01.pdf")

if __name__ == "__main__":

    print("Please wait while the PDF files are being extracted and saved...")
    downloader = Download()
    try:
        # downloader.save("txt")
        downloader.save_text_file()
    except Exception as e:
        print(f"Error: {e}")
    print("Hoorrah!!! PDF files extracted and saved successfully!")
