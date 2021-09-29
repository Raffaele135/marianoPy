class libro:

    libri_libreria = 0

    #Metodo Costruttore
    def __init__(self, titolo, autore, casa_editrice, anno_pubblicazione, genere):

        self.titolo = titolo
        self.autore = autore
        self.casa_editrice = casa_editrice
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere

        libro.libri_libreria +=1
    
    def scheda_libro(self):
        return f'Scheda libro:\n Titolo:{self.titolo}\n Autore:{self.autore}\n Casa Editrice:{self.casa_editrice}\n Anno di pubblicazione:{self.anno_pubblicazione}\n Genere:{self.genere}'
    
libro_uno = libro(" Il mondo perduto"," Arthur Conan Doyle"," La biblioteca dei ragazzi"," 1912"," Avventura")
print(libro_uno.scheda_libro())


        
