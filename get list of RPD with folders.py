import pandas as pd
import os
import shutil
from pathlib import Path


excel_file_opop = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД по ОПОП статистика.xlsx'

df = pd.read_excel(excel_file_opop, sheet_name='ОПОП из сводной', header=[1])
list_of_opop = df['Названия строк'].tolist()
# print(list_of_opop)

# перемещение РПД в новую папку для сортировки or file.startswith('~$Д_')
# path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в'
# destination_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ'

# for root, dirs, files in os.walk(path):
#     for file in files:
#         if file.startswith('РПД_'):
#             file_to_move = destination_folder + '\\' + file
#             if os.path.isfile(os.path.join(root, file)):
#                 shutil.move(os.path.join(root, file), file_to_move)
#                 print('Перемещение файла:', file)
        
all_rpd_files_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ'

for root, dirs, files in os.walk(all_rpd_files_folder):
    for g_file in files:
        for item in list_of_opop:
            if g_file.find(item) != -1:
                
                base_dir = Path(all_rpd_files_folder)
                output_dir = base_dir/item
                output_dir.mkdir(exist_ok=True)
                # print(output_dir)
                if os.path.isfile(os.path.join(root, g_file)):
                    shutil.move(os.path.join(root, g_file), output_dir/g_file)
                    print('Перемещение файла:', g_file, 'в папку:', output_dir)
