print("Введите число:")
Chislo = int(input())
tretiechislo = ((Chislo % 100) % 10)
vtoroechislo = ((Chislo % 100) // 10)
pervoechislo = (Chislo // 100);
res = (pervoechislo * 10) + tretiechislo;
print(f"Первая цифра {pervoechislo}, вторая цифра {vtoroechislo}, третья цифра {tretiechislo}")
print(f"{pervoechislo}{tretiechislo}")
print(res)