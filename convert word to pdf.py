
import glob
from docx2pdf import convert
from pathlib import Path

g_folder = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Отсутствующие ОПОП на 28.10.22\Новая папка\ЛА\*.docx')

base_dir = Path(__file__).parent

output_dir = base_dir/"ЛА_16 файлов_pdf"

output_dir.mkdir(exist_ok=True)

counter = 0

for g_file in g_folder:
    new_file_name = g_file.replace('C:\\Users\\User\\Desktop\\Рабочая папка\\от Геращенковой\\2022\\c 01.08.22\\Отсутствующие ОПОП на 28.10.22\\Новая папка\\ЛА\\', '').replace('.docx', '')
    output_path = output_dir/f'{new_file_name}.pdf'
    counter += 1 
    print(counter)
    convert(f'{g_file}', f'{output_path}')
    
    
