import json, os

def manual(self):
    select = input('''
******************************************************************************************************
어떤 기능을 사용하시겠습니까
I:고객정보입력          Q:프로그램종료          A:전체 고객정보 조회
C:현재 고객정보 조회    P:이전 고객정보 조회    N:다음 고객정보 조회 
U:현재 고객 정보 수정   D:현재 고객 정보 삭제   S:고객 정보 저장
******************************************************************************************************
''').upper()
    return select

def exe(self):

    while True:
        select = self.manual()

        if select == "I":       #고객 정보 입력
            self.inputinfo()

        elif select == "C":
            self.nowinfo(self.page, self.customlist)

        elif select == "N":
            self.page = self.nextinfo(self.page, self.customlist)
        
        elif select == "P":
            self.page = self.preinfo(self.page, self.customlist)

        elif select == "A":
            self.printallinfo(self.customlist)

        elif select == "U":
            self.updateinfo(self.page)
        
        elif select == "D":
            self.page = self.deleteinfo(self.page)

        elif select == "S":
            self.saveData()

        elif select == "Q":
            self.saveData()
            break

        else:
            print("명령어를 확인해주세요")

def updateinfo(self, page):
    if len(self.customlist)==0:
        print("수정할 고객 정보가 없습니다.")
    else:
        self.printinfo(page,self.customlist)
        print("수정할 정보를 입력해주세요")
        name = self.inputname()
        gender = self.inputgender()
        email = self.inputemail()
        year = self.inputyear()
        dic = {"name":name, "gender":gender, "email":email, "year":year}
    self.customlist[page] = dic

def deleteinfo(self, page):
    if len(self.customlist)==0:
        print("삭제할 고객 정보가 없습니다.")
    else:
        lastpage = len(self.customlist)
        del self.customlist[page]
        print("현재 고객 정보 삭제가 완료되었습니다")
        
        if len(self.customlist)==0:
            print("리스트에 고객 정보가 없습니다.")
        elif lastpage == page + 1:
            print("마지막 고객 정보입니다. 이전 고객 정보를 불러옵니다")
            page = page - 1
        else:
            print("다음 고객 정보를 불러옵니다")
    return page

def saveData(self):
    print("현재 고객 리스트를 저장하였습니다.")
    with open('./data.json','wt') as file:
        json.dump(self.customlist,file,indent=4)

def loadData(self):
    if os.path.exists('./data.json'):    
        with open('./data.json','rt') as file:
                self.customlist=json.load(file)

def allinfo(self, list):
    print("모든 고객 정보를 출력합니다.")
    self.printallinfo(list)

def nowinfo(self, page, list):
    if len(list) == 0 :
        print("현재 저장된 고객 정보가 없습니다.")
    else :
        self.printinfo(page, list)

def nextinfo(self, page, list):
    if len(list) == 0 :
        print("현재 저장된 고객 정보가 없습니다.")
    elif len(list) < page + 2 :
        print("다음 페이지가 존재하지 않습니다.")
    else :
        page = page + 1
        self.printinfo(page, list)
    return page

def preinfo(self, page, list):
    if len(list) == 0 :
        print("현재 저장된 고객 정보가 없습니다.")
    elif page == 0 :
        print("이전 페이지가 존재하지 않습니다.")
    else :
        page = page - 1
        self.printinfo(page, list)
    return page

def inputinfo(self):
    name = self.inputname()
    gender = self.inputgender()
    email = self.inputemail()
    year = self.inputyear()
    dic = {"name":name, "gender":gender, "email":email, "year":year}

    self.customlist.append(dic)

def printinfo(self, page, list):
    m = list[page]
    print("|page|{0:^15}|{1:^6}|{2:^30}|{3:^6}|".format("name","gender","email","year"))
    print("|{0:>4}|{1:^15}|{2:^6}|{3:^30}|{4:^6}|".format(page+1,m["name"],m["gender"],m["email"],m["year"]))

def printallinfo(self, list):
    count=0
    print("|page|{0:^15}|{1:^6}|{2:^30}|{3:^6}|".format("name","gender","email","year"))
    for m in list:
        count = count + 1
        print("|{0:>4}|{1:^15}|{2:^6}|{3:^30}|{4:^6}|".format(count,m["name"],m["gender"],m["email"],m["year"]))

def inputname(self):
    while True:
        name = input("name:")
        if len(name)>=2 and len(name)<=30 and self.hasNumber(name)==False:
            return name
        print("이름은 2자이상 30자 이하의 문자만 입력할 수 있습니다.")

def inputgender(self):
    while True:
        gender = input("성별을 입력하세요(남성:M,여성:F):").upper()
        if gender == "M" or gender == "F":
            return gender
        print("성별은 M(m)/F(f)만 올 수 있습니다.")

def inputemail(self):
    while True:
        email = input("이메일을 입력하세요:")
        if email:
            return email

def inputyear(self):
    while True:
        year = input("태어난 연도를 입력하시요(ex 1993):")
        if len(year)==4 and year.isdigit():
            return year
        print("태어난 연도는 숫자 네글자만 올 수 있습니다.")

def hasNumber(self,inputString):     #입력된 문자열에 숫자가 있으면 True 없으면 False
    return any(one.isdigit() for one in inputString)

def __init__(self):
    self.customlist = []
    self.page = 0
    self.loadData()
    self.exe()              #고객 관리 시스템 실행
