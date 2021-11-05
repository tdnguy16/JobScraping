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

        # FIND REQUIRED SKILLS
        r = requests.get(job_link)
        soup = BeautifulSoup(r.text, 'html.parser')

        skills_list = ['python', 'sas', 'excel', 'tableau', 'power bi', 'sql', 'spss', 'sap', 'matlab']
        skills_required = []

        job_details = soup.find_all('div', 'jobsearch-jobDescriptionText')
        for job_detail in job_details:
            text = job_detail.text.lower()

            for skill in skills_list:
                if skill in text:
                    skills_required.append(skill)

        job_types = soup.find_all('div', 'jobsearch-JobDescriptionSection-sectionItem')
        for job_type in job_types:
            type = job_type.find_all('div')[-1].text
            job_list.append(type)

        job_list.append(skills_required)

        # COMBINE INFO INTO A LIST OF LISTS
        total_list.append(job_list)

total_list = []

# SCRAPE THROUGH PAGES
for i in range(0, 10, 10):
    c = extract(i)
    transform(c)

# Make Dataframe from lists of jobs
data = pd.DataFrame(total_list, columns=('Job', 'Company', 'Location', 'Website', 'Type', 'Skills'))
print(data)

# Export dataframe to an excel file
data.to_excel("IRjob.xlsx")