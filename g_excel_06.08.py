import pandas as pd
import glob

g_path = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\ФОЦЭ_09.08\2022\2022_ФОЦЭ_4_очная"

g_filenames = glob.glob(g_path + "\*.xlsx")

g_list = []

for g_title_sheet in g_filenames:
    g_data_frame = pd.read_excel(g_title_sheet, sheet_name="Титул", header=1)
    g_data_frame = g_data_frame.drop(labels=1, axis=1)
    g_data_frame = g_data_frame.rename(columns= {
        "Unnamed: 1" : "Столбец1",
        "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ" : "Столбец2",
        "Unnamed: 3" : "Столбец3",
        "Unnamed: 4" : "Столбец4",
        "Unnamed: 20" : "Столбец20"
    })

    g_shifr = g_data_frame.at[16, "Столбец2"]
    g_profile = g_data_frame.at[17, "Столбец2"]
    g_cafedra = g_data_frame.at[24, "Столбец2"]
    g_facultet = g_data_frame.at[25, "Столбец2"]
    g_cvalification = g_data_frame.at[27, "Столбец1"]
    g_form = g_data_frame.at[29, "Столбец1"]
    g_term = g_data_frame.at[30, "Столбец1"]

    g_data = g_shifr + "; " + g_profile + "; " + g_cafedra + "; " + g_facultet + "; " + g_cvalification + "; " + g_form + "; " + g_term
    g_list.append(g_data)
    

g_data_frame_info = pd.DataFrame(g_list, columns=["Инфо"])
print(g_data_frame_info)
g_data_frame_info.to_excel("15.xlsx")
    