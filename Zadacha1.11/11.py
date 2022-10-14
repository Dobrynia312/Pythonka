print("Введите первое число:")
pervoeChislo = float(input())
print("Введите второе число:")
vtoroeChislo = float(input())
ostatok = pervoeChislo % vtoroeChislo
if pervoeChislo % vtoroeChislo == 0:
    print("Числа кратны")
else:
    print(f"Остаток от деления {ostatok}")
