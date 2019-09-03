def information():
    info = {}
    info['name'] = input_name()
    info['gender'] = input_gender()
    info['email'] = input_email()
    info['age'] = input_age()

    return info

def input_name() :
    while True:
        name = input("이름을 입력하시오 : ")
        if any(i.isdigit() for i in name) == False:
            return name
        else:            
            print("글자만 입력하세요")

def input_gender() :    
    while True :
        mem_gender = input("성별을 입력하세요(남자면:M 여자면: F) : ").upper()
        if mem_gender == "M" or mem_gender == "F" :            
            return mem_gender
        else:
            print("성별을 M(m)이나 F(f)로 입력해주세요.")
            continue       
                
def input_email() :
    while True: 
        email = input("이메일을 입력하세요 : ")
        if email:
            return email

def input_age() :    
    while True:
        age = input("나이를 입력하세요 : ")
        if age.isdigit() and int(age) >=1 and int(age) <=150:
            return age 
        else:
            print("나이는 숫자만 입력 가능합니다.(1~150)")
            
def menual() :
    choice=input("""
    다음 중에 하실 일을 고르세요
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    A - 전체 고객 정보 조회
    """).upper()
    return choice

def printInfo(i):
    print("|{0:^8}|{1:^5}|{2:^25}|{3:^4}| ".format("name",'sex','email','age'))
    print("|{0:^8}|{1:^5}|{2:^25}|{3:^4}| ".format(member[i]['name'],member[i]['gender'],member[i]['email'],member[i]['age']))

def printAllInfo():
    print("|{0:^8}|{1:^5}|{2:^25}|{3:^4}| ".format("name",'sex','email','age'))
    for info in member:
        print("|{0:^8}|{1:^5}|{2:^25}|{3:^4}| ".format(info['name'],info['gender'],info['email'],info['age']))


member= []
i = 0

while True:
    choice = menual()
    if choice == 'I' :
        member.append(information())
        i = len(member) - 1

    elif choice == 'C' : 
        if len(member) == '0' :
            print("회원정보가 하나도 없습니다.")
        else :
            printInfo(i)
        
    elif choice == 'P' :
        if i == 0 :
            print("이전 회원 정보 없습니다.")
            printInfo(i)
        else :
            i = i - 1
            printInfo(i)

    elif choice == 'N':
        if i >= len(member)-1 :
            print("다음 회원 정보 없습니다.")
            printInfo(i)
        else :
            i = i+1
            printInfo(i)

    elif choice =='U' :
        printInfo(i)
        member[i] = information()
        printInfo(i)
    
    elif choice == 'A' :
        printAllInfo()

    elif choice == 'D' :
        if len(member) == 0:
            print("삭제할 정보가 없습니다.")
        else:
            del member[i]
            if i != 0:
                i = i-1