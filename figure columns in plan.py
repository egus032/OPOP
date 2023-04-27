
# посчитать и проверить первые 24 колонки листа План на соответствие

import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\01.09.22\*\*.xlsx")

g_list_title = []
g_list_title_1 = []

for file in g_folder:
    df = pd.read_excel(file, sheet_name="План", header = [2])
    
    df['Файл'] = file
    df = df.iloc[:, list(range(0, 8+1)) + [-1]]
    # print(df.columns)           
    g_list_title.append(df)
        
    df_1 = pd.set_option('display.max_colwidth', 150)
    df_1 = pd.concat(g_list_title)
    #  df_1 = df_1.iloc[:, -1]
    # str_1 = str(f'{file}, {df_1.columns}')
    # g_list_title_1.append(str_1)
    print(df_1)
    
    # print(df_1.iloc[:, -1])
    # break
# df_2 = pd.DataFrame(g_list_title_1)            
    
df_1.to_excel('Проверка_2020 года по столбцам.xlsx')