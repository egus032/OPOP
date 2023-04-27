from docx import Document
import pandas as pd
import glob

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О\*'

g_glob = glob.glob(g_path)

tables = []

error_list = []

for g_file in g_glob:
    g_file_short = g_file.replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О' + '\\', '')
    document = Document(g_file)
    for table in document.tables:
        df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
        for i, row in enumerate(table.rows):
            try:
                for j, cell in enumerate(row.cells):
                    if cell.text:
                        df[i][j] = cell.text
            except IndexError as e:
                error_list.append(f'{e, g_file_short, table, i, j, cell.text}')
        tables.append(df)
    print(g_file)
print(error_list)
    # print(tables)

df_tables = pd.DataFrame(tables)
print(df_tables)
df_tables.to_excel('выкачка_6.xlsx')