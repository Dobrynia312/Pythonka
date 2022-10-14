print("Введите номер дня недели, напоминаю их 7")
DenNedeli = int(input())
if DenNedeli <= 7:
        if DenNedeli==1:
            print("Понедельник")           
        elif DenNedeli==2:
            print("Вторник")        
        elif DenNedeli==3:
            print("Среда")        
        elif DenNedeli==4:
            print("Четверг")        
        elif DenNedeli==5:
            print("Пятница")       
        elif DenNedeli==6:
            print("Суббота")       
        elif DenNedeli==7:
            print("Воскресенье")
else:
    print("Введен неправильный номер дня недели, напоминаю их 7")
