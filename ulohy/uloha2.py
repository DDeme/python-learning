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