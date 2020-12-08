stringa = dict(input("La parola è "))

alfabeto = ("abcdefghijklmnopqrstuvwxyz")
for lettera in alfabeto:
    if stringa.count(lettera):
        print(lettera , "=" , stringa.count(lettera))