
import pandas as pd

g_file = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\УП для разбора\Бакалавр_заочная\15.03.01_МАШ_ИиРМ_4.6_2021_заочная.xls'

g_dataframe = pd.read_excel(g_file, sheet_name='Компетенции')

g_dataframe = g_dataframe.rename(columns= {'Unnamed: 1': 'Код компетенции', 'Unnamed: 2' : 'Код дисциплины'})

g_dataframe = g_dataframe.drop(labels='Индекс', axis=1)

print(g_dataframe)

# g_dataframe.to_excel('компетенции.xlsx')

g_discipline = g_dataframe.drop(labels='Код компетенции', axis=1).dropna().rename(columns={'Содержание' : 'Дисциплина, модуль'})

g_discipline.to_excel('дисциплины.xlsx')
g_competence = g_dataframe.drop(labels='Код дисциплины', axis=1).dropna().rename(columns={'Содержание' : 'Расшифровка компетенции'})

print(g_discipline, g_competence)

