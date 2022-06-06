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
