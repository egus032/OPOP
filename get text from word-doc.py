from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table, _Row
from docx.text.paragraph import Paragraph
import docx
import pandas as pd
import glob
import os
import aspose.words as aw
import docx.package
import docx.parts.document
import docx.parts.numbering
import docx.oxml.numbering as dom
from docx2python import docx2python


path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О\*.docx'

g_glob = glob.glob(path)

counter = 0

df_tables_list = []

stop_kaf = ['ФВиС', 'ГиСД', 'ВМ', 'ОФ', 'ИнЯз']

first_lit = 'УЧЕБНО-МЕТОДИЧЕСКОЕ И ИНФОРМАЦИОННОЕ ОБЕСПЕЧЕНИЕ ДИСЦИПЛИНЫ'
sec_lit = 'МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ ДИСЦИПЛИНЫ'

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

def iter_paragraphs(parent, recursive=True):
    """
    Yield each paragraph and table child within *parent*, in document order.
    Each returned value is an instance of Paragraph. *parent*
    would most commonly be a reference to a main Document object, but
    also works for a _Cell object, which itself can contain paragraphs and tables.
    """
    if isinstance(parent, docx.document.Document):
        parent_elm = parent.element.body
    elif isinstance(parent, docx.table._Cell):
        parent_elm = parent._tc
    else:
        raise TypeError(repr(type(parent)))

    for child in parent_elm.iterchildren():
        if isinstance(child, docx.oxml.text.paragraph.CT_P):
            yield docx.text.paragraph.Paragraph(child, parent)
        elif isinstance(child, docx.oxml.table.CT_Tbl):
            if recursive:
                table = docx.table.Table(child, parent)
                for row in table.rows:
                    for cell in row.cells:
                        for child_paragraph in iter_paragraphs(cell):
                            yield child_paragraph

for g_file in g_glob:
    g_file_short = g_file.replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О' + '\\', '')
    dir_name = os.path.dirname(g_file).replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023' + '\\', '')
    if g_file_short.startswith('РПД_'):
        document = docx2python(g_file)
        for items in document.body:
            for item in items:
                for it in item:
                    if '\t\tРЕАЛИЗАЦИЯ ДИСЦИПЛИНЫ ПРИ ИСПОЛЬЗОВАНИИ ТЕХНОЛОГИЙ ЭЛЕКТРОННОГО ОБУЧЕНИЯ И (ИЛИ) ДИСТАНЦИОННЫХ ОБРАЗОВАТЕЛЬНЫХ ТЕХНОЛОГИЙ' in it:
                        counter += 1
                        print(f'{counter}; {g_file_short}', it)
        # for i in document.body[37]:
        #     print(counter, g_file_short, i)
        # for d in document.body:
        #     counter += 1
        #     print(counter, d)
        # doc = docx.Document(g_file)
        # for block in iter_block_items(doc):
        #     # read Paragraph
        #     if isinstance(block, Paragraph):
        #         # print('ЭТО РПД')
        #         if block.text == first_lit:
        #             counter += 1
        #             for paragraph in iter_paragraphs(doc):
        #                 print(paragraph.text)
        #                 num_pr = dom.CT_NumPr.numId
        #                 print(num_pr)
                            # start_doc = aw.Document(g_file)
                            # s = start_doc.first_section.body.get_child(aw.NodeType.PARAGRAPH, 6, True).as_paragraph()
                    
                    
                    
            # read table
#             elif isinstance(block, Table):
#                 print(block.table.cell(0,0).text)
#                 print(block.table.rows)
#                 print(g_file_short, doc)
#                 if block.table.cell(0,0).text == 'Наименование раздела (темы) дисциплины' and block.table.cell(0,1).text == 'Трудоемкость, час.':
                    
#                     df = [['' for i in range(len(block.table.columns))] for j in range(len(block.table.rows))]
#                     for r, row in enumerate(block.table.rows):
#                         for c, cell in enumerate(row.cells):
#                             # print(r, c, cell.text)
#                             df[r][c] = cell.text
#                     df_tables = pd.DataFrame(df)
#                     df_tables['Имя_файла'] = g_file_short
#                     # print(df)
#                     df_tables_list.append(df_tables)

# df_concat = pd.concat(df_tables_list)

# print(df_tables)
# print(df_concat)

# df_concat.to_excel(f'Сборка_{dir_name}.xlsx')
                      
        
    

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