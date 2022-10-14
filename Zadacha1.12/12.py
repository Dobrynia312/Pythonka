print("Введите число:")
Chislo = int(input())
if Chislo // 100 != 0:
    while Chislo / 100 >= 10:
        Chislo = Chislo // 10
        print(Chislo)
    print(Chislo % 10)
else:
    print("Числа нет")