# создание файлов из вордовского шаблона и таблицы excel

from pathlib import Path
import pandas as pd
from docxtpl import DocxTemplate
from docx2pdf import convert

base_dir = Path(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список')

filename = r"\ТИПОВАЯ ОПОП_МАГИСТРАТУРА_3+.docx"
type_level = '3+_специалист'

word_template = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список' + filename
excel_template = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\действующие_2022_2023_exel_список\ОПОП_свод 14.11.22++_для генерации_5.xlsx'

output_dir = base_dir/type_level

output_dir.mkdir(exist_ok=True)

df = pd.read_excel(excel_template, sheet_name=type_level)

counter = 0

for record in df.to_dict(orient='records'):
    doc = DocxTemplate(word_template)
    doc.render(record)
    # ГОД_ФАКУЛ_КАФ_Шифр направление_Специальность_Уровень_Форма
    output_path = output_dir/ f"{record['Название_файла']}.docx"
    doc.save(output_path)
    # new_file_name = f'{output_path}'.replace(f'{output_dir}\\', '').replace('.docx', '')
    # output_path_pdf = output_dir/f'{new_file_name}.pdf'
    counter += 1
    print(counter, output_path)
    # convert(f'{output_path}', f'{output_path_pdf}')
    
    
   
    