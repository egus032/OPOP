import pandas as pd
import glob
import os
import win32com.client as client

counter = 0

g_excel = client.Dispatch("Excel.Application")
g_excel.Visible = False
input_dir = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\СД СП\СД и СП'
output_dir = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\new_folder'
files = glob.glob(input_dir + '\*.xls')

for filename in files:
    file = os.path.basename(filename)
    if file.find('.xls') != -1:
        print(file)
        output = output_dir + '\\' + file.replace('.xls','.xlsx')
        wb = g_excel.Workbooks.Open(filename)
        wb.ActiveSheet.SaveAs(output,51)
        wb.Close(True)
        counter += 1
        print(counter, output)

g_excel.Quit()

# проверить названия листов в файлах
# for g_file in g_folder:
#     xl = pd.ExcelFile(g_file)
#     g_file_short = g_file.replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\СД СП\СД и СП'+'\\', '')
#     if g_file_short.find('xls') != -1:
        
    
    # if split_tup[1] == 'xls':
    #     print(split_tup[1])

    # print(g_file_short, xl.sheet_names)
    # if xl.sheet_names[0] != 'Лист1':
    #     wb = openpyxl.load_workbook(filename=g_file)
    #     wb.active.title = 'Лист1'
    #     wb.save(g_file)
        
        # print('Неправильное имя!', g_file_short)


    




# for g_file in g_folder:

#     # ss=openpyxl.load_workbook(g_file)
#     # print(ss.sheetnames, g_file)
        
#     df = pd.read_excel(g_file, sheet_name='TDSheet', header=[0])
#     df['Имя файла_общее'] = g_file
#     print(g_file, ' ', df.columns)
#     g_list.append(df)

# df_1 = pd.concat(g_list) #, axis=0, ignore_index=True
    

# df_1.to_excel('ФРДО_2.xlsx')