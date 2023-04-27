import glob
import win32com.client as client
import os

counter = 0

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\Таблицы для рассылки\*'

folder_with_files = glob.glob(g_path + '\*.xlsx')

g_excel = client.Dispatch("Excel.Application")
g_excel.Visible = False

for g_file in folder_with_files:
   # print(g_file)
   file = os.path.basename(g_file)
   # output = output_dir + '\\' + file
   wb_2 = g_excel.Workbooks.Open(g_file)
   ws_2 = wb_2.Worksheets('Таблица_для кадровой_справки')
   
   ws_2.Move(Before=wb_2.Worksheets('Для столбца ФИО_ППС'))
   wb_2.Save()
   wb_2.Close(True)
   # wb_2.Close(SaveChanges=True)
   counter += 1
   print(counter, g_file)
   

g_excel.Quit()


# wb1 = xl.Workbooks.Open(Filename=path1)
# wb2 = xl.Workbooks.Open(Filename=path2)


# for filename in files:
#     file = os.path.basename(filename)
#     if file.find('.xls') != -1:
#         print(file)
#         output = output_dir + '\\' + file.replace('.xls','.xlsx')
#         wb = g_excel.Workbooks.Open(filename)
#         wb.ActiveSheet.SaveAs(output,51)
#         wb.Close(True)
#         counter += 1
#         print(counter, output)

# g_excel.Quit()


# input_dir = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\СД СП\Шкумат 11.11'
# output_dir = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\new_folder_1'
# files = glob.glob(input_dir + '\*.xls')