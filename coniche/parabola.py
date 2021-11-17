class parabola:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):
            self.__a = int(p1)  
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []

        elif(tipo == "fuocoDiret"):
            pass
        
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    

    def fuoco(self, asse_simmetria = "x"):
        if (asse_simmetria == "x"):
            y =-((self.__b)/((self.__a)*2))
            x = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
            return f"Le coordinate del fuoco sono {x,y}"

        elif (asse_simmetria == "y"):
            x =-((self.__b)/((self.__a)*2))
            y = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
            return f"Le coordinate del fuoco sono {x,y}"

    def direttrice(self, asse_simmetria = "x"):
        if (asse_simmetria == "x"):
            y= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            return f"L'equazione della direttrice è y = ' {y}"

        elif (asse_simmetria == "y"):
            x= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            return f"L'equazione della direttrice è x = ' {x}"  

valori = parabola(input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ')) 
print(valori.fuoco(input('Asse simmetria parallelo a ' ))) 
print(valori.direttrice(input('Asse simmetria parallelo a ' ))) 

