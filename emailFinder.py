from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import re

def find_emails(company_name, num_results=5):
    ddgs = DDGS()
    search_query = f"{company_name} contact email"
    results = ddgs.text(search_query, max_results=num_results)
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = set()

    for result in results:
        url = result.get("href")
        if url:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    text = soup.get_text()
                    found_emails = re.findall(email_pattern, text)
                    emails.update(found_emails)
            except Exception as e:
                print(f"Error scraping {url}: {e}")

    return list(emails)

