# чтение файла word 77 конференция и экстракция научных руководителей

import docx
import pandas as pd


g_doc = docx.Document(r'C:\Users\User\Downloads\77_ya_konferentsia 1.docx')
text  = []

substring = 'Научный руководитель:'

for x in g_doc.paragraphs:
    if substring in x.text:
        text.append(x.text)
    
df = pd.DataFrame(text)
print(df)
df.to_excel("Научные рук 77 конф_1.xlsx")

        
    