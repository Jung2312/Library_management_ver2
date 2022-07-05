import pymysql
import pandas as pd
from sqlalchemy import create_engine

class userclass:
    def __init__(self):
        # sql 데이터 불러옴
        self.conn = pymysql.connect(host="localhost", user="root", password="2312", db="book_db", charset="utf8", autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        curs = self.conn.cursor()
        sql = "select * from user_table"
        curs.execute(sql)
        input_data = curs.fetchall()

        self.Userdf = pd.DataFrame(input_data) # sql 데이터로 데이터 프레임 생성
        print(self.Userdf)
        self.Userdf.to_csv('user_list.csv', encoding='utf-8-sig', index = False)
    def user_searh(self):
        # 회원 검색
        u_name = "김길동"

        if (self.Userdf['user_name']==u_name).any():
            user_srh = self.Userdf[self.Userdf["user_name"] == u_name]
            user_srh = user_srh[['user_name','user_num','user_del','user_rent']]
        else:
            print("존재하지 않는 회원입니다.\n")
        
    def user_append(self):
        # 회원 등록
        if ((self.Userdf['user_num']=="010-1234-5678").any())==False:
            input_user = {"user_name":["홍길동"], "user_birth":[19990101],"user_sex":[False],"user_num":["010-4444-5555"],"user_email":["ghd@naver.com"],"user_del":[False],"user_photo":[None],"user_rent":[0]}
            input_user = pd.DataFrame(input_user)
            self.Userdf = pd.concat([self.Userdf,input_user])
            self.Userdf.to_csv('user_list.csv', encoding='utf-8-sig', index = False)
            print(self.Userdf)
        else:
            print("존재하는 회원입니다\n")

        self.conn.close() # csv를 sql에 전송하기 위해 전의 db 연결 끊음
        
        sql_df = pd.read_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv",encoding = 'utf-8')
        # sqlalchemy를 사용해 원하는 database에 csv파일 저장
        engine = create_engine("mysql+pymysql://root:"+"2312"+"@localhost:3306/book_db?charset=utf8", encoding = "utf-8") # sql 연결
        self.conn = engine.connect()
        sql_df.to_sql("user_table", con = engine, if_exists = 'replace', index = False) # 새로운 csv 데이터로 덮어쓰기
        
    def user_modify(self):
        self.conn.close() # sql 연결 끊음






book = userclass()
book.user_searh()
