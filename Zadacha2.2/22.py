print("Введите первое число:")
pervoeChislo = float(input())
print("Введите второе число:")
vtoroeChislo = float(input())
kvadrat = pow(vtoroeChislo, 2)
kvadrat2 = pow(pervoeChislo, 2)
if pervoeChislo == kvadrat:
    print("Первое число квадрат второго")
elif vtoroeChislo == kvadrat2:
    print("Второе число квадрат первого")
else:
    print("Одно число не квадрат другого")
