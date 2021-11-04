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
        # GET JOB TITLE
        job_title = post.h2('span')[-1].text
        print(job_title)


        # GET COMPANY NAME
        company_name = post.pre.find('span').text
        print(company_name)

        # GET COMPANY LOCATION
        company_location = post.find('div', 'companyLocation').text
        print(company_location)


        # GET LINK TO JOB DETAILS
        links = soup.find_all('a', 'tapItem')
        links_list = []
        for link in links:
            x = 'https://www.indeed.com' + link.get('href')
            links_list.append(x)
        # print(len(links_list))
        # print(links_list)

    # COMBINE INFO INTO A LIST OF LISTS
    # for i in range(len(job_list)):
    #     listings = []
    #     for key in job_list:
    #         listings.append(key)
    #         job_list.remove(key)
    #         total_list.append(listings)
    # print(len(listings))
    # print(listings)
    # return

total_list = []

# SCRAPE THROUGH PAGES
for i in range(0,10,10):
    c = extract(i)
    transform(c)

# print(len(total_list))
# print(total_list)
#
# data = pd.DataFrame(total_list, columns=('Job','Company','Location','Website'))
# print(data)
#
# data.to_excel("IRjob.xlsx")