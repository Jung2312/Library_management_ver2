import pandas as pd


class book_class:
    def __init__(self):
        self.df = pd.read_csv('../Data_design/CSV/book_list.csv', encoding='utf-8')

    def book_search(self):  # 도서 검색
        title = '나나나'
        if (self.df['book_title'] == title).any():
            search = self.df[self.df['book_title'] == title]
            ser_print = search[['book_isbn', 'book_title', 'book_pub', 'book_rent']]  # 도서 isbn, 제목, 출판사, 대여여부
        else:  # 같은 제목의 도서가 없을 때
            print('존재하지 않은 도서입니다.\n')

    def book_append(self):  # 도서 등록
        if not ((self.df['book_isbn'] == '1234').any()):
            input_data = pd.DataFrame(
                {'book_title': ['데미안'], 'book_author': ['헤르만 헤세'], 'book_pub': ['민용사'], 'book_isbn': [9791165341909],
                 'book_price': [11200], 'book_link': ['https://ssl.yes24.com/dMyCart/CartMain'],
                 'book_ex': ['데미안을 통해..'],
                 'book_photo': [None], 'book_del': [False], 'book_rent': [False]})
            self.df = pd.concat([self.df, input_data])
            self.df.to_csv('../Data_design/CSV/book_list.csv', encoding='utf-8', index=False)
        else:
            print('이미 등록되어있는 도서입니다.\n')

    def book_modify(self):  # 도서 수정
        isbn_ = '9788982814471'
        if not ((self.df['book_isbn'] == '9791165341909').any()):
            input_data = self.df.loc[
                self.df.book_isbn == '9791165341909', ('book_title', 'book_author', 'book_pub', 'book_isbn')] = \
                ('연금술사', '파울로 코엘료', '문학동네', '9788982814471')
            self.df.to_csv('../Data_design/CSV/book_list.csv', encoding='utf-8', index=False)
        else:
            print('이미 등록되어있는 도서입니다.\n')

    def book_delete(self):  # 도서 삭제
        isbn_ = '9788982814471'
        if (self.df['book_isbn'] == isbn_).any():
            self.df = self.df.drop([isbn_])
            self.df.to_csv('../Data_design/CSV/book_list.csv', encoding='utf-8', index=False)
            print('도서를 삭제합니다.\n')
        else:
            print('존재하지 않는 도서입니다..\n')

    def book_rentn(self):  # 도서 대여
        isbn_ = (self.df['book_isbn'] == '9788982814471').any()
        if isbn_:
            if (isbn_['book_rent'] == False).any():
                input_data = self.df.loc[self.df.book_isbn == '9788982814471', 'book_rent'] = True
                self.df.to_csv('../Data_design/CSV/book_list.csv', encoding='utf-8', index=False)
            else:
                print('이미 대여 중인 도서입니다.')
        else:
            print('존재하지 않은 도서입니다.\n')

    def book_return(self):  # 도서 반납
        isbn_ = (self.df['book_isbn'] == '9788982814471').any()
        if isbn_:
            if (isbn_['book_rent'] == True).any():
                input_data = self.df.loc[self.df.book_isbn == '9788982814471', 'book_rent'] = False
                self.df.to_csv('../Data_design/CSV/book_list.csv', encoding='utf-8', index=False)
            else:
                print('대여 중이지 않은 도서입니다.')
        else:
            print('존재하지 않은 도서입니다.\n')


book = book_class()
print(book.book_append())
