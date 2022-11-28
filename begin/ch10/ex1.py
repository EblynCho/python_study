# ex1.py

# tkinter : 윈도우 담당 모듈
from tkinter import *

window = Tk()
window.title('윈도 창 연습')
window.geometry('400x100')
# window.resizable(width=False, height=False)

label1 = Label(window, text='COOKBOOK~~Python을')
label2 = Label(window, text='열심히', font=('궁서체', 30), fg='blue')
label3 = Label(window, text='공부 중입니다.', bg='magenta', width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
