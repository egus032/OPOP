from gc import garbage
import PyPDF2
import glob
import fitz

g_folder = glob.glob(r'D:\OPOP\3++_специалист_pdf\*.pdf')

list_pages = []

for g_file in g_folder:
    g_doc = fitz.open(g_file)
    del_pages = list(range(g_doc.page_count))
    print(del_pages[-1])
    for p in del_pages:
        if p == del_pages[-1]:
            
 
    g_doc.save(g_file, garbage=3)
    g_doc.close(g_file)
        
    # file_open = open(g_file, 'rb')
    # ReadPDF = PyPDF2.PdfFileReader(file_open)
    # pages = ReadPDF.getNumPages()
    
    # a = list(range(pages))
    # g_page = fitz.Document(g_file).delete_pages(a[-2:])

    # file_open = open(g_file, 'rb')
    # ReadPDF = PyPDF2.PdfFileReader(file_open)
    # pages = ReadPDF.getNumPages()
    # a = list(range(pages))
    # del a[-2:]
    # print(a)


        
        
    