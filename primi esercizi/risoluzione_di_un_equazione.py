print("Risoluzione di un equazione data  nella forma: ax+b=0")
import math  
a = float(input("a è "))
b = float(input("b è "))
if a == 0 :
    print("L'equazione è impossibile")
elif b == 0 :
    print("L'equazione è indeterminata")
else:
    x = -b / a 
    print("La soluzione dell'eqiazione è:" , x)
