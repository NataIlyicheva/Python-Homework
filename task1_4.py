# "4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y). 
# *Пример:* - 1 -> x > 0, y > 0           - 8 -> нет такой четверти"

print ('Введите номер четверти плоскости координат:')
number = int(input())
if number == 1:
    print('x > 0, y > 0')
elif number == 2:
    print('x < 0, y > 0')
elif number == 3:
    print('x < 0, y < 0')
elif number == 4:
    print('x > 0, y < 0')
if number <= 0 or number > 4:
    print('такой четверти нет')
