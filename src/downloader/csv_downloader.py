import requests
from bs4 import BeautifulSoup
import pandas as pd

class CSVDownloader:
    def __init__(self):
        self.data = []

    def read(self, years, page_limit):
        for year in years:
            print(f"Initiating with a new year {year}")
            for page in range(1, page_limit + 1):  # Adjust the range to include 01, 02, etc.
                page_str = str(page).zfill(2)  # Format page number with leading zero if needed
                url = f"https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/{year}/ANO{year}-{page_str}"

                try:
                    page_response = requests.get(url)
                    page_content = page_response.content
                    soup = BeautifulSoup(page_content, "html.parser")
                    results = soup.find(id="tcmbMainContent")

                    if results is None:
                        continue
                    release_date = results.find_all('p')[1].text.strip()
                    title = results.find('h2').text.strip()
                    summary = results.find('div', class_='tcmb-content').text.strip()

                    # Append data to list
                    self.data.append({'Year': year, 'Release Date': release_date, 'Title': title, 'Summary': summary})

                except Exception as e:
                    print(f"Error processing page {url}: {str(e)}")

    def save_to_csv(self, filename='output.csv'):
        if self.data:
            df = pd.DataFrame(self.data)
            df.to_csv(filename, index=False,)
            print(f"Data saved to {filename}")
        else:
            print("No data to save.")




