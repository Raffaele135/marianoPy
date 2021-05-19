#software realizzato da Mariano e di Gennaro per il gruppo Mariano, di Gennaro, Greco, Iannuzzi0
from csv import reader
import random
from tkinter import *
from tkinter import filedialog 
import tkinter as tk
from PIL import ImageTk, Image 

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
    print (x)
    print (y)
    print (z)

window = tk.Tk()
window.geometry("700x700")  
window.config(background = "dark blue") 

button_genera_grafico = tk.Button(window, text = "Genera grafico", width = 100, height = 2, command = software)
button_genera_grafico.pack()


window.mainloop()