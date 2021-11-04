import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas


def extract(page):
    url = f'https://www.indeed.com/jobs?q=institutional%20research&start={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def transform(soup):
    job_posts = soup.find_all('a', 'tapItem')
    for post in job_posts:
        job_list = []
        # GET JOB TITLE
        job_title = post.h2('span')[-1].text
        job_list.append(job_title)

        # GET COMPANY NAME
        company_name = post.pre.find('span').text
        job_list.append(company_name)

        # GET COMPANY LOCATION
        company_location = post.find('div', 'companyLocation').text
        job_list.append(company_location)

        # GET LINK TO JOB DETAILS
        job_link = 'https://www.indeed.com' + post.get('href')
        job_list.append(job_link)

        # COMBINE INFO INTO A LIST OF LISTS
        total_list.append(job_list)

total_list = []

# SCRAPE THROUGH PAGES
for i in range(0,30,10):
    c = extract(i)
    transform(c)

# Make Dataframe from lists of jobs
data = pd.DataFrame(total_list, columns=('Job','Company','Location','Website'))
print(data)

# Export dataframe to an excel file
data.to_excel("IRjob.xlsx")