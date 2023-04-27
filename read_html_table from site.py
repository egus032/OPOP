
import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen('https://www.tu-bryansk.ru/sveden/education/eduop/')

soup = BeautifulSoup(url, 'html.parser')

pattern = ['№', 'Код, шифр группы научных специальностей' ]

text_1 = soup.find('th', text = pattern[0])
print(text_1.text)

text_2 = soup.find('th', text = pattern[1])
print(text_2.text)
