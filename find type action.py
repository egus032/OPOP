import glob
import pandas as pd

df = pd.read_excel(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\ОПОП таблица_304 столбца_05.10.22_269_штук\ОПОП таблица_304 столбца_07.10.22_265_штук.xlsx', sheet_name='ВСЕ_ОПОП', header=0)
# print(df.columns.values)
df_1 = df[['Код_и_название_направления_подготовки_специальности', 'Профиль_подготовки_специализация',
     'Уровень_ВО_', 'Форма_обучения', 'Кафедра_кратк', 'Фак_Инст', 'Типы_задач_проф_деят__Виды_проф_деят']]
print(df_1)

df_1.to_excel('типы задач и виды деятельности для УП.xlsx')