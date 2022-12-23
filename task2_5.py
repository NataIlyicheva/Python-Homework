# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

ran = range(int(input('укажите длину списка: ')))
mylist = list(ran)
print(mylist)
new_list = mylist
temp = 0
for i in mylist:
    for k in mylist:
        temp = mylist[i]
        mylist[i] = mylist[k]
        mylist[k] = temp
print(new_list)
