voti = {
    "Mario": {"matematica": "6", "italiano": "6", "scienze": "7", "inglese": "4"}    
    "Giovanni": {"matematica": "4", "italiano": "6", "scienze": "5", "inglese": "7"}
    "Paola": {"matematica": "9", "italiano": "6", "scienze": "8", "inglese": "8"}
}

m = mean[voti.items('Mario')]
g = mean[voti.items('Giovanni')]
p = mean[voti.items('Paola')]

print("La media dei valori di Marco è " , m)
print("La media dei valori di Giovanni è " , g)
print("La media dei valori di Paola è " , p)