from module_1 import scraper
from module_2 import spider
import os

def main():
    root_path = "CS325_p2"
    raw_data_path = os.path.join(root_path, "Data", "raw", "articles.txt")  # Path to the file containing the URLs
    processed_data_path = os.path.join(root_path, "Data", "processed")      # Path to store processed articles

    # Scrape articles and save them to separate files
    article_files = scraper.scrape_articles(raw_data_path)

    # Create an instance of ArticleSpider
    article_spider = spider.ArticleSpider(article_files)

    # Process each article
    for article_text in article_spider.start_requests():
        title = article_text.split('\n', 1)[0]  # Get the title

        processed_file_path = os.path.join(processed_data_path, f"{title}.txt")  # Create the file path for the processed article

        # Write the text to the file
        with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
            processed_file.write(article_text)

if __name__ == "__main__":
    main()