
# чтение файла Учебный план из папок и обработка листа План, добавление пути и имени файла

import pandas as pd
import glob

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список (1)\действующие_2022_2023_exel_список'

full_g_path = g_path + '\\*.xlsx'

g_folder = glob.glob(full_g_path)

g_list_title = []

for file in g_folder:
    df = pd.read_excel(file, sheet_name="План", header = [2])
    g_profile = file.replace(g_path, '').replace('.xlsx', '').replace('\УП_', '')
    df['УП_Имя файла'] = g_profile
    df['РПД_Имя_файла'] = f'РПД_{g_profile}_' + df['Индекс']
    # df = df.iloc[:, list([0,2]) + [-3, -2, -1]]
    
    g_list_title.append(df)
    
    
    df_1 = pd.concat(g_list_title)

    print(df_1)
    
df_1.to_excel('346 учебных планов 14.11.22_1.xlsx')

print(df_1.columns)
    
    