# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:10:28 2020

@author: Talib
"""

import sys,os,bs4,webbrowser,requests

url = 'https://xkcd.com/'

os.makedirs('xkcd',exist_ok = True)

while not url.endswith("#"):
                       
                       print("Downloading page %s..."%url)
                       
                       res = requests.get(url)
                       
                       res.raise_for_status = True
                       
                       soup = bs4.BeautifulSoup(res.text,'html.parser')
                    
                       comicElem = soup.select('#comic img')
                       
                       if len(comicElem)==0:
                           
                           print("No Images")
                           
                       else:
                           
                           comicUrl = 'https:' + comicElem[0].get("src")
                           
                           print("Downloading image %s..."%(comicUrl))
                           
                           res = requests.get(comicUrl)
                           
                           res.raise_for_status = True
                           
                       #Save the image    
                       
                       imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
                       
                       for chunk in res.iter_content(100000):
                           
                           imageFile.write(chunk)
                           
                       imageFile.close()
                       
                       prevLink = soup.select('a[rel = "prev"]')[0]
                       
                       url = 'https://xkcd.com/' + prevLink.get("href")
                       
                       
print("Done")
                    
                           
                    
                           
                           
                           
                           
                       
                 
                                               
                       
                       
                                               
                                               
                                               
                                               
                      