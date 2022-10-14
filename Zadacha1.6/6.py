print("Введите число:")
Chislo = int(input())
i = 0
while i <= Chislo:
    if i % 2 == 0:
        print(i)
        i+=1
    elif i%2!=0:
        i+=1