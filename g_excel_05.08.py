import pandas as pd
import glob
import os

g_path = r"E:\МТФ_актуально_с_сайта\2022_МТФ\2022_Бакалавр очная"

g_filenames = glob.glob(g_path + "\*.xlsx")

finalexcelsheet = pd.DataFrame()

df = pd.concat(pd.read_excel(file, sheet_name="План", header=[0, 1, 2]) for file in g_filenames)

print(df)

# for file in g_filenames:
#     g_column = pd.read_excel(file, nrows = 1).columns
#     df = pd.concat(pd.read_excel(file, sheet_name="План", header=[0, 1, 2]) for file in g_filenames)
#     df.to_excel("13.xlsx")
    # finalexcelsheet = finalexcelsheet.append(df, ignore_index=True)
    # finalexcelsheet.to_excel("10.xlsx")
    # print(finalexcelsheet)

