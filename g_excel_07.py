import pandas as pd
import glob

g_path = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\ФОЦЭ_09.08\2022\2022_ФОЦЭ_2_очная"

g_filenames = glob.glob(g_path + "\*.xls")
 
g_df_for_plans = pd.DataFrame()
g_list_for_plans = []

for g_sheet in g_filenames:
    g_data_frame_titles = pd.read_excel(g_sheet, sheet_name="Титул")
    g_data_frame_titles = g_data_frame_titles.drop(labels=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13", "Unnamed: 14", "Unnamed: 15",
    "Unnamed: 16", "Unnamed: 17", "Unnamed: 18", "Unnamed: 20", "Unnamed: 21", "Unnamed: 22", "Unnamed: 23", "Unnamed: 24", "Unnamed: 25", "Unnamed: 26"], axis=1)
    g_data_frame_titles = g_data_frame_titles.rename(columns= {"Unnamed: 0" : "Столбец1", "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ" :  "Столбец2", "Unnamed: 19" : "Столбец3"})
  
    g_shifr = g_data_frame_titles.at[16, "Столбец2"]
    g_profile = g_data_frame_titles.at[17, "Столбец2"]
    g_kafedra = g_data_frame_titles.at[24, "Столбец2"]
    g_fakultet = g_data_frame_titles.at[25, "Столбец2"]
    g_kvalif = g_data_frame_titles.at[27, "Столбец1"]
    g_year = g_data_frame_titles.at[27, "Столбец3"]
    g_form = g_data_frame_titles.at[29, "Столбец1"]
    g_term = g_data_frame_titles.at[30, "Столбец1"]
    
    g_data = f"{g_shifr}; {g_profile}; {g_kafedra}; {g_fakultet}; {g_kvalif}; {g_form}; {g_term}; {g_year}"

    print(g_data)
    
    g_data_frame_plans = pd.read_excel(g_sheet, sheet_name="План", header=[0, 1, 2]).assign(My_Info = g_data)

    g_list_for_plans.append(g_data_frame_plans)

    g_df_for_plans = pd.concat(g_list_for_plans)

    g_df_for_plans.to_excel("21.xlsx") 
    
    