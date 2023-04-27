import os


g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_к_16.02.23_2в'


counter = 0


for root, dirs, files in os.walk(g_path):
    for dir in dirs:
        # counter += 1
        split_folder = os.path.split(os.path.join(root, dir))
        # print(counter, split_folder[1])
        if split_folder[1].startswith('РПД') or split_folder[1].startswith('Архив_РПД'):
            for g_file in files:
                counter += 1
                print(counter,  g_file)