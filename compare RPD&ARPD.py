import pandas as pd
import glob


initial_folder = r'D:\OPOP\Извлечение архива РПД\*\*'

final_folder = r''


initial_glob = glob.glob(initial_folder)
final_glob = glob.glob(final_folder)

g_list_1 = []
g_list_2 = []

for i in initial_glob:
    i_short = i.replace(r'D:\OPOP\Извлечение архива РПД' + '\\', '')
    print(i_short)
    g_list_1.append(i_short)

df = pd.DataFrame(g_list_1)
df.to_excel('исходные файлы.xlsx')


