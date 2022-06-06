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