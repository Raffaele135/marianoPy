#software realizzato da Mariano e di Gennaro per il gruppo Mariano, di Gennaro, Greco, Iannuzzi0
import random 
lista_a = ["elefante", "maiale", "pollo"]
lista_b = ["bello", "brutto", "medio"]
lista_c = ["quaderno", "matita", "penna"]
 
def estrazione(lista): 
    p=random.randint(0,len(lista)-1) 
    x=lista[p] 
    lista.remove(x) 
    return x 
  
x=estrazione(lista_a) 
y=estrazione(lista_b)
z=estrazione(lista_c)

print (x)
print (x)
print (x)
print (y)
print (z)