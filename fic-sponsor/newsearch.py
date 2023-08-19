import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

visited_urls = set()  # To keep track of visited URLs

def extract_emails_from_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    return emails

def get_emails_from_website_recursive(url, depth, max_depth):
    global visited_urls
    
    if depth > max_depth:
        return []  # Stop recursion if maximum depth is reached
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        base_url = url  # Used for resolving relative URLs
        
        emails = []  # To store email addresses
        
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(base_url, link['href'])
            visited_urls.add(absolute_url)
            emails += get_emails_from_website_recursive(absolute_url, depth + 1, max_depth)
        
        text = soup.get_text()  # Extract text from the page
        page_emails = extract_emails_from_text(text)
        emails += page_emails
        
        return emails
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

# Input from the user
website_url = input("Enter the website URL: ")
max_depth = int(input("Enter the maximum depth for recursion: "))

email_list = get_emails_from_website_recursive(website_url, depth=1, max_depth=max_depth)
print("Email addresses found:")
print(email_list)
