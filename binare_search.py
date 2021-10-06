def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

x=int(input('massif nechta elementdan iborat bo\'lsin? '))
massif=[]

for n in range(x):
    massif.append(int(input(f"massifning {n}-elementini kiriting ")))

massif.sort()
izla=int(input("qaysi elementni izlayapsiz ? "))
print(binary_search(massif,izla))