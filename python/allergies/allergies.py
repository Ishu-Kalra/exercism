import math

class Allergies(object):

    master_dict = {1: 'eggs', 2: 'peanuts', 4: 'shellfish', 8: 'strawberries', 16: 'tomatoes', 32: 'chocolates', 64: 'pollen', 128: 'cats',}

    def __init__(self, score):
        self.score = score
        self.init_dict = {'eggs': False, 'peanuts': False, 'shellfish': False, 'strawberries': False, 'tomatoes': False, 'chocolates': False, 'pollen': False, 'cats': False,}
        master_dict = {1: 'eggs', 2: 'peanuts', 4: 'shellfish', 8: 'strawberries', 16: 'tomatoes', 32: 'chocolates', 64: 'pollen', 128: 'cats',}
        k = 0
        for n in range(0, 8):
            if score - math.pow(2, n) < 0:
                k = n - 1
                break
            if n == 8:
                k = 7
        for m in range(0, k + 1):
            if score <= 0:
                break
            if score - math.pow(2, k - m) >= 0:
                self.init_dict[master_dict[math.pow(2, k - m)]] = True
                score = score - math.pow(2, k - m)
        self.allergies_list =[]
        for k, v in self.init_dict.items():
            if v == True:
                self.allergies_list.append(k)

    def is_allergic_to(self, item):
        return self.init_dict[item]

    @property
    def lst(self):
        return self.allergies_list

print(Allergies(129).lst)
