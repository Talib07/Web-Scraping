import requests
import bs4

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=India'
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = "ResultsContainer")
job_elems = results.find_all('section', class_='card-content')

for jobs in job_elems:
    title = jobs.find('h2',class_ = 'title')
    company = jobs.find('div',class_ = 'company')
    location = jobs.find('div',class_ = 'location')
    if None in (title, company, location):
        continue
    job_title = title.getText().strip()
    company = company.getText().strip()
    job_location = location.getText().strip()
    print(job_title,end = '\n')
    print(company,end = "\n")
    print(job_location,end = "\n")
    print("\n\n\n")
