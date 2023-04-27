from urllib.request import URLopener, urlopen
from bs4 import BeautifulSoup

g_html_main_address = urlopen("https://www.tu-bryansk.ru/sveden/struct/")

g_bs = BeautifulSoup(g_html_main_address, 'html.parser')

nameList_1 = g_bs.find_all('a', {'class' : {'deplist-itm1-title', 'name'}})

for name in nameList_1:
    g_name = name.get_text()
    print(g_name)
