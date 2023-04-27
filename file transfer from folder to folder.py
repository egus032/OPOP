import glob
import shutil

g_folder = glob.glob(r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\СД СП\СД и СП\СД и СП\*\*')

# g_folder_1 = glob.glob(r'C:\Users\User\Downloads\БГТУ_exel\БГТУ_exel\*\*\*\*.xlsx')

target = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2022\c 01.08.22\СД СП\СД и СП'


for f in g_folder:
   a = shutil.move(f, target)
   print(f)