# Creare una lista di 100 numeri e restituirli in output
from random import randint
f = open("testo.txt", 'w')
testo = ""
for riga in range(100):
    for elemento in range(1):
        testo = testo + str(randint(1,100))
        testo = testo + "\n"

print(testo)
f.write(testo)
f.close()