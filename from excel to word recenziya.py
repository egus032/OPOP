# создание файлов из вордовского шаблона и таблицы excel

from pathlib import Path
import pandas as pd
from docxtpl import DocxTemplate


base_dir = Path(__file__).parent

file_name = '\\ИСПРАВ Шаблон рецензии № 2 специалитет.docx'
type_file = '№2_специалист'

word_template = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Макет рецензий_29.09.22" + file_name
excel_template = r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Макет рецензий_29.09.22\ОПОП для рецензии.xlsx"

output_dir = base_dir/type_file

output_dir.mkdir(exist_ok=True)

df = pd.read_excel(excel_template, sheet_name=type_file)

for record in df.to_dict(orient='records'):
    doc = DocxTemplate(word_template)
    doc.render(record)
    # ГОД_ФАКУЛ_КАФ_Шифр направление_Специальность_Уровень_Форма
    output_path = output_dir/ f"{record['Название_файла']}.docx"
    doc.save(output_path)