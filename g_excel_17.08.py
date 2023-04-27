
# выводим список всех файлов в папке

import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Учебные планы\*\*\*\*\*.xlsx")

g_folder_1 = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\*\*.xlsx")

g_folder_2 = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\2019-2020-2021-2022_07.09.22\*.xlsx")

g_list_kaf = []
g_list_kaf_1 = []

# for file in g_folder:
#     g_list_kaf.append(file)

# df_1 = pd.DataFrame(g_list_kaf)
# df_1.to_excel("Перечень учебных планов.xlsx")
# print(df_1)

for file_1 in g_folder_2:
    g_list_kaf_1.append(file_1)

df_2 = pd.DataFrame(g_list_kaf_1)
df_2.to_excel("Перечень учебных планов_08.09.xlsx")
print(df_2)

    

