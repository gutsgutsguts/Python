from requests import get
from bs4 import BeautifulSoup
from wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

base_url = "https://kr.indeed.com/jobs?q="

browser.get("https://weworkremotely.com/remote-jobs/search?term=python")


print(browser.page_source)


while(True):
    pass
