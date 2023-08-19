import requests
from bs4 import BeautifulSoup
import re
import sys
import concurrent.futures
from collections import deque
from urllib.parse import urljoin
import threading

# Configure console output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Global variables
visited_urls = set()
visited_urls_lock = threading.Lock()

def get_website_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No title found"
        return title
    except (requests.exceptions.RequestException, AttributeError):
        return "Error fetching information"

def get_emails_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, soup.get_text())
        return emails
    except (requests.exceptions.RequestException, AttributeError):
        return []

if __name__ == "__main__":
    starting_url = input("Enter the URL for depth scraping: ")
    max_depth = int(input("Enter the maximum depth for the depth-first search: "))

    def scrape_depth_first(url, depth):
        if depth > max_depth:
            return []

        with visited_urls_lock:
            if url in visited_urls:
                return []
            visited_urls.add(url)

        emails = get_emails_from_url(url)
        if emails:
            website_info = get_website_info(url)
            return [(website_info, url, emails)]

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)

            result = []
            for link in links:
                new_url = urljoin(url, link['href'])
                if new_url.startswith('http'):
                    result.extend(scrape_depth_first(new_url, depth + 1))
            return result
        except (requests.exceptions.RequestException, AttributeError):
            return []

    final_website_info_list = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scrape_depth_first, starting_url, 0)]

        for future in concurrent.futures.as_completed(futures):
            final_website_info_list.extend(future.result())

    print("Websites with emails:")
    for index, (website_info, url, _) in enumerate(final_website_info_list, start=1):
        print(f"{index}. {website_info} - {url}")

    email_list = [email for _, _, emails in final_website_info_list for email in emails]
    print("List of email addresses:", email_list)
