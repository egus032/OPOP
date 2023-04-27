from urllib.request import URLopener, urlopen
from bs4 import BeautifulSoup as bs

g_html_main_address = "https://www.stoloto.ru/4x20/archive/"

g_lottery_draw = 5030
 
def get_string_for_url(g_html_main_address, g_lottery_draw):
    g_list = []
    for g_link in range(1, g_lottery_draw):
        g_string = f"{g_html_main_address}{g_link}"
        g_list.append(g_string)
    return g_list

g_value = get_string_for_url(g_html_main_address, g_lottery_draw)
# print(g_value[1080])


        
        
    
    
    