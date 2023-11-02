from random import randint
print('2-мерный массив. A[n][m]. Количество элементов n * m')
n = int(input())
massiv = [[0 for i in range(n)] for j in range(n)] #задали матрицу из 0-вых элементов

for i in range(n):
    for j in range(n):
        massiv[i][j] = randint(1,9)#заполнение матрицы случ. числами

for i in range(n):
    for j in range(n):
        print(massiv[i][j], end=' ')
    print()#вывод матрицы

s = 0
for i in range(n):
    for j in range(n):
        s += massiv[i][j]
print(s)#сложение всех элементов матрицы
