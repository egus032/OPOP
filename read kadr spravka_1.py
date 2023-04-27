import glob
import pandas as pd

g_folder = glob.glob(r"C:\Users\User\Desktop\Кадровая справка\*.xlsx")

g_list = []

for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='Лист1')
    # print(df.columns)
    
    g_list.append(df)

df_1 = pd.concat(g_list, ignore_index=True)
print(df_1)

df_1.to_excel('Справка кадровая_26.09.22_13_50.xlsx')