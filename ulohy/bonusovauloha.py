#Vstupuju vety, kym nevstupi veta práznda.Vypiste vietky vety, ktoré sa zacinaju na pismeno, ktorym sa zacina predposledna veta

vety=[]
while True:
    poslednaveta=input("zadaj vetu:")
    if poslednaveta=="":
        break
    else:
        vety.append(poslednaveta)

predposlednaveta=vety[len(vety)-1]
prvepismenopredposlednejvety=predposlednaveta[0]

for veta in vety:
    if veta[0]==prvepismenopredposlednejvety and veta != predposlednaveta:
        print(veta)