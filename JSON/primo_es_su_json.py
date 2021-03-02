import json

libreria_string = '''
{
    "libreria": [
        {
            "titolo": "20000 leghe sotto i mari",
            "autore": "Jules Verne",
            "genere": "Fantascienza",
            "editore": "Pierre-Jules Hetzel",
            "data di pubblicazione": "20 Giugno 1870"
        },
        {
            "titolo": "I viaggi di Gulliver",
            "autore": "Jonathan Swift",
            "genere": "Avventura",
            "editore": "Benjamin Motte",
            "data di pubblicazione": "28 Ottobre 1726"
        },
        {
            "titolo": "Viaggio al centro della Terra",
            "autore": "Jules Verne",
            "genere": "Fantascienza, Avventura",
            "editore": "Pierre-Jules Hetzel",
            "data di pubblicazione": "1864"
        },
        {
            "titolo": "Dracula",
            "autore": "Bram Stoker",
            "genere": "Horror",
            "editore": "Robinson",
            "data di pubblicazione": "26 Maggio 1897"
        },
        {
            "titolo": "Robinson Crouse",
            "autore": "Daniel Defoe",
            "genere": "Avventura",
            "editore": "Paternoster Row",
            "data di pubblicazione": "25 Aprile 1719"
        },
        {
            "titolo": "Frankenstein",
            "autore": "Mary Shelly",
            "genere": "Horror",
            "editore": "",
            "data di pubblicazione": "1823"
        },
        {
            "titolo": "Il piccolo principe",
            "autore": "Antoine de Saint-Exupéry",
            "genere": "Favola",
            "editore": "",
            "data di pubblicazione": "6 Aprile 1943"
        },
        {
            "titolo": "Il ritratto di Doryan Grey",
            "autore": "Oscar Wilde",
            "genere": "Fantascienza",
            "editore": "",
            "data di pubblicazione": "1890-1891"
        },
        {
            "titolo": "L'isola del tesoro",
            "autore": "Robert Luis Stevenson",
            "genere": "Avventura",
            "editore": "Cassell"
            "data di pubblicazione": "1883"
        },
        {
            "titolo": "Moby Dick",
            "autore": "Herman Melville",
            "genere": "Fantascienza, Avventura",
            "editore": "",
            "data di pubblicazione": "1851"
        }
    ]
}
'''

data = json.loads(libreria_string)
print(type(data))
print(data)