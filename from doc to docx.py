from glob import glob
import re
import os
from win32com.client import constants
import win32com.client as client


# Create list of paths to .doc files
paths = glob('C:\\path\\to\\doc\\files\\**\\*.doc', recursive=True)

path_g = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в'

g_word = client.Dispatch("Word.Application")
g_word.Visible = False

counter = 0

list_path = []

output_dir = r'\C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в\Doc'

for root, dirs, files in os.walk(path_g):
    for g_file in files:
        if g_file.endswith('.doc') and g_file.find('АРПД') == -1:
            list_path.append(os.path.join(root, g_file))

# print(len(list_path), list_path)

for filename in list_path:
    print(filename)
    counter += 1
    file = os.path.basename(filename)
    file_docx = file.replace('.doc','.docx')
    output = os.path.join(root, file_docx)
    doc = g_word.Documents.Open(filename)
    doc.SaveAs(output, FileFormat = 16)
    doc.Close(True)
    print(counter, output)
            

g_word.Quit()
                

