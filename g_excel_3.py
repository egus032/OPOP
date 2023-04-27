from openpyxl import load_workbook
import pandas as pd
import glob

g_list = [  " ",
            "Блок 1. Дисциплины (модули)", 
            "Базовая часть", 
            "Вариативная часть", 
            "Дисциплины (модули) по выбору 1 (ДВ.1)", 
            "Дисциплины (модули) по выбору 2 (ДВ.2)", 
            "Дисциплины (модули) по выбору 3(ДВ.3)", 
            "Дисциплины (модули) по выбору 3 (ДВ.3)",
            "Дисциплины (модули) по выбору 4 (ДВ.4)",
            "Дисциплины (модули) по выбору 5 (ДВ.5)", 
            "Дисциплины (модули) по выбору 6 (ДВ.6)", 
            "Дисциплины (модули) по выбору 7 (ДВ.7)",
            "Дисциплины (модули) по выбору 8 (ДВ.8)",
            "Дисциплины (модули) по выбору 9 (ДВ.9)",
            "Элективные дисциплины по физической культуре и спорту", 
            "Блок 2. Практики",
            "Блок 3. Государственная итоговая аттестация", 
            "ФТД. Факультативы", 
            ]

g_all_files = glob.glob("D:/Matrix competition/*.xlsx")

for file_name in g_all_files:
    g_data_frame = pd.concat((pd.read_excel(file_name) for file_name in g_all_files))
    for list_item in g_list:
        g_data_frame = g_data_frame[g_data_frame["МАТРИЦА КОМПЕТЕНЦИЙ"] != list_item ]
        g_file_excel = g_data_frame.to_excel("all_matrix_1.xlsx")
        
