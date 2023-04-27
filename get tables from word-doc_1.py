import win32com.client as client
import glob
import os



word_files_folder = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\РПД_2018_10.05.04_аид_О\*'

g_glob = glob.glob(word_files_folder)

g_word = client.Dispatch('Word.Application')
g_word.Visible = False


for word_file in g_glob:
    # print(word_file)
    if word_file.find('~$Д') == -1:
        doc = g_word.Documents.Open(word_file)
        print(doc)
        open_doc = doc.Tables(11).Cell(1, 0)
        # open_doc = doc.Tables.Item(11)
        
        print(open_doc)
        
        doc.Save()
        doc.Close(True)
        
            

g_word.Quit()