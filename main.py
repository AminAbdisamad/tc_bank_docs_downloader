from src.downloader.csv_downloader import CSVDownloader
from src.downloader.constants import YEARS_FROM_2014_TO_2023, MAX_PAGES

csv_downloader = CSVDownloader()

content = csv_downloader.read(years=YEARS_FROM_2014_TO_2023,page_limit=MAX_PAGES)
csv_downloader.save_to_csv("central_bank_press_release.csv")


# TODO: 
# 1. Fix for pages that start with 01 - DOne
# 2. Save data to csv file - Done


