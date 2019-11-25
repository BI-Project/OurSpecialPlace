import numpy as np
import math

class FunctionBox:
    def __init__(self, user_choice, dataset):
        self.user_choice = user_choice #1차원 리스트
        self.Dataset = dataset #여행지의 이름과 배열이 담긴 딕셔너리
        self.cos_data = {}
        self.top_ten_list = {}

    def CosSimilarity(self):
        Set1 = np.array(self.user_choice)
        for spot_name in self.Dataset.keys():
            Set2 = np.array(self.Dataset[spot_name])
            multi = sum(Set1 * Set2)
            x = math.sqrt(sum(Set1 * Set1))
            y = math.sqrt(sum(Set2 * Set2))
            if x * y != 0:
                result = multi / (x * y)
            else:
                result = 0
            self.cos_data[spot_name] = result

    def print_userchoice(self):
        print(self.user_choice)

    def print_cosdata(self):
        print(self.cos_data)

    def print_top10list(self):
        print(self.top_ten_list)

    def Ranking(self):
        temp = sorted(list(self.cos_data.values()))
        top_ten = temp[::-1][:10]
        for score in top_ten:
            for name in self.cos_data.keys():
                if score == self.cos_data[name]:
                    self.top_ten_list[name] = score
        return self.top_ten_list
