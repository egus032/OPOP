import glob
from pathlib import Path
import shutil


from_folder = r'C:\Users\User\Downloads\РПД и АРПД ГиСД - копия\*'
example_folders = r'C:\Users\User\Downloads\Архив 3+\*'
g_folders_1 = glob.glob(example_folders)
g_folders_2 = glob.glob(from_folder)
base_dir = Path(r'C:\Users\User\Desktop\Дадыкин В.С\РПД')
counter = 0

for fold_0 in g_folders_1:
    fold_short_name = fold_0.replace(r'C:\Users\User\Downloads\Архив 3+' + '\\', '')
    fold_short_name = fold_short_name.replace('zip', '')

    for fold_1 in g_folders_2:
        fold_1_short_name = fold_1.replace(r':\Users\User\Downloads\РПД и АРПД ГиСД - копия' + '\\', '')
        if fold_1.find(fold_short_name) != -1:          
            output_dir = base_dir/fold_short_name
            output_dir.mkdir(exist_ok=True)        
            a = shutil.move(fold_1, output_dir)
            counter += 1
            print(counter, fold_1)
    