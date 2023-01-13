from decimal import Decimal


num = Decimal(input('Введите число: '))
accuracy = input('Введите формат округления: ')
num = num.quantize(Decimal(accuracy))
print(num)