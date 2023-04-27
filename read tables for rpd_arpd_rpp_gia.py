import glob
import pandas as pd
import shutil


g_folder = r'C:\Users\User\Downloads\ГИА\ГИА\*\*.pdf'

target_path = r'C:\Users\User\Downloads\ГИА\target'

g_folder_path = glob.glob(g_folder)

def transfer_files(g_folder_path, target_path):
    for f in g_folder_path:
        shutil.move(f, target_path)
        print(f)


transfer_files(g_folder_path, target_path=target_path)