

import docx
import io
import pandas as pd

content = docx.Document(r'C:\Users\User\Downloads\77_ya_konferentsia.docx').paragraphs[1500].text
df = pd.read_csv(io.StringIO(content))


print(content)
