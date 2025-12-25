import json
import os

from src.crawler import DocumentationCrawler
from src.parser import DocumentationParser
from src.extractor import ModuleExtractor
from src.summarizer import DescriptionSummarizer
from src.utils import is_valid_url


def run_pipeline(url, max_pages=15):
    print(f"\n[INFO] Starting module extraction for: {url}")

    crawler = DocumentationCrawler(base_url=url, max_pages=max_pages)
    pages = crawler.crawl()
    print(f"[INFO] Crawled {len(pages)} pages")

    parser = DocumentationParser()
    sections = parser.parse_pages(pages)
    print(f"[INFO] Extracted {len(sections)} sections")

    extractor = ModuleExtractor()
    modules_dict = extractor.extract_modules(sections)
    modules = extractor.format_output(modules_dict)
    print(f"[INFO] Identified {len(modules)} modules")

    summarizer = DescriptionSummarizer(max_length=250)
    final_output = summarizer.summarize_modules(modules)

    return final_output


def save_output(data, filename):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Output saved → {filepath}")


if __name__ == "__main__":

    # ===== MULTIPLE WEBSITES (PDF-COMPLIANT) =====
    TARGET_WEBSITES = {
        "https://help.instagram.com/": "instagram_modules.json",
        "https://wordpress.org/documentation/": "wordpress_modules.json",
        "https://support.neo.space/hc/en-us": "neo_modules.json",
        "https://help.zluri.com/": "zluri_modules.json",
        "https://docs.github.com/en": "github_modules.json"

    }

    for url, output_file in TARGET_WEBSITES.items():
        if not is_valid_url(url):
            print(f"[ERROR] Invalid URL skipped: {url}")
            continue

        result = run_pipeline(url, max_pages=15)
        save_output(result, output_file)

    print("\n✅ All websites processed successfully")
