# создание таблицы из Плана для РПД

import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список\действующие_2022_2023_exel_список\*.xlsx")

g_list = []

for g_file in g_folder:
    df_title = pd.read_excel(g_file, sheet_name="Титул", header = 1).drop(labels=[1, 'Unnamed: 1'], axis=1)
    shifr = df_title.at[26, 'Unnamed: 3']
    spec = df_title.at[27, 'Unnamed: 3']
    kaf = df_title.at[34, 'Unnamed: 3']
    fakul = df_title.at[35, 'Unnamed: 3']
    kval = df_title.at[37, 'Unnamed: 2']
    form = df_title.at[39, 'Unnamed: 2']
    term = df_title.at[40, 'Unnamed: 2']
    year = df_title.at[37, 'Unnamed: 22']
    
    data_from_title = '; '.join([shifr, spec, kaf, fakul, kval, form, term, year, g_file])
    
    print(data_from_title)
   
    
    df_plan = pd.read_excel(g_file, sheet_name="План", header = [2]).assign(My_Info = data_from_title)
#     # df.columns = df.columns.map(';'.join)
#     # print(df.columns)
    g_list.append(df_plan)
    
    df_1 = pd.concat(g_list, axis=0, ignore_index=True)
    print(df_1)

df_1.to_excel("Столбцы План_15.12.xlsx")
