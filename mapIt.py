# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:17:33 2020

@author: Talib
"""
import webbrowser,sys,pyperclip,requests,bs4

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open('https://forecast.weather.gov/' + address)

