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
    # GET JOB TITLE
    job_title = soup.find_all('h2', 'jobTitle')
    job_list = []
    for job in job_title:
        title = (job.find_all('span')[-1]).text
        job_list.append(title)
    # print(len(job_list))
    # print(job_list)

    # GET COMPANY NAME
    company_name = soup.find_all('pre')
    company_list = []
    for company in company_name:
        name = (company.find('span')).text
        company_list.append(name)
    # print(len(company_list))
    # print(company_list)

    # GET COMPANY LOCATION
    location = soup.find_all('pre')
    location_list = []
    for loc in location:
        city = (loc.find('div')).text
        location_list.append(city)
    # print(len(location_list))
    # print(location_list)

    # GET LINK TO JOB DETAILS
    links = soup.find_all('a', 'tapItem')
    links_list = []
    for link in links:
        x = 'https://www.indeed.com' + link.get('href')
        links_list.append(x)
    # print(len(links_list))
    # print(links_list)

    # COMBINE INFO INTO A LIST OF LISTS
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
                    for link in links_list:
                        listings.append(link)
                        links_list.remove(link)
                        total_list.append(listings)
                        break
                    break
                break
            break
    # print(len(listings))
    # print(listings)
    return

total_list = []

# SCRAPE THROUGH PAGES
for i in range(0,100,10):
    c = extract(i)
    transform(c)

print(len(total_list))
print(total_list)

data = pd.DataFrame(total_list, columns=('Job','Company','Location','Website'))
print(data)

data.to_excel("IRjob.xlsx")