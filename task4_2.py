number = int(input('Enter any number: '))
count = 2
my_list = []
while count > 1:
    if number % count == 0:
        my_list.append(count)
        number = number / count
    else:
        count += 1
    print(my_list)
