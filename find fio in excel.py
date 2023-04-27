
import re
import pandas as pd

txt = 'Научныйруководитель:ст.преподавателькафедры«Трубопроводныетранспортныесистемы»,С.А.Олисов.'

txt_1 = 'Научныйруководитель:старшийпреподавателькафедры«Физическоевоспитаниеиспорт»БойкоГ.М.'

s_1 = "([А-Я]\.[А-Я]\.[А-Я][а-я]+)"

s_2 = "([А-Я][а-я]+[А-Я]\.[А-Я]\.)"

# substring = re.findall(s_1, txt)

# print(substring)

excel_file = r'D:\OPOP\Научные рук 77 конф_1.xlsx'

df = pd.read_excel(excel_file)
g_list = []

# for cell in df.itertuples():
#     sub_1 = re.findall(s_1, cell.Data)
#     for x in sub_1:
#         g_list.append(x)

# df_1 = pd.DataFrame(g_list)
# df_1.to_excel("И.О.Фамилия.xlsx")

for cell in df.itertuples():
    sub_2 = re.findall(s_2, cell.Data)
    for x in sub_2:
        g_list.append(x)

df_2 = pd.DataFrame(g_list)
df_2.to_excel("ФамилияИ.О.xlsx")