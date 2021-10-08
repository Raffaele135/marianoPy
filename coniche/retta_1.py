print("Lavorare con equazione scritta nella forma: ax + by + c = 0")
class retta:
    

    def __init__(self, a, b, c, x):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__x = float(x)
        self.__punti = []
        

    def Implicita(self):
        if self.__b == 0:
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__c} = 0"       
        elif self.__a == 0:
            return f"\nForma implicita dell'equazione:\n {self.__b}y + {self.__c} = 0"    
        elif self.__c == 0:
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.__b}y = 0"    
        else:   
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__b}y + {self.__c} = 0 "

    def Esplicita(self):
        if self.__b == 0:
            return f"\nForma esplicita dell'equazione: \n L'equazione è impossibile"
        elif self.__a == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__c / self.__b}"
        elif self.__c == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}"
        else:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}x + {-self.__c / self.__b}"
    
    def m(self):
        if self.__b == 0:
            return f"\nCoefficiente angolare: \n Il coefficiente angolare non è definito; la retta è parallela all'asse y"
        else:
            return f"\nCoefficiente angolare: \n m = {-self.__b / self.__a}"
    
    def trovaY(self):
        y = (-self.__a * self.__x) / self.__b + (-self.__c / self.__b)
        return f"\n Y: \n y = {-self.__a * self.__x / self.__b + (-self.__c / self.__b)}"


    def punti(self, N, M, x):
        self.__N = N
        self.__M = M
    
        for self.__N in range (self.__M):
            tupla = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x + 1
            self.__punti.append(tupla)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.__punti}"         



valori = retta(4, 2, 1, 3)
print(valori.Implicita())
print(valori.Esplicita())
print(valori.m())
print(valori.trovaY())
print(valori.punti(0, 300, -100))



