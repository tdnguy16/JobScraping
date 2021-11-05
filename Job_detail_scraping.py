import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas


url = 'https://www.indeed.com/viewjob?jk=9564b8d31599d030&from=serp&vjs=3'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

skills_list = ['python', 'sas', 'excel', 'tableau', 'power bi', 'sql', 'matlab']
skills_required = []

job_details = soup.find_all('div', 'jobsearch-jobDescriptionText')
for job_detail in job_details:
    text = job_detail.text.lower()
    # print(text)

    for skill in skills_list:
        if skill in text:
            skills_required.append(skill)

job_types = soup.find_all('div', 'jobsearch-JobDescriptionSection-sectionItem')
for type in job_types:
    x = type.find_all('div')[-1].text
    print(x)

# print(skills_required)

