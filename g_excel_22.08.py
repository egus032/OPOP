import pandas as pd
 
df = pd.read_excel(r"C:\Users\User\Desktop\15.03.01_МАШ_ОиТСП_4.6_2018_заочная.xls", sheet_name="План", header=[1,2])
 
df.columns = df.columns.map("; ".join)
# df.columns = [f'{i}{j}' for i, j in df.columns]
 
print(df.head(10))
 
# df.to_excel("concat plans.xlsx")