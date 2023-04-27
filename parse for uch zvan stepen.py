from bs4 import BeautifulSoup as bs
import urllib.request as url
import pandas as pd
from urllib.request import urlopen
import numpy as np
 
g_html_main_address = 'https://www.tu-bryansk.ru/sveden/employees/'
 
finish_num = 15

# finish_num = 8100
 
g_list = []
g_list_1 = []
g_list_2 = []

counter = 0 

# создаем список рабочих ссылок для парсинга таблицы
def parse_html_string(g_html_main_address, finish_num):
    for i in range(1, finish_num):
        url = g_html_main_address + str(i)
        try:
            urlopen(url)
            print(url)
            g_list.append(url)
        except:
            print(url, ' - ошибка на странице!!!')
    return g_list

for g_link in parse_html_string(g_html_main_address, finish_num):
    html_page = url.urlopen(g_link)
    soup = bs(html_page, 'html.parser')
    fio = soup.find('h1').text
    table = soup.find_all('span', class_ = 'val')
    
    if fio != '' and table != []:
        try:
            table.insert(0, fio)
            g_list_1.append(table)
            counter += 1
            print(counter)
        except:
            print('Ошибка на странице:', g_link)
    # print(g_list_1)

df = pd.DataFrame(g_list_1)
print(df)
df.to_excel('Ученое звание и степень с сайта.xlsx')
        
        # try:
        #     # можно через dict
        #     # g_dict[fio] = table
        #     # g_dict.update
        #     df = pd.read_html(table)
        #     # df['ФИО'] = fio
        #     print(df)
        #     # g_list_1.append(df)
                        
        # except:
        #     counter += 1
        #     print('Ошибка на странице:', counter, g_link)



# values = np.array([v for v in g_list_1])
# for v in values:
#     g_list_2.append(v)
#     df_1 = pd.concat(g_list_2)

# print(df_1)
# df_1.to_excel('Ученое звание и степень с сайта.xlsx')