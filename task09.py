'''Найти максимальный элемент среди минимальных элементов столбцов матрицы'''

from random import randint

matrix = [[randint(-100, 100) for i in range(6)] for i in range(6)]

for line in matrix:
    for i in line:
        print(f'{i:>4}', end='')
    print()

my_list = []

for i in range(len(matrix)):
    max_value = -100
    for j in range(len(matrix[i])):
        if matrix[j][i] > max_value:
            max_value = matrix[j][i]
    my_list.append(max_value)

print(f'Максимальный элемент каждого столбца: ')

for i in my_list:
    print(f'{i:>4}', end='')
    
'''Тот случай, когда сделал задание, а потом осознал, что я его неверно понял '''
