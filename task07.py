'''В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.'''

from random import randint

my_list = [randint(-100, 100) for i in range(10)]
print(f'Исходный массив: \n {my_list}')

def find_min(a):
    min_value = my_list[0]
    min_value_ind = 0
    for ind in range(1, len(my_list)):
        if my_list[ind] < min_value:
            min_value, min_value_ind = my_list[ind], ind
    return my_list.pop(min_value_ind)

print(f'Минимальные числа списка: {find_min(my_list)} и {find_min(my_list)}')