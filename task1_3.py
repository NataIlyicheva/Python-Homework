# "Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится)."

print ('Введите координату X:')
number1 = int(input())
print ('Введите координату Y:')
number2 = int(input())
if number1 == 0 and number2 == 0:
    print('введите число > или < 0')
if number1 > 0 and number2 > 0:
    print('Точка на четверти 1')
elif number1 < 0 and number2 > 0:
    print('Точка на четверти 2')
elif number1 < 0 and number2 < 0:
    print('Точка на четверти 3')
elif number1 > 0 and number2 < 0:
    print('Точка на четверти 4')
