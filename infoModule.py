def Info():
    name = inputName()
    sex = inputSex()
    email = inputEmail()
    birthDate = inputBirthDate()
    temp = (name,sex,email,birthDate)
    return temp

def inputInfo(infoList):
    print("고객 정보를 입력하세요")
    infoList.append(Info())

def updateInfo(infoCount,infoList):
    if infoCount == -1:
        print("현재 조회하고 있는 고객 정보가 없습니다.")
    else:
        print("수정할 정보로 입력하십시오")
        infoList[infoCount]=Info()
    return infoCount

def deleteInfo(infoCount,infoList):
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
    return infoCount

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

def hasNumber(inputString):     #입력된 문자열에 숫자가 있으면 True 없으면 False
    return any(one.isdigit() for one in inputString)