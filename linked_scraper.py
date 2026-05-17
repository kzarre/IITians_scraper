import json
import random
import time
import re
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import pyautogui as pag
cookies = {}

with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# urls = [ ... your 380 links ... ]
urls = [
"https://www.linkedin.com/in/vamshi-jatothu/",
"https://www.linkedin.com/in/deepika-podugu-209161202/",
"https://www.linkedin.com/in/LINKEDINUSERID/"
]


def recheck(s):
    pattern = r"([ a-zA-Z0-9\(\)_,.:=-]+) · Indian Institute of Technology, Guwahati"
    match = re.search(pattern, s)
    if match:
        name_only = match.group(1)
        return name_only.strip()
    else:
        return ""


def define_and_scrape(urls):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])

        companies = [" "]*len(urls)
        stealth = Stealth()
        context = browser.new_context()
        context.add_cookies(cookies)

        page = context.new_page()
        stealth.apply_stealth_sync(page)

        for idx, url in enumerate(urls):
            url = str(url)
            print(idx+1, end=" ")
            if len(url) < 15:
                print("weird URL:", url)
                continue

            company = scrape(page, url)
            companies[idx] = company
            print(company)
            time.sleep(random.uniform(15.0, 30.0))

        return companies

def scrape(page, url):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=15000)

        current_url = page.url
        if "checkpoint" in current_url or "login" in current_url:
            print("\n[CRITICAL] Security checkpoint or logout detected!")
            import sys
            sys.exit(1)

        time.sleep(random.uniform(2, 5)) 

        scroll_amount = random.randint(400, 800)
        page.mouse.wheel(0, scroll_amount)
        time.sleep(random.uniform(3, 6))

        page.mouse.wheel(0, -int(scroll_amount / 2))

        html = page.content()
        company = recheck(html)
        return company
    except Exception as e:
        print(f"Skipping {url} due to error: {e}")
        return " "


if __name__ == "__main__":
    define_and_scrape(urls[:1])
