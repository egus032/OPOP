import glob
import pandas as pd


start_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\Таблицы для рассылки\*\*'
finish_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\Таблицы обработанные\*\*'

g_path_start = glob.glob(start_folder)
g_path_finish = glob.glob(finish_folder)


g_list_1 = [f for f in g_path_start]
g_list_2 = [f_1 for f_1 in g_path_finish]

df_1 = pd.Series(g_list_1, name='Исходные папки')
df_2 = pd.Series(g_list_2, name='Входящие папки')

df_1.to_excel('Исходные папки.xlsx')
df_2.to_excel('Входящие папки.xlsx')