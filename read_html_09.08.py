from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pandas as pd

g_html_main_address = "https://www.stoloto.ru/4x20/archive/"

g_lottery_draw = 5060
 
def get_string_for_url(g_html_main_address, g_lottery_draw):
    g_list = []
    for g_link in range(5036, g_lottery_draw):
        g_string = f"{g_html_main_address}{g_link}"
        g_list.append(g_string)
    return g_list

g_value = get_string_for_url(g_html_main_address, g_lottery_draw)

g_list_p_tag = []

for g_html_page in g_value:
    g_url = urlopen(g_html_page)
    g_bs = BeautifulSoup(g_url.read(), "html.parser")
    g_p_tag = [p_tag.get_text() for p_tag in g_bs.find_all("p", {"class" : "number"})]
    g_my_data = f"{g_bs.h1.get_text()}, {g_p_tag}"
    g_list_p_tag.append(g_my_data)
      
    with open("draws_data_19.08.csv", "wt+") as f:
        for i in g_list_p_tag:
            f.write(f"{i}\n")
        print(f"{i}\n")
    
    