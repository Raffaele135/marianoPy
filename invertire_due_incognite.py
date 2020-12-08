print("Invertire il  valore di due variabili")
# primo metodo
x = float(input("x è "))
y = float(input("y è "))
tmp = x
x = y 
y = tmp
print("x è " , x , "y è " , y)

# secondo metodo con impostazione di una variabile

f = float(input("f è "))
g = float(input("g è "))
def swap(f,g):
    return(g,f)
result = swap(f,g)
print(result)