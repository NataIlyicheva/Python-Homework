num = int(input('Введите длину списка: '))
nums_list = list(range(num))
new_list = []
res_list = []
print(nums_list) # [0123456]
for i in range(num):
    from random import randrange
    new_list.append(randrange(num))
print(new_list) # [6201345]

for i in new_list:
    count = 0
    for x in new_list:
        if i == x:
            count += 1
    if count == 1:
        res_list.append(i)
print(res_list)
