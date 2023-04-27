# import requests
# from bs4 import BeautifulSoup
 
 
# g_url = 'https://www.tu-bryansk.ru/sveden/education/eduop/'
# reqs = requests.get(g_url)
# soup = BeautifulSoup(reqs.text, 'html.parser')
 
# urls = []
# for link in soup.find_all('a'):
#     print(str(link.get('href')))



# from urllib.request import urlopen
# from bs4 import BeautifulSoup


# html_page = 'https://www.tu-bryansk.ru/sveden/education/eduop/'

# g_url = urlopen(html_page)
# g_bs = BeautifulSoup(g_url.read(), 'html.parser')
# g_p_tag = [p_tag.get_text() for p_tag in g_bs.find_all('table', {"class" : 'table table-bordered table-condensed table-scroll-thead programs-description-table'})]
# print(g_p_tag)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

g_url = 'https://www.tu-bryansk.ru/sveden/education/eduop/'

html_page = urllib.request.urlopen(g_url)
soup = BeautifulSoup(html_page, 'html.parser')

g_list = []

for link in soup.find_all('a'):
    g_list.append(link.get('href'))
    print(link.get('href'))
    
df = pd.DataFrame(data=g_list)
df.to_excel('проверка таблицы_03.11.xlsx')


# for l in soup.select('tr td span'):
#     print(l.text)

# import pandas as pd
# import urllib.request

# html_page = urllib.request.urlopen('https://www.tu-bryansk.ru/sveden/education/eduop/')
# df = pd.read_html(html_page)

# print(df)
# df_1 = pd.concat(df)
# df_1.to_excel('fgh.xlsx')