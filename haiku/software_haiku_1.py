#software realizzato da Mariano e di Gennaro per il gruppo Mariano, di Gennaro, Greco, Iannuzzi0
from csv import reader
import random
import tkinter as tk

def software():
    # Estrattore casuale
    def estrazione(lista): 
        p=random.randint(0,len(lista)-1) 
        x=lista[p] 
        lista.remove(x) 
        return x 

    #Estrazione casuale del csv
    lista_csv = ['versi.csv']
    a = estrazione(lista_csv)

    #Apertura e lettura del file csv
    with open( a , 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_column = list(csv_reader)
    nuova_lista_1 = []
    nuova_lista_2 = []
    nuova_lista_3 = []
    for i in list_of_column: 
        nuova_lista_1.append(i[0])
        nuova_lista_2.append(i[1])
        nuova_lista_3.append(i[2])

    #Estrazione elementi da csv
    x=estrazione(nuova_lista_1) 
    y=estrazione(nuova_lista_2)
    z=estrazione(nuova_lista_3)


window = tk.Tk()
window.geometry("600x400")
window.title("Generatore di haiku")
window.resizable(False, False)
window.configure(background="light blue")


first_button = tk.Button(text="premi il bottone", command = software)
first_button.grid(row=1, column=5)





window.mainloop()