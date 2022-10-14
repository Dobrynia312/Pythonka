print("Введите номер четверти:")
chetvert = int(input())
if chetvert <= 4:
        if chetvert== 1:
            print("0<X<Бесконечность, 0<Y<Бесконечность")
        elif chetvert== 2:
            print("-Бесконечность<X<0, 0<Y<Бесконечность")
        elif chetvert== 3:
            print("-Бесконечность<X<0, -Бесконечность<Y<0")
        elif chetvert== 4:
            print("0<X<Бесконечность, -Бесконечность<Y<0")

else:
    print("Введен неправильный номер четверти, напоминаю их 4")
