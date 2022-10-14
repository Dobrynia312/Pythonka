print("Введите номер дня недели, напоминаю их 7")
DenNedeli = int(input())
if 1 <= DenNedeli <= 5:
    print("Рабочий день")
elif 6 <= DenNedeli <= 7:
    print("Выходной день")  
else:
    print("Введен неправильный номер дня недели, напоминаю их 7")