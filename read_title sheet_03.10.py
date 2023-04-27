# чтение файла Учебный план из папок и обработка листа Титул

import pandas as pd
import glob

g_folder = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\все УП от УМУ без ++_УП и .plx\*')

g_list_title = []
g_list_title_1 = []


for file in g_folder:
    df = pd.read_excel(file, sheet_name="Титул", header = 1).drop(labels=[1, 'Unnamed: 1'], axis=1)
    shifr = df.at[26, 'Unnamed: 3']
    spec = df.at[27, 'Unnamed: 3']
    kaf = df.at[34, 'Unnamed: 3']
    fakul = df.at[35, 'Unnamed: 3']
    kval = df.at[37, 'Unnamed: 2']
    form = df.at[39, 'Unnamed: 2']
    term = df.at[40, 'Unnamed: 2']
    year = df.at[37, 'Unnamed: 22']
    
    data_from_title = f'{shifr};{spec};{kaf};{fakul};{kval};{form};{term};{year};{file}'
    
    # print(data_from_title)
    
    # g_list_title.append(data_from_title)
        

    df['file'] = data_from_title
    # df_1 = df.drop(index=df.index[0:46])
    # print(df_1)
    g_list_title_1.append(df)
    

df_1 = pd.concat(g_list_title_1)
df_1.to_excel('проверка видов деят из 97 УП_1.xlsx')

# df_1 = pd.DataFrame(g_list_title)
# df_1 = df_1[0].str.split(';', expand=True)
# df_1.to_excel('Титулы_332 учебных плана.xlsx')
# print(df_1)