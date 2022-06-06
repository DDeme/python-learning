##### Uloha1

```python
# 1.vstupuju cisla kym nevstupi 0,
# zisti pocet cifier posledneho cisla a vytlacte vsetky cisla,
# ktore maju rovnaky pocet cifier

cisla=[]
while True:
    poslednecislo=int(input("zadaj cislo: "))
    cisla.append(poslednecislo)
    if poslednecislo==0:
        break

dlzkaposlednehocisla=len(str(poslednecislo))

for cislo in cisla:
    if len(str(cislo))==dlzkaposlednehocisla:
        print(cislo)
```

##### Uloha2

```python
# 2. Vstupujú vety kým nevstúpi veta, ktorá je kratšia ako 5 znakov.
# Zistite koľko samohlások sa nachádza v poslednej vete a
# a vypíšte všetky vety ktorých počet samohlasok je väčší ako v poslednej vete
samohlasky="aieou"
vety=[]

def vypocetsamohlasok(vetavstup):
    pocetsamohlasok=0
    for pismenko in vetavstup:
        for samohlaska in samohlasky:
            if pismenko.lower() == samohlaska:
                pocetsamohlasok += 1
    return pocetsamohlasok

while True:
    poslednaveta=input("zadaj vetu: ")
    vety.append(poslednaveta)
    dlzkaposlednejvety=len(poslednaveta)
    if dlzkaposlednejvety < 5:
        break

pocetsamhlasokvposlednejvete=vypocetsamohlasok(poslednaveta)
for veta in vety:
    if vypocetsamohlasok(veta) > pocetsamhlasokvposlednejvete:
        print(veta)
```

##### Uloha3

```python
# 3. pocitac generuje 100 cisel (200,800),
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
```

##### Uloha4

```python
# 4. vstupuje 6 viet, zisti počet viet,
# v ktorých sa posledný znak poslednej vety nachádza trikrát

vety=[]
for i in range(6):
    poslednaveta=input("zadaj vetu:")
    vety.append(poslednaveta)

poslednepismeno=poslednaveta[len(poslednaveta)-1]

for veta in vety:
    i=0
    for pismenko in veta:
        if pismenko==poslednepismeno:
            i+=1
        if i==3:
            print(veta)
```
