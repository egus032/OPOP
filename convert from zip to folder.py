import glob
from zipfile import ZipFile
from pathlib import Path

folder_name = glob.glob(r'C:\Users\User\Downloads\Архив 3+\*')

output_path = Path(r'D:\OPOP\Извлечение архива РПД')

for folder in folder_name:
    folder_name_short = folder.replace(r'C:\Users\User\Downloads\Архив 3+' + '\\', '').replace('zip', '')
    with ZipFile(folder, 'r') as f:
        f.extractall(output_path/folder_name_short)
        print(f)
    
