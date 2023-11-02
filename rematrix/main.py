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
print()#табуляция
for i in range(n):
    for j in range(n):
        if i == j:
            massiv[i][j] = 20#на главной диагонали меняем элемент
for i in range(n):
    for j in range(n):
        print(massiv[i][j], end=' ')
    print()#опять выводим новый массив