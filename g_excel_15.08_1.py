
# Обработка для возврата из каждого учебного плана определенных столбцов сначала и с конца

import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Учебные планы\*\*\*\*\*.xls")

g_list_kaf = []

for file in g_folder:
    df = pd.read_excel(file, sheet_name="План", header = [2])
    df = df[['Считать в плане', 'Индекс', 'Наименование', 'Код', 'Наименование.1', 'Компетенции']]
    df["Из файла"] = file.split(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Учебные планы")[-1]
    g_list_kaf.append(df)
    print(g_list_kaf)
    df = pd.concat(g_list_kaf)


df.to_excel("Общий_Дисциплина_кафедра_компетенция.xlsx")