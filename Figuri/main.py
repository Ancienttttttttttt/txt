import turtle

window = turtle.Screen()#отрисовка окна
window.title("Turtle!")#заголовок
turtle.shape("turtle")#отрисовка черепашки

#рисование квадрата
n = 4
for i in range(n):
    turtle.forward(100)#смещение черепашки на 100 пикселей
    turtle.right(90)#черепашка поварачивается на 90 градусов


#рисование круга
turtle.penup()
turtle.back(50)
turtle.pendown()
turtle.circle(100)#радиус круга

#рисование треугольника
n = 3#переменная для сторон треугольника
angle = 60#черепашка поварачивается на 60 градусов
turtle.penup()
turtle.forward(300)
turtle.pendown()
for i in range(n):
    turtle.forward(100)
    turtle.left(180 - angle)#вычитаем из 180 угол поворота


window.exitonclick()#закрытие окна
