from tkinter import *
from tkinter import filedialog 

# definisci la funzione inserisci file
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
   
    label_file_explorer.configure(text="File aperto: "+filename) 

# definisci la funzione genera grafico
def genera_grafico():
    import string
    import numpy as np
    import matplotlib.pyplot as plt

    #apriamo il file in lettura
    f = open(filename, 'r')

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
window.geometry("700x500") 

# inserisci il colore della finestra
window.config(background = "dark blue") 

# crea l'etichetta esplora file
label_file_explorer = Label(window,  
                            text = "Insrisci un file e genera un grafico", 
                            width = 100, height = 2,  
                            fg = "black")    
       
button_explore = Button(window,  
                        text = "Inserisci file", 
                         width = 100, height = 2,
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Esci", 
                     command = exit)  

button_genera_grafico = Button(window,  
                        text = "Genera grafico", 
                         width = 100, height = 2,
                        command = genera_grafico) 

label_file_explorer.grid(column = 1, row = 2) 
   
button_explore.grid(column = 1, row = 1) 
   
button_exit.grid(column = 1,row = 4) 

button_genera_grafico.grid(column = 1, row = 3)
   
window.mainloop() 