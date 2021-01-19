from tkinter import *
from tkinter import filedialog 


       
   
    

# definisci la funzione genera grafico
def genera_grafico():
    import string
    import numpy as np
    import matplotlib.pyplot as plt

    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                         "*.*"))) 

    f = filename

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
    plt.show()

# creare la finestra
window = Tk() 

# inserisci il titolo della finestra
window.title('Seleziona file e genera grafico')

# decidi la grandezza della finestra
window.geometry("700x5<00") 

# inserisci il colore della finestra
window.config(background = "dark blue") 
 
       
button_exit = Button(window,  
                     text = "Esci", 
                     command = exit)  

button_genera_grafico = Button(window,  
                        text = "Genera grafico", 
                         width = 100, height = 2,
                        command = genera_grafico) 


button_exit.grid(column = 1,row = 4) 

button_genera_grafico.grid(column = 1, row = 3)
   
window.mainloop() 