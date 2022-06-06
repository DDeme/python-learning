# 

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