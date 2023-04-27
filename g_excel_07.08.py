import pandas as pd
import glob

g_path = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\ФОЦЭ_09.08\2022\2022_ФОЦЭ_4_очная"

g_filenames = glob.glob(g_path + "\*.xls")

finalexcelsheet = pd.DataFrame()

df = pd.concat(pd.read_excel(file, sheet_name="Титул") for file in g_filenames)

print(df)
df.to_excel("10.08.xlsx")