import requests
from bs4 import BeautifulSoup
# from src.downloader.constants import YEARS




class CSVDownloader:
    # def __init__(self, url:str):
    #     pass
    # URL = f"ht)tps://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/{YEARS}/ANO{YEARS}-50"
    # def prepare(self,Years:list, pageLimit:int):
    
    def read(self,years:list,pageLimit:int):
        for year in years:
            print(f"Initiating with a new year {year}")
            for page in range(53,pageLimit):
                url = f"https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/{year}/ANO{year}-{page}"
                print(url)
                try:
                    page = requests.get(url) 
                    print(page)
                    soup = BeautifulSoup(page.content, "html.parser")
                    results = soup.find(id="tcmbMainContent")
                    if results == None:
                        break
                    all_p = results.find_all('p')
                    if len(all_p) > 1:
                        print("Release Date:", all_p[1].text.strip())
                    # Extract title
                    title = results.find('h2').text.strip()
                    print("Title:", title)
                    # Extract summary/body text
                    summary = results.find('div', class_='tcmb-content').text.strip()
                    print("Summary:", summary)
                except:
                    print("Page out of limit")
    def save_to_csv(self):
        pass


