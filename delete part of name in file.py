import os
import shutil
import glob

g_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ\*\*'

g_path_1 = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\ВСЕ РПД от УМУ'

counter = 0

g_list = []

g_list_1 = []

part_of_list = [0, 1, 2, 3, 4]

g_path_glob = glob.glob(g_path)

for g_p in g_path_glob:
    # counter += 1
    # print(counter, g_p)
    filename = os.path.basename(g_p)
    split_path = os.path.split(g_p)
    # print(counter, filename)
    short_filename = filename.split('_')
    # print(short_filename)
    for id, el in enumerate(short_filename):
        if id not in part_of_list:
            short_filename.remove(el)
            short_filename_join = '_'.join(short_filename[0:6])
    counter += 1        
    short_filename_join_docx = short_filename_join + '.docx'
    # print(counter, g_p, split_path[0] + '\\' + short_filename_join_docx)
    print(os.rename(g_p, split_path[0] + '\\' + short_filename_join_docx))
    

    
        
#         g_list.append(g_file_split)
#         # print(len(g_list))
#         for g_item in g_list:
#             for id, el in enumerate(g_item):
#             # print(id, el)
#                 if id not in part_of_list:
#                     g_item.remove(el)
#                 # print(g_item)
#                 g_list_1.append('_'.join(g_item[0:6]) + '.docx')

# print(len(g_list_1))



        # new_name = os.rename(os.path.join(root_1, g_file), os.path.join(root_1, g_new_name))
        # print(new_name)
    # for id, g_file_1 in enumerate(files):
        # if g_file_1.startswith('~$Д_'):
        #     print(id, root_1, g_file_1)
        #     # a = os.remove(os.path.join(root_1, g_file_1))
        #     # print(a)
        
        



    



        




