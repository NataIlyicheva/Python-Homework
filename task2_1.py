# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Без работы с методами строк.

num = float(input('Введите вещественное число: '))
length = len(str(num))
new_num = num * 10 ** (length-1)
sum = 0
while new_num > 0:
    if new_num >= 0:
        sum = sum + new_num % 10
        new_num //= 10
print(int(sum))
