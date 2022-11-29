# ex17.py : 명화 감상하기
from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry('400x400')

# 함수 선언
def func_open() :
    filename = askopenfilename(parent=window, filetypes=(('GIF 파일', '.gif'), ('모든 파일', '*.*')))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()


photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)  # config, configure 둘 다 사용 가능
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=func_exit)


window.mainloop()
