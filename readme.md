# Pisomka z informatiky spolu s cviceniami

- [Premenne](#premenne)
- [Nacitanie vstupu](#nacitanie-vstupu)
- [Vypis vystupu](#vypis-vystupu)
- [Typy premennych](#typy-premennych)
- [Podmienky](#podmienky)
- [Porovnania pre podmienky if](#porovnania-pre-podmienky-if)
- [Boolean algebra](#boolean-algebra)
  - [Negacia](#negacia)
  - [And (Konjukcia)](#and--konjukcia-)
  - [Or (Disjunkcia)](#or--disjunkcia-)
- [Cykly](#cykly)
  - [While](#while)
- [Praca s typom pole](#praca-s-typom-pole)
  - [Pridavanie prvkov pola na jeho koniec](#pridavanie-prvkov-pola-na-jeho-koniec)
  - [Citanie z pola](#citanie-z-pola)
- [Funkcie](#funkcie)
- [Pomocne funkcie](#pomocne-funkcie)
- [Kniznica random](#kniznica-random)

### Premenne

Premenna uklada hodnotu do RAM pamate pre neskorsie pouzitie v programe. Pri skonceni programu sa RAM pamet vymaze.

### Nacitanie vstupu

Vstup z klavesnice programu

```python
premenna=input("zadaj cislo: ")
```

> Pozor: Premenna pri vstupe z klavesnice je vzdy typu string pozri int() a str() a uloha3

### Vypis vystupu

```python
print(premenna1, premenna2)
```

### Typy premennych

- z pohladu hodnoty
  - primitivne typy
    - boolean
    ```python
        premenna=True
        premenna=False
    ```
    - string
    ```python
    premenna="ahoj1"
    premenna="2022"
    ```
    - integer
    ```python
    premmna=11
    ```
  - polia
    mnozina prvkov
  ```python
  vety=[]
  vety=["ahoj", "svet"]
  vety=[2, 19]
  ```
- z pohladu pouzitia
  - konstanty (nemenia sa pocas behu programu)
  - premenne
- z pohladu rozsahu
  - lokalne
  - globalne

### Podmienky

Podmienka riadi cast programu ktori sa ma vykonat.

```python
    if podmienka:
        print("Pravdiva vetva programu")
    else:
        print("Nepravdiva vetva programu")
    print("Vypisem sa tak ci tak")
```

podmienka je typu boolean (True, False)
Nasledujuce casti kodu sa vykonaju ak je podmienka splnena. (True)

```python
    print("Pravdiva vetva programu")
```

Ak sa podmienka nieje splnena(False) vykona sa

```python
    print("Nepravdiva vetva programu")
```

Program pokracuje dalej

```python
   print("Vypisem sa tak ci tak")
```

### Porovnania pre podmienky if

> Pozor: Pri porovnavani vzdy porovnavame premenne rovnakeho typu integer s integer a string so string

```python
    "a" == "a" ## string == string ok  ✅
    0 == 0 ## integer == integer ok ✅
    "0" == "0" ## spravne porovnanie ✅
    0 != "0" ## nespravne porovnanie integer so string 🤦🏻 ❌
```

> Pozor: Pri porovnavani string porovnavame rovnaku velkost pismena. Na prevod pouzijeme metody lower() a upper()

```python
    "a" == "a" ## string == string male pismena lowercase ok ✅
    "A" == "A"= ## string == string velke pismena uppercase ok ✅
    "a" != "A" ## nespravne porovnanie male s velkym 🤦🏻 ❌
    "A" != "a" ## nespravne porovnanie velke s malym 🤦🏻 ❌
```

### Boolean algebra

Boolova algebra je algebrická štruktúra, ktorá modeluje vlastnosti množinových a logických operácií. Je nazvaná podľa írskeho matematika George Boolea.

Boolova algebra je abstraktný formálny systém obsahujúci množinu prvkov (a, b, c, ...), nad ktorou sú definované dve binárne operácie.

Viac na <https://sk.wikipedia.org/wiki/Boolova_algebra>

#### Negacia

Negacia je obratenie boolovej hodnoty true -> false, false -> true

```python
    if !podmienka1:
        print("podmiena1 je false")
```

#### And (Konjukcia)

a zaroven -> and

```python
    if podmienka1 and podmienka2:
        print("podmiena1 a podmienka2 su obidve true")
```

#### Or (Disjunkcia)

alebo -> or

```python
    if podmienka1 or podmienka2:
        print("aspon jedna z podmiena1 a podmienka2 su true")
```

### Cykly

Pre opakovanie urcitej casti programu pouzivame cyklus.
Cyklus sa opakuje dokym je splnena podmienka alebo je nutene ukonceny klauzulou `break`

#### While

```python
    pocitadlo=0
    while pocitadlo<5:
        pocitadlo=pocitadlo+1
        print(i)
```

Podmienka sa vykona 5x. Vystup programu bude 1,2,3,4,5

Pri podmienkach vieme pouzit takzvane nutene ukocenie `break`

```python
cisla=[]
while True:
    poslednecislo=int(input("zadaj cislo: "))
    cisla.append(poslednecislo)
    if poslednecislo==0:
        break
```

Program bude vykonavat blok kodu dokym neojde k zavolaniu break.

### Praca s typom pole

Prechadzanie hodnot v poli

```python
ovocia = ["apple", "banana", "cherry"]
for ovocie in ovocia:
  print(ovocie)
```

Cyklus sa automaticky ukonci po prejdeni celeho pola.

Vystupom bude vypis apple, banana, cherry

> Pozor: Rovnako vieme prechadzat aj typ string(retazec)

```python
veta="apple"
for pismenko in veta:
  print(pismenko)
```

Vystupom bude vypis a,p,p,l,e

#### Pridavanie prvkov pola na jeho koniec

```python
pole=[]
pole.append("prvok pola")
pole.append("iny prvok pola")
print(pole)
```

vysledkom bude ["prvok pola", "iny prvok pola"]

#### Citanie z pola

Kazdy prvok pola ma svoju adresu (index). Cisluje sa od 0.
Vieme ku nim pristupit nasledovne.

```python
ovocia=["apple", "banana", "cherry", "raspberry"]
ovocia[0] ## prvy prvok
ovocia[1] ## druhy prvok
len(ovocia) ## 4
len(ovocia)-1 ## adresa posledneho je 4 -1 kedze pocitame od 0
ovocia[len(ovocia)-1] ## posledny prvok ziskame dlzkov pola - 1
ovocia[len(ovocia)-2] ## prepodsledny prvok pola
```

### Funkcie

Funkcia je podprogram alebo zbierka prikazov ktore sa vykonaju pri jej volani. Umoznuje pouzit tu istu cast kodu viac krat.

Funkcia ma vstupne a vystupne parametere.

```python
def zamen(slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

print(zamen('kočka', 1, 'a')) # kačka
print(zamen('kačka', 2, 'p')) # kapka
```

Vypocet ciferneho suctu cisla

```python
def vypocestcifsuctu(vstupnecisio):
    cifsucet=0
    for text in str(vstupnecislo):
        cifsucet += int (text)
    return cifsucet

print(vypocestcifsuctu(112)) #4
print(vypocestcifsuctu(222)) #6
```

### Pomocne funkcie

```python
len("ahoj") # vypocita dlzku retazca alebo pola "ahoj" -> 4
str(123) # prevedie integer na string 123 -> "123"
int("12") # prevedie string na integer "12" -> 12
veta="ahoj"
veta.upper() # prevedie string na uppercase "AHOJ"
veta="AHoj"
veta.lower() #prevedie string na lowercase "ahoj"
```

### Kniznica random

```python
import random ## nezabudni na import na zaciatku suboru
cislo=random.randint(200,800) ## vyberie nahodne cislo z intervalu

```
