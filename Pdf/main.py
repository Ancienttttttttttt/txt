from tkinter import *
from tkinter import filedialog as fd
from pdf2docx import parse
import pathlib

root = Tk()
root.title('PDF в Word')
root.geometry('400x300+300+300')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')

def convert():
    pdf_file = ePath.get()
    word_file = pathlib.Path(pdf_file)
    word_file = word_file.stem + '.docx'
    parse(pdf_file, word_file)
    Label(root, text='Конвертация завершена', fg='lime', bg= 'black', font='Arial 15 bold').pack(pady=10)

Button(root, text='Выбрать PDF файл', font='Arial 15 bold', fg='lime', bg='black', command=callback).pack(pady=10)
lbPath = Label(root, text='Путь к файлу', fg='lime', bg= 'black', font='Arial 15 bold')
lbPath.pack()

ePath = Entry(root, width=50, state='readonly')
ePath.pack(pady=10)

btnConvert = Button(root, text='Конвертировать', fg='lime', bg= 'black', font='Arial 15 bold', command=convert).pack(pady=10)

root.mainloop()