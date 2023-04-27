import pandas as pd
import glob

g_all_files = glob.glob(r"D:\МТФ_актуально_с_сайта\2022_МТФ\*.xlsx")
g_data_frame = pd.concat((pd.read_excel(file_name, sheet_name = "ПланСвод") for file_name in g_all_files))
#df1 = pd.read_excel(r"D:\МТФ_актуально_с_сайта\2018_МТФ\++15.03.01_МАШ_ОиТСП_УП(plx)_4.6_2~.xlsx", sheet_name= "ПланСвод")
#df2 = pd.read_excel(r"D:\МТФ_актуально_с_сайта\2018_МТФ\++15.03.01_МАШ_ПТЛ_УП(plx)_4.6_201~.xlsx", sheet_name= "ПланСвод")

# g_file_excel = df1.to_excel("2018_plans_1.xlsx", sheet_name="Вторая попытка")
# g_file_excel = df2.to_excel("2018_plans_2.xlsx", sheet_name="Вторая попытка")


#g_data_frame = pd.concat([df1, df2])

# print(g_data_frame)

# g_file_excel = g_data_frame.to_excel("2018_plans.xlsx")
g_file_excel = g_data_frame.to_excel("2018 plans 3.xlsx")
# print(g_file_excel)