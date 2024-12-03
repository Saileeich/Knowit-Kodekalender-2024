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
        tallerken["ris"] += self.påfyll["ris"][self.get_looped_index(t, self.påfyll["ris"])]
        tallerken["erter"] += self.påfyll["erter"][self.get_looped_index(t, self.påfyll["erter"])]
        tallerken["gulrøtter"] += self.påfyll["gulrøtter"][self.get_looped_index(t, self.påfyll["gulrøtter"])] if t >= 30 else 0
        if self.kjøtt_index < len(self.påfyll["reinsdyrkjøtt"]) and tallerken["reinsdyrkjøtt"] == 0 and t - self.kjøtt_tid >= 50:
            tallerken["reinsdyrkjøtt"] = self.påfyll["reinsdyrkjøtt"][self.kjøtt_index]
            self.kjøtt_index += 1
            self.kjøtt_tid = t

        # prints what got filled
        print(
            f"{t}: ris={self.påfyll['ris'][self.get_looped_index(t, self.påfyll['ris'])]} "
            f"erter={self.påfyll['erter'][self.get_looped_index(t, self.påfyll['erter'])]} "
            f"gulrøtter={self.påfyll['gulrøtter'][self.get_looped_index(t, self.påfyll['gulrøtter'])]} "
            f"reinsdyrkjøtt={self.påfyll['reinsdyrkjøtt'][self.kjøtt_index] if (self.kjøtt_index < len(self.påfyll['reinsdyrkjøtt']) and tallerken['reinsdyrkjøtt'] == 0 and t - self.kjøtt_tid > 50) else 0}"
        )



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
        if self.tallerken["ris"]:
            self.tallerken["ris"] = self.zero_subtract(self.tallerken["ris"], 5)

            if self.tallerken["erter"]:
                self.tallerken["erter"] = self.zero_subtract(self.tallerken["erter"], 3)
                print(f"{t}: spiser ris og erter - ris: {self.tallerken['ris']} erter: {self.tallerken['erter']}")
            elif self.tallerken["gulrøtter"]:
                self.tallerken["gulrøtter"] = self.zero_subtract(self.tallerken["gulrøtter"], 3)
                print(f"{t}: spiser ris og gulrøtter - ris: {self.tallerken['ris']} gulrøtter: {self.tallerken['gulrøtter']}")
            
        elif self.tallerken["erter"]:
            self.tallerken["erter"] = self.zero_subtract(self.tallerken["erter"], 5)

            if self.tallerken["gulrøtter"]:
                self.tallerken["gulrøtter"] = self.zero_subtract(self.tallerken["gulrøtter"], 3)
                print(f"{t}: spiser erter og gulrøtter - erter: {self.tallerken['erter']} gulrøtter: {self.tallerken['gulrøtter']}")
            else:
                print(f"{t}: spiser erter - erter: {self.tallerken['erter']}")

        elif self.tallerken["gulrøtter"]:
            self.tallerken["gulrøtter"] = self.zero_subtract(self.tallerken["gulrøtter"], 5)

            print(f"{t}: spiser gulrøtter - gulrøtter: {self.tallerken['gulrøtter']}")
        elif self.tallerken["reinsdyrkjøtt"]:
            self.tallerken["reinsdyrkjøtt"] = self.zero_subtract(self.tallerken["reinsdyrkjøtt"], 2)

            print(f"{t}: spiser reinsdyrkjøtt - reinsdyrkjøtt: {self.tallerken['reinsdyrkjøtt']}")
        elif self.tallerken["julekringle"] and all(self.tallerken[item] == 0 for item in ["ris", "erter", "gulrøtter", "reinsdyrkjøtt"]):
            self.tallerken["julekringle"] = self.zero_subtract(self.tallerken["julekringle"], 1)

            print(f"{t}: spiser julekringle - julekringle: {self.tallerken['julekringle']}")
            
alvefine = Alvefine()
nissmor = Nissmor()

t = -1
while alvefine.tallerken["julekringle"] > 0:
    t += 1
    nissmor.fyll_på(alvefine.tallerken, t)
    alvefine.spis(t)
print(t)