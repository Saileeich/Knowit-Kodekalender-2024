class Nissmor:
    def __init__(self):
        self.påfyll = {
            "ris": [0,0,1,0,0,2],
            "erter": [0,3,0,0],
            "gulrøtter": [0,1,0,0,0,8],
            "reinsdyrkjøtt": [100,80,40,10]
        }
        self.kjøtt_tid = 0
        self.kjøtt_index = 0

    def get_looped_index(self, t, l):
        return t - len(l) * (t // len(l))
    
    def fyll_på(self, tallerken, t):
        return



class Alvefine:
    def __init__(self):
        self.tallerken = {
            "ris": 100,
            "erter": 100,
            "gulrøtter": 100,
            "reinsdyrkjøtt": 100,
            "julekringle": 100
        }

    def zero_subtract(self, a, b):
        return max(a-b, 0)

    def spis(self, t):
        for rett in self.tallerken.values():
            print(rett)
            break


            
alvefine = Alvefine()
nissmor = Nissmor()

t = -1
while alvefine.tallerken["julekringle"] > 0:
    t += 1
    alvefine.spis(t)
    nissmor.fyll_på(alvefine.tallerken, t)
print(t)