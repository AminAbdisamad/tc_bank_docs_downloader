import requests
from bs4 import BeautifulSoup
from src.downloader.constants import YEARS




class CSVDownloader:
    # URL = f"https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/{YEARS}/ANO{YEARS}-50"
    def read(self,url:str):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        print(soup)
        results = soup.find(id="tcmbMainContent")
        # if results == None:
        #     break;
        all_p = results.find_all('p')
        if len(all_p) > 1:
            print("Release Date:", all_p[1].text.strip())
        # Extract title
        title = results.find('h2').text.strip()
        print("Title:", title)
        # Extract summary/body text
        summary = results.find('div', class_='tcmb-content').text.strip()
        print("Summary:", summary)
    def save_to_csv(self):
        pass


