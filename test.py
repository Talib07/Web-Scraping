# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:53:54 2020

@author: Talib
"""
import requests, sys, webbrowser, bs4
print('Searching...')    # display text while downloading the search result page
#wb = webbrowser.open_new_tab('https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res = requests.get('https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')

elements = soup.select('.package-snippet')

#Displaying the scrapped contents

for i in elements:
    print(i.getText())
    
#opening all in individual tabs

no_of_tabs = min(len(elements),5)

for i in range(no_of_tabs):
    open_tab = 'https://pypi.org/' + elements[i].get("href")
    webbrowser.open(open_tab)
    
    
    

