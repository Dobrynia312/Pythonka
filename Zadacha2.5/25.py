import math


print("Введите X1:")
x1 = int(input())
print("Введите Y1:")
y1 = int(input())
print("Введите Z1:")
z1 = int(input())
print("Введите X2:")
x2 = int(input())
print("Введите Y2:")
y2 = int(input())
print("Введите Z2:")
z2 = int(input())
res = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2 ) + ((z2 - z1)**2))
print(f"Расстояние между точками: {res}")