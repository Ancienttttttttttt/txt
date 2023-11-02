import tkinter as tk

WIN_H = 700
WIN_W = 1200
PANEL_H = WIN_H
PANEL_W = 200
CANVAS_H = WIN_H
CANVAS_W = WIN_W-PANEL_W

win = tk.Tk()
win.title('Генератор графиков функций')
win.config(width=WIN_W, height=WIN_H)
win.resizable(False, False)

panel = tk.Frame(win, width=PANEL_W, height=PANEL_H, bd=4, relief=tk.GROOVE)
panel.place(x=0, y=0, width=PANEL_W, height=PANEL_H)

canvas = tk.Canvas(win, width=CANVAS_W, height=CANVAS_H, bg='#012')
canvas.place(x=PANEL_W, y=0, width=CANVAS_W, height=CANVAS_H)

def draw_axis(x_left, x_right, y_bottom, y_top):
    #Центр координат
    cx = -x_left/(x_right - x_left)*CANVAS_W
    cy = y_top/(y_top - y_bottom)*CANVAS_H

    #отрисовка верт и гориз линий графика
    canvas.create_line(0, cy, CANVAS_W, cy, fill='white')
    canvas.create_line(cx, 0, cx, CANVAS_H, fill='white')

    dx = CANVAS_W/(x_right - x_left)
    dy = CANVAS_H/(y_top - y_bottom)

    x = x_left
    while x <= x_right:
        x_step = (x_right - x_left) / 12
        x_canvas = (x - x_left) * dx
        canvas.create_line(x_canvas, cy-3, x_canvas, cy+3, fill='white')
        canvas.create_text(x_canvas, cy+15, text=str(round(x, 2)),
                           font= "Verdana 9", fill='white')
        x += x_step
    # отрисовка текста на линии y

    y = y_top
    while y >= y_bottom:
        y_step = (y_top - y_bottom) / 12
        y_canvas = (y - y_top) * dy
        canvas.create_line(cx - 3, -y_canvas, cx+3, -y_canvas,fill='white')
        canvas.create_text(cx+25, -y_canvas, text=str(round(y, 2)),
                           font="Verdana 9", fill='white')
        y -= y_step
    return dx, dy
#получаем ряд чисел в диапозоне от x_left до x_right
def frange(begin, end, step):
    x = begin
    t = []
    while x <= end:
        t.append(x)
        x += step
    return t

#функция квадратичной параболы
def parabola_generator(x_tmp, a, b, c):
    y_tmp = []
    for x in x_tmp:
        y = a*x**2 + b*x + c
        y_tmp.append(y)
    return y_tmp

#нанесение координат на холст
def graph_dot(x_tmp, y_tmp, color):
    dot_list = []
    i = 0
    for x in x_tmp:
        y = y_tmp[i]
        x = (x - x_tmp[0]) * dx
        y = (y - y_top) * dy
        dot = canvas.create_oval(x-1, -(y-1), x+1, -(y+1),
                           fill=color, outline=color)
        dot_list.append(dot)
        i += 1
    return dot_list

#обработчик нажатия кнопки изменения графика
def parabola_redraw():
    global y_parabola
    global parabola
    for dot in parabola:
        canvas.delete(dot)
    a = float(ent1.get())
    b = float(ent2.get())
    c = float(ent3.get())
    y_parabola = parabola_generator(x_list, a, b, c)
    parabola = graph_dot(x_list, y_parabola, 'yellow')

x_left, x_right = -6, 12
y_bottom, y_top = -10, 20
dx, dy = draw_axis(x_left, x_right, y_bottom, y_top)
x_list = frange(x_left, x_right, 0.01)
y_parabola = parabola_generator(x_list, 0.1, 0, 0)
parabola = graph_dot(x_list, y_parabola, 'yellow')

lab01 = tk.Label(panel, text="Парабола")
lab01.place(x=0, y=0, width=190, height=30)
lab1 = tk.Label(panel, text="a:")
lab1.place(x=5, y=30, width=10, height=30)
lab2 = tk.Label(panel, text="b:")
lab2.place(x=5, y=60, width=10, height=30)
lab3 = tk.Label(panel, text="c:")
lab3.place(x=5, y=90, width=10, height=30)

ent1 = tk.Entry(panel, bd=2)
ent1.place(x=20, y=30, width=45)
ent1.insert(0, "2")
ent2 = tk.Entry(panel, bd=2)
ent2.place(x=20, y=60, width=45)
ent2.insert(0, "-9")
ent3 = tk.Entry(panel, bd= 2)
ent3.place(x=20, y=90, width=45)
ent3.insert(0, "0")

but1 = tk.Button(panel, text="Отобразить", command=parabola_redraw)
but1.place(x=80, y=50, width=100, height=30)

win.mainloop()