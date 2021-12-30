'''В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.'''

from random import randint

my_list = [randint(-100, 100) for i in range(10)]
print(f'Исходный массив: \n {my_list}')

max_value_ind = 0
max_value = -100

for ind in range(len(my_list)):
    if my_list[ind] < 0 and my_list[ind] > max_value:
        max_value, max_value_ind = my_list[ind], ind

print(f'Максимальный отрицательный элемент {max_value} \n стоит в позиции {max_value_ind}')
