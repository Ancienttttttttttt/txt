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

for i in range(n):
    for j in range(n):
        if massiv[i][j]%7 == 0:
            massiv[i][j] = 100#замена 7-ок на 100
print()
for i in range(n):
    for j in range(n):
        print(massiv[i][j], end=' ')
    print()