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

URL = "https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2014/ANO2014-80"
csv_downloader = CSVDownloader()

content = csv_downloader.read(URL)
# csv_downloader.save(content)
