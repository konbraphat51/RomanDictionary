import pandas as pd
from RomanDictionary.Utils import Consts

class Searcher:
    def import_data(self, title):
        self.df = pd.read_csv(Consts.data_folder + title + ".csv")
        
    def search(self, input_word, column, top_n=10):
        target_column = self.df[column]
        distances = [10000.0]*len(target_column)
        for cnt in range(len(target_column)):
            distances[cnt] = self.calc_distance(input_word, target_column[cnt])
        
        df_with_distance = self.df.copy()
        df_with_distance["distance"] = distances
        
        sorted_indices = sorted(range(len(target_column)), key=lambda i: distances[i], reverse=False)

        return df_with_distance.iloc[sorted_indices[:top_n]]
        
    def calc_distance(self, i, a):
        #levenshtein distance
        if i==a:
            return 0.0

        try:
            _i = "_"+i
            _a = "_"+a
        except:
            #data wrong
            return 10000.0
        
        i_n = len(_i)
        a_n = len(_a)
        
        if i_n == 1:
            return a_n
        elif a_n == 1:
            return i_n
        
        dp = [[0.0]*(a_n) for _ in range(i_n)]
        
        #initialize
        dp[0] = [cnt_a for cnt_a in range(a_n)]
        for cnt_i in (range(i_n)):
            dp[cnt_i][0] = cnt_i
            
        #calc
        for cnt_i in range(1, i_n):
            for cnt_a in range(1, a_n):
                a_add_cost = dp[cnt_i][cnt_a-1] + self.cost_add(_a[cnt_a], _a[cnt_a-1])
                i_add_cost = dp[cnt_i-1][cnt_a] + self.cost_add(_i[cnt_i], _i[cnt_i-1])
                change_cost = dp[cnt_i-1][cnt_a-1] + self.cost_change(_i[cnt_i], _i[cnt_i-1], _a[cnt_a], _a[cnt_a-1])

                dp[cnt_i][cnt_a] = min(a_add_cost, i_add_cost, change_cost)
                
        return dp[i_n-1][a_n-1]
                         
    def cost_change(self, i_letter, i_letter_former, a_letter, a_letter_former):
        if i_letter == a_letter:
            return 0.0
        elif (i_letter == i_letter_former) or (a_letter_former == a_letter):
            return 0.5
        else:
            return 1.0
    
    def cost_add(self, letter, letter_former):
        if letter == letter_former:
            return 0.5
        else:
            return 1.0

if __name__ == "__main__":
    searcher = Searcher()
    searcher.import_data("Th2Eng")
    print(searcher.search("sawadii", "Romanized"))