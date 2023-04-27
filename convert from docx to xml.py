from docx_utils.flatten import opc_to_flat_opc
import glob
import xml.etree.ElementTree as ET

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О\*'

g_glob = glob.glob(g_path)

counter = 0

# превращаем .docx в .xml
# for g in g_glob:
#     g_short = g.replace(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О' + '\\', '').replace('.docx', '.xml')
#     opc_to_flat_opc(g, r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О' + '\\' + g_short)


# читаем .xml
for g in g_glob:
    if g.endswith('.xml'):
        tree = ET.parse(g)
        root = tree.getroot()
        print(root.tag, root.attrib)
        for child in root:
            print(child.tag, child.attrib)
        

        break
              


    