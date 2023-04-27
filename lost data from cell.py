import glob
import pandas as pd


g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список\тест по содержанию ячеек\*.xlsx'

g_folder = glob.glob(g_path)

g_list = []

for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='3+_бакалавр', header=0)
    g_list.append(df)
    # print(g_file)
    # col = df.columns.tolist()
    # for _, i in df.iterrows():
    #     for c in col:
    #         print(len(str(i[c])),' ', i[c])
    #         print(g_file)
    #         print("############")
    #     break
    # for col in df.columns:
    #     df_count = len(col)
    #     print(col, df_count)

df_list = pd.concat(g_list)
col = df_list.columns.tolist()
for _, i in df.iterrows():
    for c in col:
        print(len(str(i[c])), g_file)
        
        
# df_list.to_excel('тест_1.xlsx')

