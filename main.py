from src.downloader.csv_downloader import CSVDownloader
from src.downloader.constants import YEARS_FROM_2014_TO_2023, MAX_PAGES

csv_downloader = CSVDownloader()

content = csv_downloader.read(years=YEARS_FROM_2014_TO_2023,page_limit=MAX_PAGES)
csv_downloader.save_to_csv("central_bank_press_release.csv")


# TODO: 
# Explain these concepts
# 1. Multiple loops
# 2. Getting body from list of articles 
# 3. Code usage - Unifications 


 


