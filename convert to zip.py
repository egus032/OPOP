import shutil
import glob

folder_name = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\Нагрузка\Таблицы для рассылки\*')


for f in folder_name:
    print(f)
    shutil.make_archive(f, 'zip', f)
    