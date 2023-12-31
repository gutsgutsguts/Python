from requests import get
from bs4 import BeautifulSoup
from wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    serch_term = "python"

    browser = webdriver.Chrome(options=options)

    response = browser.get(f"{base_url}{keyword}")
    
    if response.status_code != 200:
        print("Cant request page")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination-list")
        if pagination == None:
            return 1

        pages = pagination.find_all("li", recursive=False)
        count = len(pages)

        if count >= 5:
            return 5
        else:
            return count 

print(get_page_count("python"))



def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        serch_term = "python"

        browser = webdriver.Chrome(options=options)

        response = browser.get(final_url)
        
        if response.status_code != 200:
            print("Cant request page")
        else:

            soup = BeautifulSoup(browser.page_source, "html.parser")
            job_list = soup.find("ul", class_="jobsearch-ResultsList")

            jobs = job_list.find_all('li', recursive=False)

            results = []

            for job in jobs:
                zone = job.find("div", class_="mosaic-zone")
                if zone == None:
                    anchor = job.select_one("h2 a")
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")

                    job_data = {
                    'link' : f"https://kr.indeed.com{link}",
                    'company' : company.string,
                    'location' : location.string,
                    'position' : title
                    
                }

            results.append(job_data)

    for result in results:
        print(result, "///////\n/////////")
