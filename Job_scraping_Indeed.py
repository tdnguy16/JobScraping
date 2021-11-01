import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas


def extract(page):
    url = f'https://www.indeed.com/jobs?q=institutional%20research&start={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    job_title = soup.select('h2', class_='jobTitle')
    job_list = []
    for job in job_title:
        title = (job.find_all('span')[-1]).text
        job_list.append(title)
    # print(len(job_list))
    # print(job_list)

    company_name = soup.select('pre')
    company_list = []
    for company in company_name:
        name = (company.find('span')).text
        company_list.append(name)
    # print(len(company_list))
    # print(company_list)

    location = soup.select('pre')
    location_list = []
    for loc in location:
        city = (loc.find('div')).text
        location_list.append(city)
    # print(len(location_list))
    # print(location_list)

    # listings = {}
    # for key in job_list:
    #     for value in company_list:
    #         listings[key] = value
    #         company_list.remove(value)
    #         break

    for i in range(len(job_list)):
        listings = []
        for key in job_list:
            listings.append(key)
            job_list.remove(key)
            for value in company_list:
                listings.append(value)
                company_list.remove(value)
                for loc in location_list:
                    listings.append(loc)
                    location_list.remove(loc)
                    total_list.append(listings)
                    break
                break
            break
    # print(len(listings))
    # print(listings)
    return

total_list = []

for i in range(0,20,10):
    c = extract(i)
    transform(c)

print(len(total_list))
print(total_list)

data = pd.DataFrame(total_list)
print(data)