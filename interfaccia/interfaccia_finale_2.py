from tkinter import *
from tkinter import filedialog 
import tkinter as tk
from PIL import ImageTk, Image 


# definisci la funzione genera grafico
def genera_grafico():
    import string
    import numpy as np
    import matplotlib.pyplot as plt

    #apriamo il file in lettura
    f = open(text_box.get(), "r") 
    coordX = []
    coordY = []

    for riga in f:
        valori = str(riga)  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

    f.close()  

    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.savefig("grafico.png", dpi=100, facecolor = "#f1f1f1")
    img = ImageTk.PhotoImage(Image.open("grafico.png")) 
    panel = tk.Label(window, image = img) 
    panel.pack(side = "bottom", expand = "yes") 



window = tk.Tk()
window.title('Seleziona file e genera grafico')
window.geometry("700x700")  
window.config(background = "dark blue") 

text_box = tk.Entry(window, text="")
text_box.pack()

button_genera_grafico = tk.Button(window, text = "Genera grafico", width = 100, height = 2, command = genera_grafico)
button_genera_grafico.pack()

button_exit = tk.Button(window, text = "Esci", command = exit)
button_exit.pack()

window.mainloop() 