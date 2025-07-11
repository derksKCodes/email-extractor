import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

# -------------------------------------------
input_file = 'files/sampleInput.xlsx'
output_file = 'files/rado_sample_with_emails.xlsx'
max_workers = 5
# -------------------------------------------

# Load DataFrame
df = pd.read_excel(input_file)
print(f"Loaded {len(df)} rows from {input_file}")

# Email regex
email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

# Requests helper
def safe_get(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.text
    except:
        pass
    return None

# Extract emails
def find_emails_in_html(html):
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return list(set(email_pattern.findall(text)))

# Find social media links
def find_social_links(html, base_url):
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if any(social in href for social in ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com']):
            if not urlparse(href).netloc:
                href = urljoin(base_url, href)
            links.append(href)
    return list(set(links))

# Selenium setup per thread
thread_local = threading.local()
def get_driver():
    driver = getattr(thread_local, "driver", None)
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=chrome_options)
        thread_local.driver = driver
    return driver

def wait_for_page_load(driver, timeout=15):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
    except:
        pass
    
# Scrape email from social media using Selenium
def scrape_social_media_email(link):
    try:
        driver = get_driver()
        driver.get(link)
        wait_for_page_load(driver)  # Wait for content
        page_source = driver.page_source
        emails = list(set(email_pattern.findall(page_source)))
        if emails:
            return emails[0]
    except Exception as e:
        print(f"Error scraping social: {e}")
    return None

# Worker function
def process_row(idx):
    website_url = df.iloc[idx, 10]  # Column K
    found_email = None

    if pd.notna(website_url) and website_url != "-":
        html = safe_get(website_url)
        emails = find_emails_in_html(html)
        if emails:
            found_email = emails[0]
        else:
            # Try subpages
            for sub in ['contact', 'about', 'privacy-policy', 'About', 'Contact', 'Privacy-Policy']:
                sub_url = urljoin(website_url, sub)
                sub_html = safe_get(sub_url)
                emails = find_emails_in_html(sub_html)
                if emails:
                    found_email = emails[0]
                    break
            # Try social media
            if not found_email:
                social_links = find_social_links(html, website_url)
                for link in social_links:
                    email_from_social = scrape_social_media_email(link)
                    if email_from_social:
                        found_email = email_from_social
                        break

    if found_email:
        df.iat[idx, 9] = found_email  # Column J
        # Save immediately
        df.to_excel(output_file, index=False)
        print(f"[{idx}/{len(df)}] Processed: {website_url} -> {found_email}")
    else:
        print(f"[{idx}/{len(df)}] No email found: {website_url}")

    return idx

# Parallel execution
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = [executor.submit(process_row, idx) for idx in range(len(df))]
    for future in as_completed(futures):
        future.result()

# Cleanup Selenium drivers
try:
    driver = getattr(thread_local, "driver", None)
    if driver:
        driver.quit()
except:
    pass

print(f"Done! Saved updated data to {output_file}")
