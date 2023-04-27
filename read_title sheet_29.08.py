
# чтение файла Учебный план из папок и обработка листа Титул

import pandas as pd
import glob

g_folder = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список\действующие_2022_2023_exel_список\*.xlsx')

g_list_title = []

for file in g_folder:
    df = pd.read_excel(file, sheet_name="Титул", header = 1) #.drop(labels=[1, 'Unnamed: 1'], axis=1)
    shifr = df.at[26, 'Unnamed: 3']
    spec = df.at[27, 'Unnamed: 3']
    kaf = df.at[34, 'Unnamed: 3']
    fakul = df.at[35, 'Unnamed: 3']
    kval = df.at[37, 'Unnamed: 2']
    form = df.at[39, 'Unnamed: 2']
    term = df.at[40, 'Unnamed: 2']
    year = df.at[37, 'Unnamed: 22']
    # data_from_title = '; '.join([shifr, spec, kaf, fakul, kval, form, term, year, file])
    data_from_title = f'{shifr};{spec};{kaf};{fakul};{kval};{form};{term};{year};{file}'
    # print(file)
    print(data_from_title)
    # break
    g_list_title.append(data_from_title)
        
df_1 = pd.DataFrame(g_list_title)
df_1 = df_1[0].str.split(';', expand=True)
df_1.to_excel('Титулы_346 УП_15.12.2022.xlsx')
print(df_1)




        

        
        


