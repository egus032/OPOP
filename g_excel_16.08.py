
# Сбор информации по каждой основной профессиональной образовательной программе высшего образования

import csv
import pandas as pd
import xml.etree.ElementTree as ET

g_opop_table = pd.DataFrame(columns=["ОПОП ВО", "Год набора", "Срок обучения", "Название дисциплин/индекс", "Семестр", "Код компетенции", 
"Наименование компетенции (1-n)", "Общая трудоемкость дисциплины, з.е.", "Общая трудоемкость дисциплины, ак.час.", "Лекции, час.", "Лабораторные работы, час.",
"Практические занятия, рас.", "Самостоятельная работа обучающихся, час.", "Курсовой проект (да/пусто если отсутствует)", "Курсовая работа (да/пусто если отсутствует)",
"Расчетно-графическая работа (да/пусто если отсутствует)", "Типы практик", "Количество по видам практик з.е.", "Форма промежуточной аттестации", "Закрепление дисциплин за кафедрами"])

g_tree = ET.parse(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\++15.03.01_МАШ_ОиТСП_УП(plx)_4.6_2018_заочная.plx")
g_root = g_tree.getroot()

csvFile = open("editors_17.08.22.csv", "wt+")
writer = csv.writer(csvFile)
for child in g_root.iter():
    
    g_list = []
    g_list.append(f"{child.tag} ; {child.attrib}")
    writer.writerow(g_list)
    
    