
import glob
from docx2pdf import convert
from pathlib import Path

g_folder_1 = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\РПП\Для РПП_бак до 2021\*\*.docx')

g_folder_2 = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\РПП\Для РПП_бак до 2021\*')

counter = 0

for folder in g_folder_2:
    new_folder = folder.replace('C:\\Users\\User\\Desktop\\Рабочая папка\\от Геращенковой\\2022\\c 01.08.22\\РПП\\Для РПП_бак до 2021\\', '')
    for filename in g_folder_1:
        new_file_name = filename.replace('C:\\Users\\User\\Desktop\\Рабочая папка\\от Геращенковой\\2022\\c 01.08.22\\РПП\\Для РПП_бак до 2021\\', '')
        if new_file_name.find(new_folder) != -1:
            new_file_name = new_file_name.replace(f'{new_folder}\\', '').replace('.docx', '')
            base_dir = Path(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\РПП\PDF_Для РПП_бак до 2021')
            output_dir = base_dir/f'{new_folder}_pdf'
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir/f'{new_file_name}.pdf'
            print(filename, output_path)
            convert(f'{filename}', f'{output_path}')
            
        
            
                


