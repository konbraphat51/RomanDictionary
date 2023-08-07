import requests
from bs4 import BeautifulSoup
import pandas as pd
from RomanDictionaryMaker.Utils import Consts
from pythainlp.transliterate import romanize

class DataMaker_Th:
    def scrape(should_save = False):
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
                pass
                    
        df = pd.DataFrame(temp_table, columns=["Eng", "Th"])

        if should_save:
            df.to_csv(Consts.datamaker_folder + "list_simple_Th.csv", index=False)
            
        return df
    
    def romanize_df(df, should_save = False):
        romanized = []
        for th in df["Th"]:
            try:
                romanized.append(romanize(th, "thai2rom"))
            except:
                print(th)
            
        df["Romanized"] = romanized
        
        if should_save:
            df.to_csv(Consts.datamaker_folder + "list_romanized_Th.csv", index=False)
    
        return df
        
    def sort_alphabetically(df, should_save = True):
        #sort by Eng
        df_sorted_eng = df.copy().sort_values(by=["Eng"])
        
        #sort by Romanized
        df_sorted_romanized = df.copy().sort_values(by=["Romanized"])
        
        #sort by Th
        df_sorted_th = df.copy().sort_values(by=["Th"])
        
        if should_save:
            df_sorted_eng.to_csv(Consts.data_folder + "1_Th.csv", index=False)
            df_sorted_romanized.to_csv(Consts.data_folder + "romanized_Th.csv", index=False)
            df_sorted_th.to_csv(Consts.data_folder + "0_Th.csv", index=False)
    
        return df_sorted_eng, df_sorted_romanized, df_sorted_th
    
    def run(output = [False, False, True]):
        df_list_simple = DataMaker_Th.scrape(should_save=output[0])
        df_romanized = DataMaker_Th.romanize_df(df_list_simple, should_save=output[1])
        df_sorted_eng, df_sorted_romanized, df_sorted_th = DataMaker_Th.sort_alphabetically(df_romanized, should_save=output[2])
        
        return df_sorted_eng, df_sorted_romanized, df_sorted_th
    
if __name__ == "__main__":
    DataMaker_Th.run()
    