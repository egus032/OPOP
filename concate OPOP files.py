import pandas as pd
import glob

g_folder = glob.glob(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\из КС\*.xlsx")

g_list_columns = []

g_list_title = []

# Считаем столбцы в каждом файле
# for g_file in g_folder:
#     df = pd.read_excel(g_file, sheet_name='ВСЕ', header = [0])
#     num = len(df.columns)
#     g_list_columns.append(f'{g_file}: {num}')
  

# df_1 = pd.DataFrame(data=g_list_columns)
# df_1.to_excel('Столбцы.xlsx')
# print(df_1)

    
for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='Sheet1', header = [0])
    g_list_title.append(df)
    df_1 = pd.concat(g_list_title)
    print(g_file)
    print(df_1)

df_1.to_excel('ВСЕ КС таблицы_11.04.22.xlsx')

