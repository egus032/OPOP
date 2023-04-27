import pandas as pd

g_file = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\346 учебных планов 14.xlsx'


df = pd.read_excel(g_file, sheet_name='Sheet5', header = 0)



for col in df.columns:
    
    print(col)
