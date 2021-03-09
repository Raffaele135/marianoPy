#Chiedi all'utente una lista di 5 numeri interi e salvali in un Array. 
#Ordina la lista e restituiscila in output nell'ordine inverso.

"Scrivi 5 numeri interi da 1 a 9"
array = list(input())
array.sort()
array.reverse()
print(array)