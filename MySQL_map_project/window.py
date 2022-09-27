from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *

def func_exit():
    window.quit()
    window.destroy()

def click_button1():
    messagebox.showinfo("버튼1 클릭", "버튼1을 클릭했습니다.")

def click_button2():
    messagebox.showinfo("버튼2 클릭", "버튼2을 클릭했습니다.")
    
def click_button3():
    value = str(askinteger("숫자 입력창", "나이를 입력하세요 (0-99)", minvalue=0, maxvalue=99))
    return value

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_cascade(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)


button1 = Button(window, text='버튼1', command=click_button1)
button2 = Button(window, text='버튼2', command=click_button2)
button3, value = Button(window, text='버튼3', command=click_button3)

button1.pack(side=LEFT, fill=Y, padx=10, pady=10)
button2.pack(side=LEFT, fill=Y, padx=10, pady=10)
button3.pack(side=LEFT, fill=Y, padx=10, pady=10)

upFrame = Frame(window)
upFrame.pack()
editBox = Entry(upFrame, width=10, bg='gray')
editBox.pack(padx=20, pady=20)

downFrame = Frame(window)
downFrame.pack()
listbox = Listbox(downFrame, bg='lightgray');
listbox.pack()
listbox.insert(END, '나이')
listbox.insert(END, value)

window.mainloop()