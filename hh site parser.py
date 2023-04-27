import pandas as pd
import requests
import json
import os
import glob
from datetime import datetime

g_text = 'Бизнес аналитик'
g_data = datetime.today().strftime('%d.%m.%Y')

main_address = "https://api.hh.ru/vacancies"

def get_vacancies(page = 0):
    get_params = {
    'area': [ 1, 2019],
    'employment' : 'full',
    'label' : 'not_from_agency',
    'schedule' : 'fullDay',
    'search_field' : ['name', 'description'],
    'enable_snippets' : False,
    'text' : g_text,
    'ored_clusters' : True,
    'order_by' : 'publication_time',
    'search_period' : 30,
    'page' : page,
    "pages": 20, 
    'per_page' : 50
}
    req = requests.get(main_address, get_params)
    g_data = req.content.decode()
    req.close()
    return g_data

counter = 0

for page in range(0, 20):
    json_object = json.loads(get_vacancies(page))  
    nextFileName = 'D:\OPOP\pagination\hh{}.json'.format(len(os.listdir('D:\OPOP\pagination')))

    with open(nextFileName, 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(json_object, ensure_ascii=False))
        outfile.close()
    
    if (json_object['pages'] - page) <= 1:
            break 

g_path = r'D:\OPOP\pagination\*.json'

g_folder = glob.glob(g_path)

g_list = []

for file_name in g_folder:
    df_json = pd.read_json(file_name, encoding='utf-8')
    df_json_norm_1 = pd.json_normalize(df_json['items'])
    g_list.append(df_json_norm_1)

df_json_norm = pd.concat(g_list)

df_json_norm.to_excel(f'выгрузка с hh_{g_text}_{g_data}.xlsx')

# print(df_json_norm)
# print(df_json_norm)
# counter += 1
# print(json_object)
# print(counter, page, len(json_object))

# get_string = """https://hh.ru/search/vacancy?area=1&area=2019&employment=full&label=not_from_agency&schedule=fullDay&search_field=name&search_field=description&enable_snippets=false&text=Python&ored_clusters=true&search_period=30"""

# Для нахождения вашей вакансии использовал скрипт на Python, 
# с помощью которого выгрузил данные через 'https://api.hh.ru/vacancies', затем с помощью pandas превратил в таблицу Excel.

# import pandas as pd
# import requests
# import json
# import os
# import glob
# main_address = "https://api.hh.ru/vacancies"
# def get_vacancies(page = 0):
#     get_params = {
#     'area': [ 1, 2019],
#     'employment' : 'full',
#     'label' : 'not_from_agency',
#     'schedule' : 'fullDay',
#     'search_field' : ['name', 'description'],
#     'enable_snippets' : False,
#     'text' : 'Python',
#     'ored_clusters' : True,
#     'search_period' : 30,
#     'page' : page,
#     "pages": 20, 
#     'per_page' : 50
# }
#     req = requests.get(main_address, get_params)
#     g_data = req.content.decode()
#     req.close()
#     return g_data

# for page in range(0, 20):
#     json_object = json.loads(get_vacancies(page))  
#     nextFileName = 'D:\OPOP\pagination\hh{}.json'.format(len(os.listdir('D:\OPOP\pagination')))

#     with open(nextFileName, 'w', encoding='utf-8') as outfile:
#         outfile.write(json.dumps(json_object, ensure_ascii=False))
#         outfile.close()
    
#     if (json_object['pages'] - page) <= 1:
#             break 

# g_path = r'D:\OPOP\pagination\*.json'

# g_folder = glob.glob(g_path)

# g_list = []

# for file_name in g_folder:
#     df_json = pd.read_json(file_name, encoding='utf-8')
#     df_json_norm_1 = pd.json_normalize(df_json['items'])
#     g_list.append(df_json_norm_1)

# df_json_norm = pd.concat(g_list)

# df_json_norm.to_excel('выгрузка с hh.xlsx')