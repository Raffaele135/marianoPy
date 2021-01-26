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

    '''
    si potrebbe usare il metodo readlines 
    per ottenere una lista di righe del file

    stampiamo la prima riga
    print(f.readline()) 

    possiamo fare un ciclo e prendere riga per riga 
    Python, tuttavia, mette a disposizione la possibilità
    di inserire riga per riga all'interno di una varabile, 
    utilizzando un ciclo di for

    valori = str(riga)

    permette di salvare in "valori" il contenuto della riga estratta
    '''
    coordX = []
    coordY = []

    # da notare che posso fare un ciclo all'interno di un file
    # direttamente sulle righe

    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()

# genera la finestra                                                                                        
window = Tk() 

# inserisci il titolo della finestra
window.title('Seleziona file e genera grafico')

# decidi la grandezza della finestra
window.geometry("700x700") 

# inserisci il colore della finestra
window.config(background = "dark blue") 

# crea l'etichetta esplora file
label_file_explorer = Label(window,  
                            text = "Insrisci un file e genera un grafico", 
                            width = 100, height = 4,  
                            fg = "black")    
       
button_explore = Button(window,  
                        text = "Inserisci file", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Esci", 
                     command = exit)  

button_genera_grafico = Button(window,  
                        text = "Genera grafico", 
                        command = genera_grafico) 

label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 4) 

button_genera_grafico.grid(column = 1, row = 3)
   
window.mainloop() 