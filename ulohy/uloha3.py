# 2. pocitac generuje 100 cisel (200,800), 
# ak je ciferny sucet posledneho cisla parny, 
# vypiste cisla na 0. a 2. mieste, ak nie je parny tak na 1. a 3. mieste

import random
cisla=[]
for i in range(100):
    poslednecislo=random.randint(200,800)
    cisla.append(poslednecislo)

def vypocestcifsuctu(vstupnecislo):
    cifsucet=0
    for text in str(vstupnecislo):
        cifsucet += int(text)
    return cifsucet

if vypocestcifsuctu(poslednecislo)%2==0:
    print(cisla[0],cisla[2])
else:
    print(cisla[1],cisla[3])
