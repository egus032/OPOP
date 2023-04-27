
# Создание сводного файла для проверки наличия колонок по факультетам

import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\УП для разбора\Бакалавр_заочная\*.xls")

g_list_kaf = []
g_dict = {}

for file in g_folder:
    df = pd.read_excel(file, sheet_name="План", header = [0,1,2])
    # df["From file data"] = file.split("\\")[-1]
    df = df[:0]
    for item in df:
        g_list_kaf.append(f"{file} : {item}")
    df_1 = pd.DataFrame(g_list_kaf)
df_1.to_excel("ФОЦЭ.xlsx") 
    
    