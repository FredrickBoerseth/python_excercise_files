import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Scraper:
    def __init__(self, site):
        self.site = site


    def scrape(self):
        req = urllib.request.Request(
        self.site,
        headers={"User-Agent": "Mozilla/5.0"}
    )
        html = urllib.request.urlopen(req).read()

        sp = BeautifulSoup(html, "html.parser")

        with open("st.txt", "w", encoding="utf-8") as f:
            for tag in sp.find_all("a", href=True):
                url = urljoin(self.site, tag["href"])
                print(url)
                f.write(url + "\n")

news = "https://news.google.com"
Scraper(news).scrape()

