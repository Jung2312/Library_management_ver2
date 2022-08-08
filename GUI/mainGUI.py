from tkinter import *
import tkinter.font as tkFont
import tkinter as tk


class main_home():
    def __init__(self):
        self.Lib_image = PhotoImage(file ='../GUI/program_image/라이브러리로고.png')
        self.B_shr_image = PhotoImage(file ="../GUI/program_image/도서검색바.png")
        self.Shr_button_image = PhotoImage(file ="../GUI/program_image/도서검색버튼.png")
        
        self.book_rent_ima = PhotoImage(file ='../GUI/program_image/도서 대여버튼.png')
        self.book_app_ima = PhotoImage(file ='../GUI/program_image/도서등록버튼.png')
        
        self.book_re_ima = PhotoImage(file ='../GUI/program_image/도서반납버튼.png')
        self.user_app_ima = PhotoImage(file ='../GUI/program_image/회원등록버튼.png')
        
        self.Lib_txt_image = PhotoImage(file ='../GUI/program_image/도서관리메인로고.png')
        self.under_bar = PhotoImage(file ='../GUI/program_image/도서하단바.png')
        
        self.frame = Frame(main, bg="white", width=472, height=700)
        self.frame.pack(side="left",fill="both",expand=True)
        
    def home(self):
        Lib_label = tk.Label(self.frame, image=self.Lib_image, bg='white')
        Lib_label.pack(anchor=NW, padx=20)
        
        # 도서 검색 바
        B_shr_bar = Label(self.frame,image=self.B_shr_image)
        B_shr_bar.pack(anchor=NW, padx=20, pady=8)

        # 도서 검색 엔트리
        book_shr_Entry = Entry(self.frame, width=34, bd=0)
        book_shr_Entry.place(x=110, y=70)

        # 도서 검색 버튼
        Shr_button = Button(self.frame,image=self.Shr_button_image, bg="white", bd=0)
        Shr_button.place(x=420, y=70)
        
        # 도서 대여 메뉴로 가는 버튼
        book_rent_butt = Button(self.frame, image=self.book_rent_ima, bg="white", bd=0)
        book_rent_butt.place(x=20, y=140)
        
        # 도서 등록 메뉴로 가는 버튼
        book_app_butt = Button(self.frame, image=self.book_app_ima, bg="white", bd=0)
        book_app_butt.place(x=20, y=324)
        
        # 도서 반납 메뉴로 가는 버튼
        book_re_butt = Button(self.frame, image=self.book_re_ima, bg="white", bd=0)
        book_re_butt.place(x=236, y=190)
        
        # 회원 등록 메뉴로 가는 버튼
        user_app_butt = Button(self.frame, image=self.user_app_ima, bg="white", bd=0)
        user_app_butt.place(x=236, y=374)
        
        Lib_txt = Label(image=self.Lib_txt_image , bg="white")
        Lib_txt.place(x=140, y=580)
        
        under_image = Label(image=self.under_bar, bg="black")
        under_image.place(y=720)
        
        
        
        

# 메인 화면
# 카테고리는 메인에, 나머지 버튼은 프레임에
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

main_class = main_home()
main_class.home()

main.mainloop()

    