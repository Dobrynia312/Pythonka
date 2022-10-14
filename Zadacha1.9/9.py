from random import randint


numberA = randint(1,100)
print(numberA)
vtoroechislo = (numberA % 10)
pervoechislo = (numberA // 10)
print(pervoechislo)
print(vtoroechislo)
print(max(pervoechislo, vtoroechislo))