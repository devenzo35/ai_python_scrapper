import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print('launching chrome browser')

    chrome_driver_path='./chromedriver'
    options= webdriver.ChromeOptions()
    driver= webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print('page loaded...')
        html= driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else: 
        return ''
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in body_content(['script'], ['style']):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip() )

    return cleaned_content