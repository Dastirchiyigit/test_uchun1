x=int(input('n = '))
massif=[]

for n in range(x):
    massif.append(int(input(f"{n+1}- ")))

massif.sort()
for n in range(x-1):
    son = (massif[n+1]-massif[n])
    if son // 2 ==0 and son // 3 == 0:
        print(f"{massif[n]} va {massif[n+1]}")