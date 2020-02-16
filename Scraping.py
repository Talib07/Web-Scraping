# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 01:24:18 2020

@author: Talib
"""

import bs4,requests

res = requests.get("https://www.lipsum.com/")       

type(res)

scrapped = bs4.BeautifulSoup(res.text,'html.parser')

elements = scrapped.select("#Panes > div:nth-child(1) > p")
                           
len(elements)
                    
elements[0].getText()