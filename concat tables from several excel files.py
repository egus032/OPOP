import pandas as pd
import glob
import os

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\Учебные планы от 05.04.23\*'

g_folder = glob.glob(g_path)

g_list = []

counter = 0

for g_file in g_folder:
    # if g_file.find('.xlsx') != -1:
    #     try:
    df = pd.read_excel(g_file, sheet_name='План', header=[2])
    short_name = g_file.replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\Учебные планы от 05.04.23' + '\\', '').replace('.plx', '').replace('.xlsx', '')
    # df.columns = df.columns.map('_'.join)
    df['Имя_файла'] = short_name
    print(df)
    
    g_list.append(df)
    counter += 1
    print(counter, g_file)
        # except:
        #     print('Проверить расширение файла:', g_file)

df_1 = pd.concat(g_list, axis=0, ignore_index=True)  
df_1.to_excel('17.04.2023_4_97 учебных планов_дисциплины_кафедры.xlsx')