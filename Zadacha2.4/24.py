print("Введите число:")
chislo = int(input())
a = (chislo//10000);
b = ((chislo%10000)//1000);
c = (((chislo%10000)%1000)//100);
d = ((((chislo%10000)%1000)%100)//10);
e = ((((chislo//10000)%1000)%100)%10);
obratnoechislo=(e*10000+d*1000+c*100+b*10+a);
if obratnoechislo==chislo:
    print("Polinom")
else:
    print("Ne Polinom")
