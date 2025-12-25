from bs4 import BeautifulSoup


class DocumentationParser:
    def __init__(self):
        pass

    def remove_noise(self, soup):
        """
        Remove unwanted tags like nav, footer, scripts, styles
        """
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        return soup

    def extract_sections(self, soup):
        """
        Extract headings (H1, H2, H3) with their related text
        """
        sections = []
        current_section = None

        for element in soup.find_all(["h1", "h2", "h3", "p", "ul", "ol"]):
            if element.name in ["h1", "h2", "h3"]:
                if current_section:
                    sections.append(current_section)

                current_section = {
                    "level": element.name,
                    "title": element.get_text(strip=True),
                    "content": []
                }

            else:
                if current_section:
                    text = element.get_text(" ", strip=True)
                    if text:
                        current_section["content"].append(text)

        if current_section:
            sections.append(current_section)

        return sections

    def parse_page(self, soup):
        """
        Clean HTML and extract structured sections
        """
        soup = self.remove_noise(soup)
        sections = self.extract_sections(soup)
        return sections

    def parse_pages(self, pages):
        """
        Parse multiple crawled pages
        """
        all_sections = []

        for page in pages:
            page_sections = self.parse_page(page["soup"])
            all_sections.extend(page_sections)

        return all_sections