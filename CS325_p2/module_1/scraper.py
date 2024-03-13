import os 
from bs4 import BeautifulSoup
import requests

def scrape_articles(urls_file):     # create an output directory if url doesn't exist
    output_dir = 'Data/processed'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(urls_file,'r') as file:       # reads urls from file
        urls = file.readlines()

    for idx, url in enumerate(urls):        #scrapes the urls
        url = url.strip()

        try:
            response = requests.get(url)
            response.raise_for_status()     # get teh page content

            soup = BeautifulSoup(response.content, 'html.parse')    # parse the HTML

            article_text = soup.get_text()  # gets the text from the articles

            article_file = os.path.join(output_dir, f'article_{idx + 1}.txt')
            with open(article_file,'w', encoding='utf-8') as f:
                f.write(article_text)

                print(f"Article {idx + 1} scaped and saved")
        
        except Exception as e:
            print(f"Error scraping article {idx + 1}: {e}")