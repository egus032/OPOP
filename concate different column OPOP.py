import pandas as pd
import glob
 
g_folder = glob.glob(r'C:\Users\User\Downloads\Таблицы для ОПОП\БОЛЬШЕ СТОЛБЦОВ\*.xlsx')

 
g_list = []
 
for g_file in g_folder:
    df = pd.read_excel(g_file, sheet_name='ВСЕ', header=[0])
    # df['FileName'] = g_file
    
    g_list.append(df)

    # print(g_list)
 
    df_1 = pd.concat(g_list, axis=0, ignore_index=True)
    print(g_file)
    print(df_1)
    
# df_1 = df_1.reindex(sorted(df_1.columns), axis=1)

df_1.to_excel('Сборка 8 ОПОП_разные столбцы_1.xlsx')