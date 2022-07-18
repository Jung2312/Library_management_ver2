import pandas as pd

class userclass:
    def __init__(self):
        self.Userdf = pd.read_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv",encoding = 'utf-8')
        
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
        if (self.Userdf["user_num"]=="010-4877-5678").any():
            print("존재하는 회원입니다\n")
        else:
            input_user = {"user_name":["박길동"], "user_birth":[19990101],"user_sex":[False],"user_num":["010-1234-5678"],"user_email":["ghd@naver.com"],"user_del":[False],"user_photo":[None],"user_rent":[0]}
            input_user = pd.DataFrame(input_user)
            self.Userdf = pd.concat([self.Userdf,input_user])
            self.Userdf.to_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv", encoding='utf-8-sig', index = False)
        
    def user_modify(self):
        # 회원 수정
        u_num = "010-1234-5678"
        mod_num = "010-8887-7847"
        if (self.Userdf['user_num']==u_num).any():
            user_mod = self.Userdf[self.Userdf["user_name"] == u_num]
            if (user_mod["user_num"]==u_num).any() or ((self.Userdf["user_num"]==mod_num).any())==False:
                self.Userdf.loc[self.Userdf.user_num == u_num, ("user_name", "user_birth", "user_sex","user_num","user_email","user_photo")] = ("김길순","19970404", True, mod_num,"rlftns@daum.net",None)  # 전화번호 기준으로 수정하고자 하는 컬럼의 데이터 수정
                self.Userdf.to_csv("C:\\Users\\alswj\\OneDrive\\문서\\Library_management_ver2\\Data_design\\CSV\\user_list.csv", encoding='utf-8-sig', index = False)
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
        else:
            print("존재하는 회원입니다\n")
            
            
user = userclass()
user.user_append()
