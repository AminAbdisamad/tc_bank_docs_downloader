from src.downloader.csv_downloader import CSVDownloader

data_limit = [
    {
        "year":"2014",
        "limit":"78"
    },
     {
        "year":"2015",
        "limit":"78"
    }
]

# Loop through the years (2014 - 2023)
# Loop through pages (1 - 80)


# URL = "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2014/ANO2014-80"
# for year in YEARS_FROM_2014_TO_2023:
#     # 2014
#     for page in pageLimit:
#         url = "hjdttt:{year}{page}"


csv_downloader = CSVDownloader()

content = csv_downloader.read(years=['2022','2023'],pageLimit=70)
# csv_downloader.save(content)
