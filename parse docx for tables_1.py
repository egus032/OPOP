import docx
import glob
import os
import pandas as pd

g_fold = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О'

g_path = glob.glob(g_fold + '\\*.*')

g_list = []

g_dict = {}

keys = None

counter = 0

df_tables = []

for g_file in g_path:
    g_file_short = g_file.replace(g_fold + '\\', '')
    if g_file_short.find('~$') == -1:
        g_doc = docx.Document(g_file)
        g_table = g_doc.tables
        for t, table in enumerate(g_table):
            if t == 2:
                print(t, table.columns, table.rows)
                df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
                for r, row in enumerate(table.rows):
                    for c, cell in enumerate(row.cells):
                        if cell.text:
                            df[r][c] = cell.text
                    df_tables = pd.DataFrame(df)
                    df_tables['Имя_файла'] = g_file_short       
                g_list.append(df_tables)
                df_2 = pd.concat(g_list)
                print(g_file_short, df_2)
                # df_2.to_excel('Обработка РПД_02.03.23_0.xlsx')
                
        

# Варианты кода                    
                    # for first_row, second_row in zip(table.row_cells(0), table.row_cells(1)):
                    #     g_list.append({first_row.text, second_row.text})
                    # print(g_list)
                    # for second_row in table.row_cells(1):
                    #     g_list.append(second_row.text)
                    #     print(g_list)

                        

            # break
                    # df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
                    # for r, row in enumerate(table.rows):
                    #     for c, cell in enumerate(row.cells):
                    #         if cell.text:
                    #             df[r][c] = cell.text
                    #         df_tables.append(pd.DataFrame(df))
                    #     print(df_tables)
                    #     break