from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table, _Row
from docx.text.paragraph import Paragraph
import docx
import pandas as pd

path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\Кадровые справки в ворд_2_rename\КС_АТ_2019_23.03.01_обд_З.docx'
doc = docx.Document(path)

df_tables = []

def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    elif isinstance(parent, _Row):
        parent_elm = parent._tr
    else:
        raise ValueError("Что-то пошло не так!!")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

for block in iter_block_items(doc):
    # read Paragraph
    if isinstance(block, Paragraph):
        print(block.text)
    # read table
    elif isinstance(block, Table):
        # print(block.style.name)
        # print(block.table.rows)
        df = [['' for i in range(len(block.table.columns))] for j in range(len(block.table.rows))]
        for r, row in enumerate(block.table.rows):
            for c, cell in enumerate(row.cells):
                # print(r, c, cell.text)
                df[r][c] = cell.text
        # print(df)
        df_tables.append(pd.DataFrame(df))

df_concat = pd.concat(df_tables)

print(df_tables)
print(df_concat)

df_concat.to_excel('Кадровая справка_таблица_тест.xlsx')
  
# Таблица 1 – Планируемые результаты обучения по дисциплине
# Таблица 2 – Распределение трудоемкости дисциплины по видам учебной работы и семестрам
# Таблица 3 – Тематический план дисциплины
# Таблица 4 – Формирование компетенций по разделам дисциплины
# Таблица 5 – Тематика и содержание лекций
# Таблица 6 – Тематика лабораторных работ
# Таблица 7 – Тематика и содержание практических занятий
# Таблица 8 – Вопросы для самостоятельного изучения дисциплины
# Таблица 9 – Виды самостоятельной работы
# Таблица 10 – Формы и периодичность текущего контроля успеваемости
# Таблица 11 – Образовательные технологии, применяемые в ходе преподавания дисциплины
# Таблица 12 – Методические рекомендации обучающимся по освоению дисциплины
# Таблица 13 – Виды и средства оценивания результатов освоения дисциплины
# Таблица 14 – Критерии и шкала оценки РГР / доклада (реферата), его пре-зентации (выбрать необходимое) по дисциплине
# Таблица 15 – Шкала оценивания при промежуточной аттестации обучающихся
# Таблица 16 – Шкала оценивания, применяемая при выполнении и защите курсовой работы (курсового проекта) для технических дисциплин
# Таблица 17 – Шкала оценивания, применяемая при выполнении и защите курсовой работы (курсового проекта) для гуманитарных дисциплин
# Таблица 18 – Характеристика результатов обучения по дисциплине

