import pandas as pd
import glob

g_all_files = glob.glob("D:/Matrix competition/*.xlsx")
g_data_frame = pd.concat((pd.read_excel(file_name) for file_name in g_all_files))
g_file_excel = g_data_frame.to_excel("all_matrix.xlsx")

g_data_frame_copy = pd.read_excel("C:/Users/User/all_matrix.xlsx")

#список строк для удаления
g_list = [  " ",
            "Блок 1. Дисциплины (модули)", 
            "Базовая часть", 
            "Вариативная часть", 
            "Дисциплины (модули) по выбору 1 (ДВ.1)", 
            "Дисциплины (модули) по выбору 2 (ДВ.2)", 
            "Дисциплины (модули) по выбору 3(ДВ.3)", 
            "Дисциплины (модули) по выбору 4 (ДВ.4)",
            "Дисциплины (модули) по выбору 5 (ДВ.5)", 
            "Дисциплины (модули) по выбору 6 (ДВ.6)", 
            "Дисциплины (модули) по выбору 7 (ДВ.7)",
            "Элективные дисциплины по физической культуре и спорту", 
            "Блок 2. Практики",
            "Блок 3. Государственная итоговая аттестация", 
            "ФТД. Факультативы", 
            ]

#удаляем из таблицы строки согласно списку
for list_item in g_list:
    g_data_frame_copy = g_data_frame_copy[g_data_frame_copy["МАТРИЦА КОМПЕТЕНЦИЙ"] != list_item ]
    g_data_frame_copy.to_excel("all_matrix_without_trash.xlsx")
    print(g_data_frame_copy)






