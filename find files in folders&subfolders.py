import os		
from zipfile import ZipFile
import pandas as pd
import shutil
import glob
import re
from pathlib import Path


file_list = []

counter = 0

# подсчет и вывод в файл всех файлов из подпапок
# path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\Новая папка'
# for root, dirs, files in os.walk(path):
#     for file in files:
#         counter +=1
#         print(counter, os.path.join(root, file))
#         file_list.append(os.path.join(root, file))

# df = pd.DataFrame(file_list)
# df.to_excel('РПД разложенные по папкам_1 версия.xlsx')
# print(df)


# копирование всех РПД в отдельную папку
# path = r'C:\Users\User\Desktop\Exel_22_03_2023_2023_2024_1_курc'
# path_for_copyfile = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\все УП от УМУ'
# for root, dirs, files in os.walk(path):
#     for file in files:
#         # if file.startswith('РПД') and file.endswith('.doc'):
#             counter += 1
#             g_copy = shutil.copy(os.path.join(root, file), path_for_copyfile + '\\' + file)
#             print(counter, g_copy)

# копирование всех Учебных планов в отдельную папку
path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\!!!!!!!!_05_04_2023_Exel_plx_2023_2024_1_курс_+++++++'
path_for_copyfile = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\Учебные планы от 05.04.23'
for root, dirs, files in os.walk(path):
    for file in files:
        # if file.startswith('РПД') and file.endswith('.doc'):
            counter += 1
            g_copy = shutil.copy(os.path.join(root, file), path_for_copyfile + '\\' + file)
            print(counter, g_copy)

# убрать ++_УП из имени файла
# counter = 0
# path_for_copyfile = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\все УП от УМУ'
# path_for_copyfile_2 = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\все УП от УМУ без ++_УП и .plx'
# for root, dirs, files in os.walk(path_for_copyfile):
#     for file in files:
#         if file.startswith('++_УП_') and file.find('.plx'):
#             short_file_name = file.replace('++_УП_', '').replace('.plx', '')
#             counter += 1
#             # print(counter, short_file_name)
#             g_copy = shutil.copy(os.path.join(root, file), path_for_copyfile_2 + '\\' + short_file_name)
#             print(counter, g_copy)
            
# убрать Фамилия И.О. из имени файла
# path_for_copyfile = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\все РПД от УМУ'
# path_for_copyfile_2 = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД без ФИО'
# part_of_list = [0, 1, 2, 3, 4, 6, 7]
# for root, dirs, files in os.walk(path_for_copyfile):
#     for file in files:
#         split_path = file.split('_')
#         # print(split_path)
#         for id, el in enumerate(split_path):
#             if id not in part_of_list:
#                 split_path.remove(el)
#                 split_path_join = '_'.join(split_path[0:8])
#                 # print(split_path_join)
#                 counter += 1
#                 g_copy = shutil.copy(os.path.join(root, file), path_for_copyfile_2 + '\\' + split_path_join)
#                 print(counter, g_copy)


# разложить файлы по папкам ОПОП через копирование
# excel_file = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД по ОПОП статистика.xlsx'
# df = pd.read_excel(excel_file, sheet_name='Для сборки', header=0)
# df_list = df['Названия строк'].tolist()

# docx_files_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД без ФИО\*'
# glob_path = glob.glob(docx_files_path)
# g_folder_name = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\Новая папка'

# for item in df_list:
#     for file_name in glob_path:
#         file = os.path.basename(file_name)
#         if re.search(item, file):        
#             base_dir = Path(g_folder_name)
#             output_dir = base_dir/f'РПД_{item}'
#             output_dir.mkdir(exist_ok=True)
#             output_path = output_dir/file
#             g_copy = shutil.copy(file_name, output_path)
#             counter += 1
#             print(counter, g_copy)
            

    






# path_2 = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в'
# counter = 0

# excel_file_exclude = r'D:\OPOP\список моих РПД и ФТД.xlsx'
# df_exclude = pd.read_excel(excel_file_exclude, sheet_name='Исключить_РПД', header=0)
# list_of_exclude = list(df_exclude['Название архива РПД'])
# print(list_of_exclude)

# file_list = []
# for root, dirs, files in os.walk(path_2):
#     for file in files:
#         if file.startswith('АРПД_') and file.endswith('.zip'):
#             zip_folder = os.path.join(root, file)
#             with ZipFile(zip_folder, 'r') as zip:
#                 for f in zip.namelist():
#                     file_list.append(f)
#                     counter += 1
#                     print(counter, f)

# df = pd.DataFrame(file_list)
# df.to_excel('список АРПД.xlsx')

# удалить zip папки из папки по условию
# for list_item in list_of_exclude:
#     for root, dirs, files in os.walk(path_2):
#         for file in files:
#             if file.endswith('.zip') and file.find(list_item):
#                 zip_folder_delete = os.path.join(root, file)
#                 file_list.append(zip_folder_delete)
#                 remove_to = os.remove(zip_folder_delete)
#                 print(zip_folder_delete)
                
