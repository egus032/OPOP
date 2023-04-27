import pandas as pd
from docxtpl import DocxTemplate, InlineImage
import jinja2
import json
import numpy as np
from pathlib import Path
import glob

counter = 0

docx_file = r'\ТИПОВАЯ ОПОП_МАГИСТРАТУРА 3++.docx'

level_opop = 'магистратура'

base_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\30.03.23_всё для ОПОП'

base_dir = Path(base_folder)

output_dir = base_dir/level_opop

output_dir.mkdir(exist_ok=True)

docx_files_folder = base_folder + docx_file

excel_files_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\30.03.23_всё для ОПОП\ОПОП_excel_2\*'

excel_path = glob.glob(excel_files_folder)

excel_list = []

for g_file in excel_path:
    df = pd.read_excel(g_file, sheet_name='новыеОПОП_Гринь')
    excel_list.append(df)
    df_1 = pd.concat(excel_list)

df_to_docx = df_1[(df_1['Уровень_ВО_'] == level_opop)]
print(df_to_docx)

for record in df_to_docx.to_dict(orient='records'):
    doc = DocxTemplate(docx_files_folder)
    doc.render(record)
    # ГОД_ФАКУЛ_КАФ_Шифр направление_Специальность_Уровень_Форма
    output_path = output_dir/ f"{record['Название_файла']}.docx"
    doc.save(output_path)
    # new_file_name = f'{output_path}'.replace(f'{output_dir}\\', '').replace('.docx', '')
    # output_path_pdf = output_dir/f'{new_file_name}.pdf'
    counter += 1
    print(counter, output_path)
    # convert(f'{output_path}', f'{output_path_pdf}')





