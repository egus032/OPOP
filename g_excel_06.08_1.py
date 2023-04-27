import pandas as pd
import glob

g_path = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\УП для разбора\Бакалавр_заочная"

g_filenames = glob.glob(g_path + "\*.xls")
 
#обработка листов из папки 
def return_data_from_titles(g_filenames):
    g_df_for_plans = pd.DataFrame()
    g_list_for_plans = []
    for g_sheet in g_filenames:
        g_data_frame_titles = pd.read_excel(g_sheet, sheet_name="Титул", header=1)
        g_data_frame_titles = g_data_frame_titles.drop(labels=1, axis=1)
        g_data_frame_titles = g_data_frame_titles.rename(columns= {
            "Unnamed: 1" : "Столбец1",
            "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ" : "Столбец2",
            "Unnamed: 3" : "Столбец3",
            "Unnamed: 4" : "Столбец4",
            "Unnamed: 20" : "Столбец20"
        })
        g_shifr = g_data_frame_titles.at[16, "Столбец2"]
        g_profile = g_data_frame_titles.at[17, "Столбец2"]
        g_cafedra = g_data_frame_titles.at[24, "Столбец2"]
        g_facultet = g_data_frame_titles.at[25, "Столбец2"]
        g_cvalification = g_data_frame_titles.at[27, "Столбец1"]
        g_form = g_data_frame_titles.at[29, "Столбец1"]
        g_term = g_data_frame_titles.at[30, "Столбец1"]

        g_data = g_shifr + "; " + g_profile + "; " + g_cafedra + "; " + g_facultet + "; " + g_cvalification + "; " + g_form + "; " + g_term

        g_data_frame_plans = pd.read_excel(g_sheet, sheet_name="План", header=[0, 1, 2]).assign(My_Info = g_data)
        
        g_list_for_plans.append(g_data_frame_plans)
                
        # print(g_list_for_plans)
        g_df_for_plans = pd.concat(g_list_for_plans)

        g_df_for_plans.columns = g_df_for_plans.columns.map("; ".join)

        print(g_df_for_plans.columns)
        
        g_df_for_plans.to_excel("МТФ_бакалавр_заочная.xlsx")
        
             
return_data_from_titles(g_filenames)