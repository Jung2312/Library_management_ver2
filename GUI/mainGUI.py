from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
    

# 메인 화면

main = Tk()
main.title("Library")
main.geometry("472x766+0+0")
main.resizable(False,False)
main.configure(bg='white')
fontExample = tkFont.Font(family='Noto Sans KR', size=14, weight="normal") # 기본 폰트 지정
fontExample2 = tkFont.Font(family='Noto Sans KR', size=12, weight="normal") # 기본 폰트 지정
fontExample3 = tkFont.Font(family='Noto Sans KR', size=18, weight="bold") # 보조 폰트 지정
fontExample4 = tkFont.Font(family='배달의민족 한나체 Pro', size=18, weight="normal") # 보조 폰트 지정

frame = tk.Frame(main)
frame.pack()

# 홈버튼
Hmenubtn = Menubutton(frame,text = "홈",font=fontExample3,bg='white', width=5)
Hmenubtn.grid(column=0, row=0)

homemenu = Menu(Hmenubtn,bg='white', tearoff=0)
Hmenubtn["menu"] = homemenu

# 도서 버튼
Bmenubtn = Menubutton(frame,text = "도서",font=fontExample3,bg='white', width=5)
Bmenubtn.grid(column=1, row=0)

bookmenu = Menu(Bmenubtn,bg='white', tearoff=0)
Bmenubtn["menu"] = bookmenu

bookmenu.add_command(label="도서등록",font=fontExample2)

# 회원 버튼
Umenubtn = Menubutton(frame,text = "회원",font=fontExample3,bg='white', width=5)
Umenubtn.grid(column=2, row=0)

usermenu = Menu(Umenubtn,bg='white', tearoff=0)
Umenubtn["menu"] = usermenu

usermenu.add_command(label="회원검색",font=fontExample2)
usermenu.add_command(label="회원등록",font=fontExample2)


# 대여 버튼
Rmenubtn = Menubutton(frame,text = "대여",font=fontExample3,bg='white', width=5)
Rmenubtn.grid(column=3, row=0)

rentmenu = Menu(Rmenubtn,bg='white', tearoff=0)
Rmenubtn["menu"] = rentmenu

rentmenu.add_command(label="도서대여",font=fontExample2)
rentmenu.add_command(label="도서반납",font=fontExample2)
Lib_image = PhotoImage(file ='C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\GUI\\program_image\\라이브러리로고.png')
Lib_label = tk.Label(main,image=Lib_image, bg='white')
Lib_label.pack(anchor=NW, padx=20)

main.mainloop()

    