import pymysql
import pandas as pd
from sqlalchemy import create_engine

class userclass:
    def __init__(self):
        self.Userdf = pd.read_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv",encoding = 'utf-8')
        
    def sql_csv(self):
        sql_df = pd.read_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv",encoding = 'utf-8')
        # sqlalchemy를 사용해 원하는 database에 csv파일 저장
        engine = create_engine("mysql+pymysql://root:"+"2312"+"@localhost:3306/book_db?charset=utf8", encoding = "utf-8") # sql 연결
        self.conn = engine.connect()
        sql_df.to_sql("user_table", con = engine, if_exists = 'replace', index = False) # 새로운 csv 데이터로 덮어쓰기
        self.conn.close() # csv를 sql에 전송하기 위해 전의 db 연결 끊음
        
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
        if (self.Userdf["user_num"]=="010-1234-5678").any():
            print("존재하는 회원입니다\n")
        else:
            input_user = {"user_name":["홍길동"], "user_birth":[19990101],"user_sex":[False],"user_num":["010-1234-5678"],"user_email":["ghd@naver.com"],"user_del":[False],"user_photo":[None],"user_rent":[0]}
            input_user = pd.DataFrame(input_user)
            self.Userdf = pd.concat([self.Userdf,input_user])
            self.Userdf.to_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv", encoding='utf-8-sig', index = False)
            userclass().sql_csv()
        
    def user_modify(self):
        # 회원 수정
        u_num = "010-1234-5678"
        mod_num = "010-8887-7847"
        if (self.Userdf['user_num']==u_num).any():
            user_mod = self.Userdf[self.Userdf["user_name"] == u_num]
            if (user_mod["user_num"]==u_num).any() or ((self.Userdf["user_num"]==mod_num).any())==False:
                self.Userdf.loc[self.Userdf.user_num == u_num, ("user_name", "user_birth", "user_sex","user_num","user_email","user_photo")] = ("김길순","19970404", True, mod_num,"rlftns@daum.net",None)  # 전화번호 기준으로 수정하고자 하는 컬럼의 데이터 수정
                self.Userdf.to_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv", encoding='utf-8-sig', index = False)
                userclass().sql_csv()
            else:
                print("동일한 전화번호가 존재합니다.\n")
        else:
            print("존재하는 회원입니다\n")
    
    def user_delete(self):
        # 회원 삭제
        u_num = "010-4444-5555"
        if (self.Userdf['user_num']==u_num).any():
            self.Userdf = self.Userdf[self.Userdf.user_num != u_num]
            self.Userdf.to_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv", encoding='utf-8-sig', index = False)
            userclass().sql_csv()
        else:
            print("존재하는 회원입니다\n")
            
            
user = userclass()
user.user_append()
