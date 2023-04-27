import pandas as pd
from docxtpl import DocxTemplate
import jinja2
import json
# from pandas import option_context

common_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023'

docx_file = 'КС_шаблон для заполнения.docx'

word_template = common_path + '\\' + docx_file

excel_file = r'ВСЕ КС таблицы_11.04.22.xlsx'

excel_path = common_path + '\\' + excel_file

df = pd.read_excel(excel_path, sheet_name='Sheet1', header=0) #.drop(labels=['Столбец1', 'Unnamed: 0'], axis=1)

names_opop = pd.Series(df['Общий_код']).drop_duplicates().to_list()

for name_opop in names_opop:
                      
        df_pivot_table = pd.pivot_table(df, index=['Общий_код', 'Год_набора', 'Форма_обучения', 'Номер', 'Дисциплина_практика_ГИА', 'ФИО_итоговые', 'Уровень_ВО',
        'Степень_звание','Условия_привлечения', 'Процент_практиков', 'Процент_остепененности', 'Код_направление', 'Профиль_подготовки_специализация'],
                values=['Часы', 'Часы_к_ставке'], aggfunc='sum').query('Общий_код == @name_opop')
        
        df_code_opop = pd.pivot_table(df, index = ['Код_направление', 'Профиль_подготовки_специализация'], aggfunc='sum')
                
        # df_pivot_table = df_pivot_table.reset_index().drop(labels='Общий_код', axis=1)  

        df_pivot_table = df_pivot_table.reset_index()
        
        fio_pps = len(pd.Series(df_pivot_table['ФИО_итоговые']).drop_duplicates().to_list())

        sum_stavki_opop = str(round(pd.Series(df_pivot_table['Часы_к_ставке']).sum(), 3)).replace('.', ',')

        form_opop = pd.Series(df_pivot_table['Форма_обучения']).drop_duplicates().to_string().replace('0    ', '')
                
        year_start_opop = pd.Series(df_pivot_table['Год_набора']).drop_duplicates().to_string().replace('0    ', '')

        level_opop = pd.Series(df_pivot_table['Уровень_ВО']).drop_duplicates().to_string().replace('0    ', '')

        code_opop = pd.Series(df_pivot_table['Код_направление']).drop_duplicates().to_string().replace('0    ', '')
                
        profile_opop = pd.Series(df_pivot_table['Профиль_подготовки_специализация']).drop_duplicates().to_string().replace('0    ', '')

        # with option_context('display.max_colwidth', None):
        #         print(len(code_opop))
        #         print(len(profile_opop))
                
        df_discipline = df_pivot_table.drop(labels=['Общий_код', 'Год_набора', 'Форма_обучения'], axis=1)
                        
        df_discipline['Часы'] = df_discipline['Часы'].round(3)
        df_discipline['Часы_к_ставке'] = df_discipline['Часы_к_ставке'].round(3)

        # perc_all = pd.Series(df_pivot_table['процент_занимается наукой']).round(2).drop_duplicates().to_string().replace('0    ', '')
        perc_pr = pd.Series(df_pivot_table['Процент_практиков']).round(2).drop_duplicates().to_string().replace('0    ', '')
        perc_os = pd.Series(df_pivot_table['Процент_остепененности']).round(2).drop_duplicates().to_string().replace('0    ', '')

        total_h = df_discipline['Часы'].round(2).sum()
        total_stavki = df_discipline['Часы_к_ставке'].round(2).sum()
                
        print(df_discipline)
        print(name_opop)
        print(level_opop)
        print(code_opop)
        print(profile_opop)
        print(perc_os, perc_pr)
        print(total_h, total_stavki)
        print('Численность научно-педагогических работников:', fio_pps)
        print('Общее количество ставок, занимаемых НПР:', sum_stavki_opop)
        print('форма обучения:', form_opop)
        print('год набора:', year_start_opop)

        g_context = {
                'level' : level_opop,
                'profile' : profile_opop,
                'shifr' : code_opop,
                'form_opop' : form_opop,
                'year_start' : year_start_opop,
                'count_pps' : fio_pps,
                'stavki' : sum_stavki_opop,
                # 'percent_all' : perc_all,
                'percent_pr' : perc_pr,
                'percent_os' : perc_os,
                'total_hours' : total_h,
                'total_stavki' : total_stavki,
                'disciplines' : json.loads(df_discipline.to_json(orient='records'))
        }

        doc = DocxTemplate(word_template)
        jinja_env = jinja2.Environment()
        doc.render(g_context, jinja_env)
        output_path = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\апрель 2023\Кадровые справки в ворд' +  '\\' + f"КС_{name_opop}.docx"
        doc.save(output_path)

        

        
        


                        
