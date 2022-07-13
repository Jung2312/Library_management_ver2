import pandas as pd
import pymysql
from sqlalchemy import create_engine

class book_class:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='0000', db='book', charset='utf-8')
        cur = self.conn.cursor()
        cur.execute('ALTER TABLE members AUTO_INCREMENT=1') # id 초기화
        cur.execute('select * from table') # 데이터 읽기 작업, 커서에 select로 조회한 결과 한꺼번에 저장 (select 칼럼명 from 테이블명)
        self.df = pd.DataFrame(cur.fetchall()) # 전체 나열 함수를 이용해 나열한 데이터로 데이터 프레임 생성

    def book_search(self): # 도서 검색
        title = '나나나'
        if (self.df['book_title']==title).any():
            search = self.df[self.df['book_title'] == title]
            ser_print = search[['book_isbn', 'book_title', 'book_pub', 'book_rent']] # 도서 isbn, 제목, 출판사, 대여여부
        else: # 같은 제목의 도서가 없을 때
            print('존재하지 않은 도서입니다.\n')

    def book_append(self): # 도서 등록
        if not ((self.df['book_isbn'] == '1234').any()):
            input_data = pd.DataFrame({'book_title':['데미안'], 'book_author':['헤르만 헤세'], 'book_pub':['민용사'], 'book_isbn':[9791165341909],
                          'book_price':[11200], 'book_link':['https://ssl.yes24.com/dMyCart/CartMain'], 'book_ex':['데미안을 통해..'],
                          'book_photo':[None], 'book_del':[False], 'book_rent':[False]})
            self.df = pd.concat([self.df, input_data])
            print(self.df)
            self.df.to_csv('book_list.csv', encoding='utf-8')
            # sql = 'INSERT INTO table VALUES('요기에', '값을', '집어', '넣음')
        else:
            print('이미 등록되어있는 도서입니다.\n')

        self.conn.close() # 데베 모두 사용 후 연결한 데베 닫기
        csv_df = pd.read_csv('../Data_design/CSV/book_list.csv', encoding='utf-8')
        # 데이터베이스 접속 엔진
        engine = create_engine('mysql+pymysql://username:password@localhost:3306/book_db', encoding='utf-8') # MySQL은 mysql+pymysql://username:password@host:3306/database
        self.conn = engine.connect()
        csv_df.to_sql('table', con=engine, if_exists='append', index=False) # if_exists='append' : 기존 테이블에 데이터 추가, 'fail' : 기존 테이블이 있으면 아무 일도 안함, 'replace' : 기존 테이블이 있으면 삭제하고 다시 만들어서 새로 데이터 넣음

    def book_modify(self): # 도서 수정
        self.conn.close()
        '''csv_df = pd.read_csv('../Data_design/CSV/book_list.csv', encoding='utf-8')
        # 데이터베이스 접속 엔진
        engine = create_engine('mysql+pymysql://username:password@localhost:3306/book_db',
                               encoding='utf-8')  # MySQL은 mysql+pymysql://username:password@host:3306/database
        self.conn = engine.connect()
        csv_df.to_sql('table', con=engine, if_exists='replace',
                      index=False)'''
        cur = self.conn.cursor()
        SQL = """
        UPDATE table SET
        book_title='데미안미안'
        """
        cur.execute(SQL)
        self.conn.commit()

    def book_delete(self): # 도서 삭제
        self.conn.close()
        cur = self.conn.cursor()
        SQL = """
                DELETE FROM table WHERE PRODUST_CODE='데미안'
                """
        cur.execute(SQL)
        self.conn.commit()

    def book_rent(self): # 도서 대여
        cur = self.conn.cursor()
        SQL = """
                UPDATE table SET
                book_rent='True'
                """
        cur.execute(SQL)
        self.conn.commit()


    def book_return(self): # 도서 반납
        cur = self.conn.cursor()
        SQL = """
                UPDATE table SET
                book_title='False'
                """
        cur.execute(SQL)
        self.conn.commit()
