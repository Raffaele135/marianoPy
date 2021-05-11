#software realizzato da Mariano e di Gennaro per il gruppo Mariano, di Gennaro, Greco, Iannuzzi0
from csv import reader

with open('versi.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_column = list(csv_reader)
nuova_lista_1 = []
nuova_lista_2 = []
nuova_lista_3 = []

for i in list_of_column:
    nuova_lista_1.append(i[0])
    nuova_lista_2.append(i[1])
    nuova_lista_3.append(i[2])

import random 
 
def estrazione(lista): 
    p=random.randint(0,len(lista)-1) 
    x=lista[p] 
    lista.remove(x) 
    return x 
  
x=estrazione(nuova_lista_1) 
y=estrazione(nuova_lista_2)
z=estrazione(nuova_lista_3)

print (x)
print (y)
print (z)