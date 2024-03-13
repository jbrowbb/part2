import os
from bs4 import BeautifulSoup
import requests

class AricleSpider:
    def __init__(self, urls_file):
        self.urls_files = urls_file

    def start_requests(self):
        with open(self.urls_file,'r') as file:      # reads urls from the file
            urls = file.readlines()

        for url in urls:        # scrapes the urls
            url = url.strip()

            try:
                response = requests.get(url)        # grabs page content
                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'html.parser')

                article_text = soup.get_text()

                yield article_text
            
            except Exception as e:
                print(f"Error scraping article from {url}: {e}")