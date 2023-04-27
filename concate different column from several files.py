import pandas as pd
import glob
import re

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Планы_ПРО Хохлова М.В._07.11.22'
 
g_folder = glob.glob(g_path + '\*.xlsx')

g_list = []

drop_columns = ['Экспер тное', 'Факт', 'Часов в з.е.', 'Экспер тное.1', 'По плану', 'Компетенции']

g_pattern = r'з.е.*|Итого.*'

for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='План', header=2).drop(columns=drop_columns, axis=1).rename(columns={'Наименование.1':'Название_кафедры'})
    df = df.drop(columns=[col for col in df.columns if re.match(pattern=g_pattern, string=col)])
    df['Имя_файла'] = g_file.replace(g_path+'\\', '').replace('.xlsx', '')
    
    
    
    g_list.append(df)

    df_1 = pd.concat(g_list)

# df_1.to_excel('Хохлова.xlsx')

# df_1['Экза мен'] = df_1['Экза мен'].map(str)
# print(df_1.info())
col_names = ['Экза мен', 'Зачет',
       'Зачет с оц.', 'КП', 'КР', 'Контр.', 'Рефе рат', 'РГР', 'Конт. раб.',
       'СР', 'Конт роль', 'Лек', 'Лаб', 'Пр', 'СР.1', 'Конт роль.1', 'Лек.1',
       'Лаб.1', 'Пр.1', 'СР.2', 'Конт роль.2', 'Лек.2', 'Лаб.2', 'Пр.2',
       'СР.3', 'Конт роль.3', 'Лек.3', 'Лаб.3', 'Пр.3', 'СР.4', 'Конт роль.4',
       'Лек.4', 'Лаб.4', 'Пр.4', 'СР.5', 'Конт роль.5', 'Лек.5', 'Лаб.5',
       'Пр.5', 'СР.6', 'Конт роль.6', 'Лек.6', 'Лаб.6', 'Пр.6', 'СР.7',
       'Конт роль.7', 'Лек.7', 'Лаб.7', 'Пр.7', 'СР.8', 'Конт роль.8', 'Лек.8',
       'Лаб.8', 'Пр.8', 'СР.9', 'Конт роль.9', 'Лек.9', 'Лаб.9', 'Пр.9',
       'СР.10', 'Конт роль.10'
       ]
df_1[col_names] = df_1[col_names].fillna(0).applymap(int)
print(df_1['Экза мен'])
# print(df_1.info())
# df_1.to_excel('Хохлова_14.11.22.xlsx')
