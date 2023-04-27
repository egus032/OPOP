import glob
import pandas as pd


g_path = "D:/All_plans"

g_all_files = glob.glob("D:/All_plans/*.xlsx")

for file_name in g_all_files:
    g_data_frame = pd.read_excel(file_name, sheet_name = "Титул")
    df = g_data_frame.drop(g_data_frame.iloc[:, 3:], axis=1)
    df_1 = df.drop(["Unnamed: 0"], axis=1)
    
    print(df_1)
    
    break
    
g_list = [["Шифр", "Профиль", "Кафедра", "Факультет", "Квалификация", "Форма обучения", "Срок обучения"]]
g_df_2 = pd.DataFrame(g_list)
print(g_df_2)
