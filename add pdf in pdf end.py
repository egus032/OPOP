import glob
import PyPDF2
import fitz
from pathlib import Path

opop_folder = glob.glob(r'D:\OPOP\ОПОП_24 файла_pdf\*.pdf')

la_folder = glob.glob(r'D:\OPOP\ЛА_16 файлов_pdf\*.pdf')

base_dir = Path(__file__).parent

output_dir = base_dir/"ОПОП_ЛА на сайт 28.10.22_pdf"

output_dir.mkdir(exist_ok=True)

counter = 0

for la_item in la_folder:
    for opop_item in opop_folder:
        if opop_item.find(la_item.replace('D:\\OPOP\\ЛА_16 файлов_pdf\\ЛА_', '')) != -1:
            new_file_name = opop_item.replace('D:\\OPOP\\ОПОП_24 файла_pdf\\', '')
            opop_item_pdf = fitz.open(opop_item)
            la_item_pdf = fitz.open(la_item)
            opop_item_pdf.insert_pdf(la_item_pdf)
            counter += 1
            print(counter)
            opop_item_pdf.save(output_dir/f'{new_file_name}',garbage=3,deflate=True)
        
        
