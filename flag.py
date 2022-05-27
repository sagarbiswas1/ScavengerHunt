#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url = 'http://mercury.picoctf.net:44070/'

add = ['','mycss.css','robots.txt','.htaccess','.DS_Store']

# split by those words
OtherParts = ['Part 3: ','Part 4: ','Part 5: ']

html_text = []


def others(listNo,resp):
    try:
        parts = resp.split(OtherParts[listNo])[1].split('\n')[0]
    except:
        parts = resp.split(OtherParts[listNo])[1]
    html_text.append(parts)


def req(url,counter):
    resp = requests.get(url).text
    if counter == 0:
        soup = BeautifulSoup(resp, 'html.parser')
        # find comments
        parts = soup.find_all(string=lambda text: isinstance(text, Comment))
        html_text.append(str(parts).split('flag: ')[1].replace(' ','').replace('"]',''))
    elif counter == 1:
        parts = resp.split('part 2: ')[1].split('*/')[0]
        html_text.append(parts.replace(' ',''))
    elif counter == 2:
        others(0,resp)
    elif counter == 3:
        others(1,resp)
    elif counter == 4:
        others(2,resp)


counter = 0
for x in add:
    URL = url+x
    req(URL,counter)
    counter += 1

# print the flag
print(f'\033[34m{html_text[0]+html_text[1]+html_text[2]+html_text[3]+html_text[4]}\033[0m')