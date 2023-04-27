import pandas as pd


# список имен столбцов
column_list = ['Экзамен', 'Зачет', 'Зачет с оц.', 'КП', 'КР', 'РГР']

df = pd.read_excel(r'D:\OPOP\Все листы План_5.xlsx', sheet_name='Sheet1')

name_semestr = 'Сем'

name_list = []

# создаем название для столбца "Сем_"+"1"+"column_list[i]"
for g_name in column_list:
    for count in range(1, 13):
        column_name = '_'.join([name_semestr, str(count), g_name])
        name_list.append(column_name)
        
# создаем пустой датафрейм, используя имена для столбцов и указывая старт.индекс и финиш.индекс
df_1 = pd.DataFrame(columns=name_list, index=[id for id in range(df.index[0],df.index[-1]+1)])

# берем столбец Экзамен и возращаем значение, если не равно NaN
# если число больше 9, то его надо разбить
# это значение содержит указание на один или несколько семестров

# список индексов не пустых
list_of_index_nonNaN = df.index[df['Экзамен'].notna()].to_list()
num_1 = df.at[list_of_index_nonNaN[0], 'Экзамен']
print(num_1)