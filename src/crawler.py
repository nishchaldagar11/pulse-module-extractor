import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


class DocumentationCrawler:
    def __init__(self, base_url, max_pages=30, delay=1):
        self.base_url = base_url.rstrip("/")
        self.max_pages = max_pages
        self.delay = delay
        self.visited_urls = set()
        self.pages_content = []

    def is_valid_url(self, url):
        return urlparse(url).netloc == urlparse(self.base_url).netloc
    
    
    def fetch_page(self, url):
        try:
            response = requests.get(
                url,
                timeout=6,
                headers={
                    "User-Agent": "Mozilla/5.0 (compatible; PulseBot/1.0)"
                },
            )

            if response.status_code == 200:
                return response.text

        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")

        return None



    def extract_links(self, soup, current_url):
        links = set()
        for tag in soup.find_all("a", href=True):
            full_url = urljoin(current_url, tag["href"])
            if self.is_valid_url(full_url):
                links.add(full_url.split("#")[0])
        return links

    def crawl(self):
        queue = [self.base_url]

        while queue and len(self.visited_urls) < self.max_pages:
            url = queue.pop(0)
            if url in self.visited_urls:
                continue

            print("[CRAWLING]", url)
            html = self.fetch_page(url)
            if not html:
                continue

            soup = BeautifulSoup(html, "html.parser")
            self.pages_content.append({"url": url, "soup": soup})
            self.visited_urls.add(url)

            for link in self.extract_links(soup, url):
                if link not in self.visited_urls:
                    queue.append(link)

            time.sleep(self.delay)

        return self.pages_content



