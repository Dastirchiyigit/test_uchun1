x=int(input('massif nechta elementdan iborat bo\'lsin? '))
massif=[]

for n in range(x):
    massif.append(int(input(f"massifning {n+1}-elementini kiriting ")))

nechi=int(input('qaysi elementni qidirmoqchisiz ?  '))


for n in range(x):
    if nechi == massif[n]:
        print(f"siz izlagan {nechi} soni massifning {n} - endex ekan")