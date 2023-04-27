import pandas as pd
import glob

g_folder = glob.glob(r'D:\OPOP\ЛА_20.10.22_109-110\*')

# g_folder_1 = glob.glob(r'C:\Users\User\Downloads\БГТУ_exel\БГТУ_exel\*\*\*\*\*')

# C:\Users\User\Downloads\БГТУ_exel\БГТУ_exel\МТФ_exel\МиМ_exel\2018\заочная

file_name = r'БГТУ_exel'

list_file = []

for g_file in g_folder:
    list_file.append(g_file)
    # list_file.append(g_file.replace(f'{file_name}\\', ''))
    
df = pd.Series(list_file)
print(df)
df.to_excel('список файлов_ЛА_20.10.22.xlsx')

    