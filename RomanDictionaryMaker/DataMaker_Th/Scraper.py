import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from RomanDictionaryMaker.Utils import Consts

res = requests.get("https://3000mostcommonwords.com/list-of-3000-most-common-thai-words-in-english/")
soup = BeautifulSoup(res.content, "html.parser")

temp_table = []

tr_even = soup.find_all("tr", class_="even")
tr_odd = soup.find_all("tr", class_="odd")

trs = tr_even + tr_odd

for tr in trs:
    try:
        tds = tr.find_all("td")
        engs = tds[1].get_text().split(", ")
        th = tds[4].get_text()
        
        for eng in engs:
            temp_table.append([eng, th])
    except:
        print(tr)
            
df = pd.DataFrame(temp_table, columns=["Eng", "Th"])

df.to_csv(Consts.datamaker_foler + "list_simple.csv", index=False)