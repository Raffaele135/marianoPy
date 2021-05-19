from csv import reader

with open('versi.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_column = list(csv_reader)
nuova_lista_1 = []
nuova_lista_2 = []
nuova_lista_3 = []

for i in list_of_column:
    nuova_lista_1.append(i[0])
    nuova_lista_2.append(i[1])
    nuova_lista_3.append(i[2])

print (nuova_lista_1)
print (nuova_lista_2)
print (nuova_lista_3)