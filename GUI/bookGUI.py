from tkinter import *
from tkinter.ttk import Style as St, Treeview as Tree
import tkinter.font as tkfont


class bookGUI:
    def __init__(self):
        self.frame = Frame(main, bg='white')
        self.frame.pack(side='left', fill='both')

        self.sans14 = tkfont.Font(family='Noto Sans KR', size=14, weight="normal")
        self.sans12 = tkfont.Font(family='Noto Sans KR', size=12, weight="normal")
        self.hanna18 = tkfont.Font(family='배달의민족 한나체 Pro', size=18, weight="normal")

    def book_search(self, logo, s_bar, s_button, black):
        logo_label = Label(self.frame, image=logo, bg='white')  # 로고 사진
        logo_label.pack(anchor=NW, padx=20, pady=8)

        search_frame = Frame(self.frame, width=100, height=30, bg='white')  # 검색 바 프레임
        search_frame.pack(side='top')

        bar_label = Label(search_frame, image=s_bar)  # 검색 바 사진
        bar_label.pack(side='left', padx=10, pady=8)

        search_entry = Entry(self.frame, width=37, bd=0)  # 검색 엔트리
        search_entry.place(x=120, y=88)

        search_button = Button(search_frame, image=s_button, width=45, height=45, bg='white', bd=0)  # 검색 버튼
        search_button.pack(side='right')

        black_label = Label(self.frame, image=black, bg="white")  # 검은색 배경
        black_label.pack(side="bottom")

        style = St()  # 트리뷰 스타일
        style.configure("style.Treeview", highlightthickness=0, bd=1,
                        font=('Noto Sans KR', 10))
        style.configure("style.Treeview.Heading", font=self.sans12)  # 제목 폰트
        #style.layout("style.Treeview", [('style.Treeview.treearea', {'sticky': 'nswe'})])

        # 트리뷰 생성
        tree = Tree(self.frame, columns=['book_isbn', 'book_title', 'book_pub', 'book_rent'],
                    displaycolumns=['book_isbn', 'book_title', 'book_pub', 'book_rent'], show='headings', height=24,
                    style="style.Treeview")
        tree.pack(pady=30, padx=10)

        tree.column('book_isbn', width=120, minwidth=50, anchor="center")
        tree.heading('book_isbn', text='ISBN', anchor="center")

        tree.column('book_title', width=100, minwidth=100, anchor="center")
        tree.heading('book_title', text='제목', anchor="center")

        tree.column('book_pub', width=100, minwidth=50, anchor="center")
        tree.heading('book_pub', text='출판사', anchor="center")

        tree.column('book_rent', width=100, minwidth=50, anchor="center")
        tree.heading('book_rent', text='대여여부', anchor="center")


main = Tk()
main.title("도서관리프로그램")
main.geometry("472x766+0+0")
main.configure(bg='white')
main.resizable(False, False)  # 크기 고정

b_gui = bookGUI()
logo_I = PhotoImage(file='../GUI/program_image/라이브러리로고.png')
bar_I = PhotoImage(file='../GUI/program_image/도서검색바.png')
search_bt = PhotoImage(file='../GUI/program_image/도서검색버튼.png')
black = PhotoImage(file='../GUI/program_image/도서하단바.png')

b_gui.book_search(logo_I, bar_I, search_bt, black)

main.mainloop()
