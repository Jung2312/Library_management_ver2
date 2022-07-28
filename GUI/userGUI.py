from tkinter import *
from tkinter.ttk import Treeview, Style

class userGUI:
    def user_search(image1,image2,image3,image4):
        frame = Frame(main, bg="white")
        frame.pack(side="left",fill="both",expand=True)

        # 라이브러리 로고
        Lib_label = Label(frame,image=image1, bg='white')
        Lib_label.pack(anchor=NW, padx=20)

        # 회원 검색 바
        U_shr_bar = Label(frame,image=image2)
        U_shr_bar.pack(anchor=NW, padx=20, pady=8)

        # 회원 검색 엔트린
        user_shr_Entry = Entry(main, width=34, bd=0)
        user_shr_Entry.place(x=110, y=70)

        # 회원 검색 버튼
        Shr_button = Button(frame,image=image3, bg="white", bd=0)
        Shr_button.place(x=420, y=70)

        # 트리뷰 스타일 지정
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Noto Sans KR', 10)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Noto Sans KR', 12)) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # 트리뷰 생성
        user_tree = Treeview(frame, columns=["name","user_num","user_del","user_rent"], displaycolumns=["name","user_num","user_del","user_rent"], show='headings', height=20, style="mystyle.Treeview")
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
        under_bg = Label(frame,image=image4, bg="white")
        under_bg.pack(side=BOTTOM)


main = Tk()
main.title("Library")
main.geometry("472x766+0+0")
main.resizable(False,False)
main.configure(bg='white')

Lib_image = PhotoImage(file ="GUI/program_image/라이브러리로고.png")
U_shr_image = PhotoImage(file ="GUI/program_image/회원검색버튼.png")
Shr_button_image = PhotoImage(file ="GUI/program_image/도서검색버튼.png")
under_image = PhotoImage(file ="GUI/program_image/도서하단바.png")

userGUI.user_search(Lib_image,U_shr_image,Shr_button_image,under_image)

main.mainloop() 