infoList = []
infoCount = -1

def hasNumber(inputString):     #입력된 문자열에 숫자가 있으면 True 없으면 False
    return any(one.isdigit() for one in inputString)

def Info():
    name = inputName()
    sex = inputSex()
    email = inputEmail()
    birthDate = inputBirthDate()
    temp = (name,sex,email,birthDate)
    return temp

def inputInfo():
    global infoList
    print("고객 정보를 입력하세요")
    infoList.append(Info())

def updateInfo():
    global infoList
    global infoCount
    if infoCount == -1:
        print("현재 조회하고 있는 고객 정보가 없습니다.")
    else:
        printInfo()
        print("수정할 정보로 입력하십시오")
        infoList[infoCount]=Info()

def deleteInfo():
    global infoList
    global infoCount

    if len(infoList) == 0:
        print("고객 정보가 없습니다")

    elif infoCount == -1:
        print("조회 중인 고객 정보가 없습니다.")

    else:
        del infoList[infoCount]
        print("현재 고객 정보를 삭제합니다")
        if len(infoList) == infoCount:
            print("마지막 페이지 고객 정보를 삭제하셨습니다. 이전 고객 정보를 불러 옵니다.")
            infoCount -= 1
            if infoCount == -1:
                print("이전 고객 정보가 없습니다. 모든 고객 정보를 삭제하였습니다.")
        else:
            print("다음 고객 정보를 불러옵니다")

def inputName():
    while True:
        name = input("이름을 입력하세요:")
        if len(name)>=2 and len(name)<=30 and hasNumber(name)==False:
            return name
        print("이름은 2자이상 30자 이하의 문자만 입력할 수 있습니다.")

def inputSex():
    while True:
        sex = input("성별을 입력하세요(남성:M,여성:F):").upper()
        if sex == "M" or sex == "F":
            return sex
        print("성별은 M(m)/F(f)만 올 수 있습니다.")

def inputEmail():
    while True:
        email = input("이메일을 입력하세요:")
        if email:
            return email

def inputBirthDate():
    while True:
        birthDate = input("태어난 연도를 입력하시요(ex 1993):")
        if len(birthDate)==4 and birthDate.isdigit():
            return birthDate
        print("태어난 연도는 숫자 네글자만 올 수 있습니다.")

def nowInfo():
    global infoCount
    if infoCount<0:
        print("조회 중인 고객 정보가 없습니다..")
    else:
        printInfo()

def nextInfo():
    global infoCount
    global infoList
    if len(infoList) == infoCount+1:
            print("다음 고객 정보가 없습니다.")
    else:
        infoCount = infoCount+1
        printInfo() 

def preInfo():
    global infoCount
    global infoList
    if infoCount<1:
            print("이전 고객 정보가 없습니다.")
    else:
        infoCount = infoCount-1
        printInfo() 

def printInfo():
    global infoList
    global infoCount
    
    if len(infoList) == 0:
        print("입력된 고객 정보가 없습니다.")
    else:
        print("|No|{0:^10}|{1:^5}|{2:^25}|{3:^9}|".format("Name","Sex","E-mail","BirthYear"))
        tempTuple = infoList[infoCount]
        print("|{0:<2}|{1:^10}|{2:^5}|{3:^25}|{4:^9}|".format(infoCount+1,tempTuple[0],tempTuple[1],tempTuple[2],tempTuple[3]))

def printAllInfo():
    global infoList
    if len(infoList) == 0:
        print("입력된 고객 정보가 없습니다.")
    else:
        count = 0
        print("|No|{0:^10}|{1:^5}|{2:^25}|{3:^9}|".format("Name","Sex","E-mail","BirthYear"))
        for member in infoList:
            count += 1
            print("|{0:^2}|{1:^10}|{2:^5}|{3:^25}|{4:^9}|".format(count,member[0],member[1],member[2],member[3]))

def input_manual():
    select = input('''
******************************************************************************************************
어떤 기능을 사용하시겠습니까
I:고객정보입력          Q:프로그램종료          A:전체 고객정보 조회
C:현재 고객정보 조회    P:이전 고객정보 조회    N:다음 고객정보 조회 
U:현재 고객 정보 수정   D:현재 고객 정보 삭제
******************************************************************************************************
''').upper()
    return select

def main():
    while True:
        select = input_manual() #메뉴얼 출력 및 동작 입력

        if select =="I":    #고객 정보 입력
            inputInfo()

        elif select =="C":  #현재 고객 정보 출력
            nowInfo()

        elif select =="N":  #다음 고객 정보 출력
            nextInfo()
            
        elif select =="P":  #이전 고객 정보 출력
            preInfo()
    
        elif select =="A":  #모든 고객 정보 출력
            printAllInfo()

        elif select =="U":  #현재 고객 정보 수정
            updateInfo()

        elif select =="D":  #현재 고객 정보 삭제
            deleteInfo()

        elif select =="Q":  #프로그램 종료
            print("프로그램을 종료합니다")
            break   

        else:               #제공하지 않는 기능_예외처리
            print("선택지를 다시 확인해주세요!")

if __name__ == "__main__":
    main()