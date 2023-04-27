from bs4 import BeautifulSoup as bs
import urllib.request as url
import pandas as pd
from urllib.request import urlopen
import numpy as np
 
g_html_main_address = 'https://www.tu-bryansk.ru/sveden/employees/'
 
finish_num = 8100
 
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
            pass
    return g_list

for g_link in parse_html_string(g_html_main_address, finish_num):
    html_page = url.urlopen(g_link)
    soup = bs(html_page, 'html.parser')
    fio = soup.find('h1').text
    table = str(soup.find_all('table'))
    if fio != '' and table != []:
        try:
            # можно через dict
            # g_dict[fio] = table
            # g_dict.update
            df = pd.concat(pd.read_html(table))
            df['ФИО'] = fio
            g_list_1.append(df)
            
        except:
            counter += 1
            print('Ошибка на странице:', counter, g_link)

values = np.array([v for v in g_list_1])
for v in values:
    g_list_2.append(v)
    df_1 = pd.concat(g_list_2)

print(df_1)
df_1.to_excel('Повышение квалификации с сайта.xlsx')

# df_from_numpy = pd.DataFrame(values, columns = ['Индекс','Год','Информация','ФИО'], index = ['Item_1', 'Item_2'])
# print(df_from_numpy)
# df = pd.DataFrame.from_dict(g_dict, orient='index')
# print(df)

# df_2 = pd.concat(g_list_1, axis=0, ignore_index=True)
# print(df_1)
 
    
 
# g_list = []
# for g_link in range(1, finish_num):
#     g_string = f'{g_html_main_address}{g_link}'
#     html_page = url.urlopen(g_string)
#     # if html_page == 'https://www.tu-bryansk.ru/404.php':
#     print(html_page)
    # soup = bs(html_page, 'html.parser')
    # if 
    # fio = soup.find('h1').text
    
    # table = soup.find_all('table')
    # print(fio, table)
    # df = pd.read_html(table)
    # df_1 = pd.DataFrame(df[0])
    # df_1['ФИО'] = fio
    # print(df_1)
    # g_list.append(df_1)
    # break
    
# df_2 = pd.concat(g_list, axis=0, ignore_index=True)
# print(df_1)
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd
 
# g_url = "https://www.tu-bryansk.ru/sveden/employees/476"
 
# soup = BeautifulSoup(urlopen(g_url), "html.parser")

# # table_1 = soup.find_all('span', {'tr' :'td'})

# fio = soup.find('h1', {'class' : 'userpage-title'})

# # # print(f'{table_1}\n')
# # print(fio)

# # for t in table_1:
# #     print(t)

# g_list = []
# for cval in soup.find_all('td'):
#     # print(cval)
#     # title = cval.text
#     # print(title)
#     g_list.append([fio, cval.text])
#     print(g_list)

# df = pd.DataFrame(g_list)
# print(df)


 
# for tab in table_1:
#     tab_array = []
#     for cell in tab.find_all(["td"]):
#         tab_array.append(cell.get_text().replace("\n","").strip())
#         print(tab_array)
        