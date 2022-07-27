from cProfile import label
from email.mime import image
from tkinter import *
import tkinter.font as tkFont
import tkinter as tk

main = Tk()
main.title("Library")
main.geometry("472x766+0+0")
main.resizable(False,False)
main.configure(bg='white')

frame = tk.Frame(main)
frame.pack()

Lib_image = PhotoImage(file ='../GUI/program_image/라이브러리로고.png')
Lib_label = tk.Label(frame,image=Lib_image, bg='white')
Lib_label.pack(anchor=NW, padx=20)

label2 = tk.Label(frame,image=Lib_image)
label2.place(x = 30, y = 40)

Entry2 = Entry(main)
Entry2.pack()
main.mainloop()