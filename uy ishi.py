x=int(input('massif nechta elementdan iborat bo\'lsin? '))
massif=[]

for n in range(x):
    massif.append(int(input(f"massifning {n+1}-elementini kiriting ")))

nechi=int(input('biron bir son kiriting  '))

for n in range(x):
    if nechi < massif[n]:
        print(massif[n])