

import pandas as pd
import pandas_read_xml as pdx
import xml.etree.ElementTree as ET



g_tree = ET.parse(r"C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\++15.03.01_МАШ_ОиТСП_УП(plx)_4.6_2018_заочная.plx").getroot()



g_list = []

for g_item in g_tree.iter():
    g_list.append(g_item.tag)
    print(g_list)
    a = g_item.find(".//{http://tempuri.org/dsMMISDB.xsd}Компетенции").attrib["Наименование"]
    print(a)
    


    