# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in  6;     out [2.0, 2.25, 2.37, 2.441, 2.488, 2.522];      14.071

number = int(input('Введите длину списка: '))
my_list = []
sum = 0
for n in range (1, number + 1):
    num_a = (1 + 1 / n) ** n
    my_list.append(round(num_a, 3))
    sum += num_a
print(my_list, (round(sum, 3)))
