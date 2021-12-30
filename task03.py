'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

from random import randint

my_list = [randint(-100, 100) for i in range(10)]
print(f'Исходный массив: \n {my_list}')

min_value = max_value = my_list[0]
min_value_ind = max_value_ind = 0

for ind in range(1, len(my_list)):
    if my_list[ind] > max_value:
        max_value, max_value_ind = my_list[ind], ind
    elif my_list[ind] < min_value:
        min_value, min_value_ind = my_list[ind], ind

my_list[min_value_ind], my_list[max_value_ind] = my_list[max_value_ind], my_list[min_value_ind]
print(f'Массив с измененными местами max и min элементами: \n {my_list}')