import requests
import bs4

URL = 'https://www.bbc.com/news/world'
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_ = "no-mpu")


top_news = results.find(class_ = "gel-layout__item gs-u-pb+@m gel-1/1 gel-1/1@xl gel-2/5@xxl gs-u-ml0 nw-o-keyline nw-o-no-keyline@m")
title = top_news.find('h3',class_ = "gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text")
title = title.getText().strip()
description = top_news.find('p',class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
description = description.getText().strip()
time = top_news.find('span', class_="gs-u-vh")
if time is None:
    time = 'Live'
else:
    time = time.getText().strip()
location = top_news.find('a',class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state")
location = location.getText().strip()

print('Title : ' + str(title),end = '\n')
print('Description : '+ str(description),end = "\n")
print('Time : ' + str(time),end = "\n")
print('Location or Domain : ' + str(location),end = "\n\n\n")

classes = ["gel-layout__item gs-u-pb+@m gel-1/3@m gel0-1/4@xl gel-1/3@xxl nw-o-keyline nw-o-no-keyline@m",
           "gel-layout__item gs-u-pb+@m gel-1/3@m gel-1/4@xl gel-1/3@xxl nw-o-keyline nw-o-no-keyline@m"]

for _ in classes:
    news = results.find_all('div',class_= _)
    
    for single_news in news:
        title = single_news.find('h3',class_ = "gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
        description = single_news.find('p',class_ = "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m")
        time = single_news.find("span",class_ = 'gs-u-vh')
        location = single_news.find('a',class_ = "gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state")
        new = [title,description,time,location]
        if None in new:
            continue
        title = title.getText().strip()
        description = description.getText().strip()
        time = time.getText().strip()
        location = location.getText().strip()
        print('Title : ' + str(title),end = '\n')
        print('Description : '+ str(description),end = "\n")
        print('Time : ' + str(time),end = "\n")
        print('Location or Domain : ' + str(location),end = "\n\n\n")
