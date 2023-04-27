import glob
import pandas as pd

g_folder = glob.glob(r'C:\Users\User\Desktop\УП_10.10.2022\*.xlsx')

g_list = []

counter = 0

for g_file in g_folder:
    df_1 = pd.read_excel(g_file, sheet_name='Компетенции', header=0).drop(labels=['Индекс', 'Unnamed: 2', 'Тип'], axis=1)
    
    df = pd.read_excel(g_file, sheet_name='Титул', header=1).drop(labels=[1, 'Unnamed: 1'], axis=1)
    shifr = df.at[26, 'Unnamed: 3']
    spec = df.at[27, 'Unnamed: 3']
    kaf = df.at[34, 'Unnamed: 3']
    fakul = df.at[35, 'Unnamed: 3']
    kval = df.at[37, 'Unnamed: 2']
    form = df.at[39, 'Unnamed: 2']
    term = df.at[40, 'Unnamed: 2']
    year = df.at[37, 'Unnamed: 22']
    
    data_from_title = f'{shifr};{spec};{kaf};{fakul};{kval};{form};{term};{year};{g_file}'
    df_1['file'] = data_from_title

    g_list.append(df_1)
    
    print(g_file)
    print(df_1)
    
df_2 = pd.concat(g_list)
# df_2 = df_2['file'].str.split(';', expand=True)
df_2.to_excel('каталог компетенций по УП.xlsx')