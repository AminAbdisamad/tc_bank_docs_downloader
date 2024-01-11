from src.downloader.csv_downloader import CSVDownloader
from src.downloader.constants import YEARS_FROM_2014_TO_2023, MAX_PAGES

# Loop through the years (2014 - 2023)
# Loop through pages (1 - 80)


# URL = "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2014/ANO2014-80"
# for year in YEARS_FROM_2014_TO_2023:
#     # 2014
#     for page in pageLimit:
#         url = "hjdttt:{year}{page}"


csv_downloader = CSVDownloader()

content = csv_downloader.read(years=YEARS_FROM_2014_TO_2023,page_limit=MAX_PAGES)
csv_downloader.save_to_csv("central_bank_press_release.csv")
# csv_downloader.save(content)

# TODO: 
# 1. Fix for pages that start with 01 - DOne
# 2. Save data to csv file - Done


