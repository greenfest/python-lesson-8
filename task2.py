# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import numpy as np 

matrix = np.random.randint(1, 10, size=(4, 4))
print(matrix)
print("-"*12)

sumOfDiagonal = 0
count = 0

for i in range(0,len(matrix[0])):
    sumOfDiagonal += matrix[i][i]
 

for i in range(0,len(matrix[0])):
    if (matrix[i].sum() > sumOfDiagonal):
        count += 1
        print(f'Сумма элементов строки {i+1} = {matrix[i].sum()} превосходит сумму главной диагонали = {sumOfDiagonal}')

if count == 0: print("Ни одна из строк по сумме элементов НЕ превосходит сумму главной диагонали матрицы")
