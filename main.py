import requests
from bs4 import BeautifulSoup

URL = "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2023/ANO2023-50"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="tcmbMainContent")
all_p = results.find_all('p')
if len(all_p) > 1:
    print("Release Date:", all_p[1].text.strip())

# Extract title
title = results.find('h2').text.strip()
print("Title:", title)

# Extract summary/body text
summary = results.find('div', class_='tcmb-content').text.strip()
print("Summary/Body Text:", summary)


