import pandas as pd
import glob
import openpyxl

g_folder = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\Таблицы обработанные\*\*')

g_list = []

for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='Таблица_для кадровой_справки')
    # print(f'{g_file}: {len(df.columns)}')
    g_list.append(f'{g_file}: {df.columns}')

df_1 = pd.DataFrame(data=g_list)
df_1.to_excel('перечень столбцов_таблицы для КС.xlsx')
print(df_1)
#     for i in df.columns.values:
#         copy_g_file = g_file.replace('C:\\Users\\User\\Downloads\\Таблицы для ОПОП\\', '')
#         # print(f'{copy_g_file}: {i}')
#         g_list.append(f'{copy_g_file}: {i}')
#     print(g_list)
# 
# print(df_1)

