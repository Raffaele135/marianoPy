class retta:
   
    def __init__(self, eqImplicita, eqEsplicita, Coordinate):
        self.eqImplicita = (eqImplicita)
        self.eqEsplicita = (eqEsplicita)
        self.Coordinate = (Coordinate)

    
    def equazione_esplicita(self):
        return f'Consegna:\n  Equazione esplicita:\n{self.eqEsplicita}\n Equazione implicita:\n{self.eqImplicita}\n Coordinate:\n{self.Coordinate}'

a = float(input("Il valore x è "))
b = float(input("Il valore y è "))
c = float(input("Il termine noto è "))
y = (-a / b) 
z = (-c / b)
eq_1 = "y =" , y ,'x' , '+' , z
eq_2 = a,'x', '+', b,'y', '+' , c , = 0
coordinate_1 = (0,z)
coordinate_2 = (y,(y + z))
coordinate_3 = coordinate_1 , coordinate_2
equazione_uno = retta(eq_1, eq_2, coordinate_3) 
print(equazione_uno.equazione_esplicita())

    