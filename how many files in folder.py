import glob
import pandas as pd

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ\*'

change = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ\\'

g_folder = glob.glob(g_path + '\\*.*')

g_list = []

for g_file in g_folder:
    g_list.append(g_file)

df = pd.DataFrame(data=g_list)
print(df)
df.to_excel('список файлов_РПД_27.02.23.xlsx')
