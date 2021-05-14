import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.brightermonday.co.ke/jobs/software-data/nairobi').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', class_='search-result')
for job in jobs:
    job_vacancy = job.find('h3').text.replace(' ', '')
    company_name = job.find('div', class_='if-content-panel padding-lr-20 flex-direction-top-to-bottom--under-lg align--start--under-lg search-result__job-meta').text.replace(' ','')
    location = job.find('div', class_='search-result__location').text.replace(' ', '')

    print(f"Vacancy:{job_vacancy}")
    print(f"Company Name:{company_name.strip()}")
    print(f"Job Location:{location.strip()}")

    print('')
