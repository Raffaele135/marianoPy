print("Lavorare con equazione scritta nella forma: ax + by + c = 0")
class retta:
    
    

    def __init__(self, a, b, c, x):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.x = float(x)
        

    def Implicita(self):
        if self.b == 0:
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.c} = 0"       
        elif self.a == 0:
            return f"\nForma implicita dell'equazione:\n {self.b}y + {self.c} = 0"    
        elif self.c == 0:
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.b}y = 0"    
        else:   
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.b}y + {self.c} = 0 "

    def Esplicita(self):
        if self.b == 0:
            return f"\nForma esplicita dell'equazione: \n L'equazione è impossibile"
        elif self.a == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.c / self.b}"
        elif self.c == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.a / self.b}"
        else:
            return f"\nForma esplicita dell'equazione: \n y = {-self.a / self.b}x + {-self.c / self.b}"
    
    def punti(self):
        for i in range (600):
            y = (-self.a * self.x) / self.b + (-self.c / self.b)
            tupla = (self.x, y)
            self.x = self.x + 1
            print(tupla)





valori = retta(input('a = '), input('b = '), input('c = '), -300)
print(valori.punti())



