import pandas as pd
import glob
 
g_folder = glob.glob(r'D:\OPOP\Новая папка\*.docx')

g_list = []

g_dict = {}
 
for g_file in g_folder:
    df_1 = pd.read_excel(g_file, sheet_name='Sheet1')
    # df_2 = pd.DataFrame(data=df_1.columns.values, columns=[f'{g_file}'])
    # g_list.append(g_file)
    g_dict[g_file] = df_1.columns.values
    g_dict.update()
    # print(g_dict)
    
    
df = pd.DataFrame.from_dict(g_dict, orient='index')
print(df)
df.to_excel('столбцы сравнение ОПОП_107 штук.xlsx')