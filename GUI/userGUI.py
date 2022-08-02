from tkinter import *
from tkinter.ttk import Treeview, Style
import tkinter.font as tkfont


class userGUI:
    def __init__(self):
        self.frame = Frame(main, bg="white", width=472, height=700)
        self.frame.pack(side="left",fill="both",expand=True)
        
        # 폰트 지정
        self.font14 = tkfont.Font(family='Noto Sans KR', size=14, weight="normal") # 기본 폰트 지정
        self.font12 = tkfont.Font(family='Noto Sans KR', size=12, weight="normal") # 기본 폰트 지정
        self.hanna18font = tkfont.Font(family='배달의민족 한나체 Pro', size=18, weight="normal") # 보조 폰트 지정
        self.hanna14font = tkfont.Font(family='배달의민족 한나체 Pro', size=14, weight="normal") # 보조 폰트 지정
    
    def user_search(self, image1,image2,image3,image4):
        
        # 라이브러리 로고
        Lib_label = Label(self.frame,image=image1, bg='white')
        Lib_label.pack(anchor=NW, padx=20)

        # 회원 검색 바
        U_shr_bar = Label(self.frame,image=image2)
        U_shr_bar.pack(anchor=NW, padx=20, pady=8)

        # 회원 검색 엔트리
        user_shr_Entry = Entry(self.frame, width=34, bd=0)
        user_shr_Entry.place(x=110, y=70)

        # 회원 검색 버튼
        Shr_button = Button(self.frame,image=image3, bg="white", bd=0)
        Shr_button.place(x=420, y=70)

        # 트리뷰 스타일 지정
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Noto Sans KR', 10)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=self.font12) # 트리뷰 제목 폰트
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # 트리뷰 생성
        user_tree = Treeview(self.frame, columns=["name","user_num","user_del","user_rent"], displaycolumns=["name","user_num","user_del","user_rent"], show='headings', height=20, style="mystyle.Treeview")
        user_tree.pack(pady=40)

        user_tree.column("name", width=90, anchor="center")
        user_tree.heading("name", text="이름", anchor="center")

        user_tree.column("user_num", width=140, anchor="center")
        user_tree.heading("user_num", text="전화번호", anchor="center")

        user_tree.column("user_del", width=91, anchor="center")
        user_tree.heading("user_del", text="탈퇴여부", anchor="center")

        user_tree.column("user_rent", width=91, anchor="center")
        user_tree.heading("user_rent", text="대여여부", anchor="center")

        # 도서 하단 블랙 바
        under_bg = Label(self.frame,image=image4, bg="white")
        under_bg.pack(side=BOTTOM)

    def user_append(self,image5, image6, image7, image8):
        name_label = Label(self.frame, text="이름", bg="white", font=self.hanna14font)
        name_label.place(x=60, y=20)
        name_entry=Entry(self.frame, font=self.hanna18font, width=10)
        name_entry.pack(anchor=NW, padx=110, pady=20)
        
        writer_label = Label(self.frame, text="저자", bg="white", font=self.hanna14font)
        writer_label.place(x=60, y=80)
        writer_entry=Entry(self.frame, font=self.font14, width=10)
        writer_entry.pack(anchor=NW, padx=110, pady=10)
        
        company_label = Label(self.frame, text="출판사", bg="white", font=self.hanna14font)
        company_label.place(x=240, y=80)
        company_entry=Entry(self.frame, font=self.font14, width=10)
        company_entry.place(x=300, y=80)
        
        line = Label(self.frame, image=image5, bg="white")
        line.pack(anchor=NW, padx=60, pady=20)
        
        image_entry = Label(self.frame, width=15, height=9)
        image_entry.pack(anchor=NW, padx=60, pady=20)
        
        phone_label = Label(self.frame, text="전화번호", bg="white", font=self.hanna14font)
        phone_label.place(x=220, y=210)
        phone_entry=Entry(self.frame, font=self.font14, width=10)
        phone_entry.place(x=300, y=210)
        
        birth_label = Label(self.frame, text="생년월일", bg="white", font=self.hanna14font)
        birth_label.place(x=220, y=270)
        birth_entry=Entry(self.frame, font=self.font14, width=10)
        birth_entry.place(x=300, y=270)
        
        email_label = Label(self.frame, text="이메일", bg="white", font=self.hanna14font)
        email_label.place(x=220, y=330)
        email_entry=Entry(self.frame, font=self.font14, width=10)
        email_entry.place(x=300, y=330)
        
        line2 = Label(self.frame, image=image5, bg="white")
        line2.pack(anchor=NW, padx=60, pady=20)
 

       # 트리뷰 생성
        '''
        회원 검색 시 클릭하면 나오는 상세 정보
        rent_label = Label(self.frame, text="대여도서", bg="white", font=self.hanna14font)
        rent_label.pack(anchor=NW, padx=60, pady=20)
        
        Urent_tree = Treeview(self.frame, columns=["ISBN","book_title","rent_day","return_Day"], displaycolumns=["ISBN","book_title","rent_day","return_Day"], show='headings', height=5, style="mystyle.Treeview")
        Urent_tree.pack()

        Urent_tree.column("ISBN", width=70, anchor="center")
        Urent_tree.heading("ISBN", text="ISBN", anchor="center")

        Urent_tree.column("book_title", width=100, anchor="center")
        Urent_tree.heading("book_title", text="제목", anchor="center")

        Urent_tree.column("rent_day", width=100, anchor="center")
        Urent_tree.heading("rent_day", text="대여일", anchor="center")

        Urent_tree.column("return_Day", width=100, anchor="center")
        Urent_tree.heading("return_Day", text="반납예정일", anchor="center")
        
        # 회원 수정 버튼
        mod_button = Button(self.frame,image=image6, bg="white", bd=0)
        mod_button.pack(anchor=NW, padx=120, pady=20)
        
        # 회원 삭제 버튼
        del_button = Button(self.frame,image=image7, bg="white", bd=0)
        del_button.place(x=210, y=640)
        
        # 회원 대여 버튼
        rent_button = Button(self.frame,image=image8, bg="white", bd=0)
        rent_button.place(x=300, y=640)
        '''
        
    def user_modifiy(self):
        pass
        
        
        
        
main = Tk()
main.title("Library")
main.geometry("472x700+0+0")
main.resizable(False,False)
main.configure(bg='white')
    
Lib_image = PhotoImage(file ="../GUI/program_image/라이브러리로고.png")
U_shr_image = PhotoImage(file ="../GUI/program_image/회원검색버튼.png")
Shr_button_image = PhotoImage(file ="../GUI/program_image/도서검색버튼.png")
under_image = PhotoImage(file ="../GUI/program_image/도서하단바.png")
line_image = PhotoImage(file ="../GUI/program_image/상세정보라인.png")
modButton_image = PhotoImage(file ="../GUI/program_image/도서상세수정버튼.png")
delButton_image = PhotoImage(file ="../GUI/program_image/도서상세삭제버튼.png")
rentButton_image = PhotoImage(file ="../GUI/program_image/도서상세대여버튼.png")

user_class = userGUI()

user_class.user_search(Lib_image,U_shr_image,Shr_button_image,under_image)
#user_class.user_append(line_image, modButton_image, delButton_image, rentButton_image)
#user_class.user_modifiy(line_image, modButton_image, delButton_image, rentButton_image)

main.mainloop() 