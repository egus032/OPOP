import pandas as pd
from docxtpl import DocxTemplate, InlineImage
import jinja2
import json
import numpy as np
from pathlib import Path

counter = 0

base_dir = Path(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023')

type_level = 'КП_ВР_на_2022-2023_ уч.год_Приложение_1'

output_dir = base_dir/type_level

output_dir.mkdir(exist_ok=True)

docx_file = 'КП ВР на 2022 2023 уч год   Приложение 1+теги.docx'

docx_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023' + '\\' + docx_file

excel_file = 'Список ОПОП для генерации КПВР_+колонки.xlsx'

excel_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023' + '\\' + excel_file


df = pd.read_excel(excel_path, sheet_name='ОПОП из УМУ', header=0)

# df_3_plus_plus = df[(df['ФГОС'] == '3++') & (df['Уровень_ВО_'] == 'магистратура')]

for record in df.to_dict(orient='records'):
    doc = DocxTemplate(docx_path)
    doc.render(record)
    # ГОД_ФАКУЛ_КАФ_Шифр направление_Специальность_Уровень_Форма
    output_path = output_dir/ f"КПВР_{record['Столбец13']}.docx"
    doc.save(output_path)
    # new_file_name = f'{output_path}'.replace(f'{output_dir}\\', '').replace('.docx', '')
    # output_path_pdf = output_dir/f'{new_file_name}.pdf'
    counter += 1
    print(counter, output_path)
    # convert(f'{output_path}', f'{output_path_pdf}')
