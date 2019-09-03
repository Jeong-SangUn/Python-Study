def hasNumber(inputString):
    return any(one.isdigit() for one in inputString)

def inputInfo():
    while True:
        name = input("이름을 입력하세요:")
        if len(name)>=2 and len(name)<=30 and hasNumber(name)==False:
            break
        print("이름은 2자이상 30자 이하의 문자만 입력할 수 있습니다.")
    while True:
        sex = input("성별을 입력하세요(남성:M,여성:F):").upper()
        if sex == "M" or sex == "F":
            break
        print("성별은 M(m)/F(f)만 올 수 있습니다.")
    while True:
        email = input("이메일을 입력하세요:")
        if email:
            break
    while True:
        birthDate = input("태어난 연도를 입력하시요(ex 1993):")
        if len(birthDate)==4 and birthDate.isdigit():
            break
        print("태어난 연도는 숫자 네글자만 올 수 있습니다.")
    tempTuple = (name,sex,email,birthDate)
    return tempTuple

infoList = []
infoCount = -1
while True:
    select = input('''
****************************************************************************************************************************************************
어떤 기능을 사용하시겠습니까
(I:고객정보입력 Q:프로그램종료 A:전체 고객정보 조회 C: 현재 고객정보 조회 P:이전 고객정보 조회 N:다음 고객정보 조회 U:현재 고객 정보 수정 D:현재 고객 정보 삭제)
****************************************************************************************************************************************************
''').upper()
    if select =="I":
        print("고객 정보를 입력하세요")
        infoList.append(inputInfo())

    elif select =="Q":
        print("프로그램을 종료합니다")
        break

    elif select =="C":
        if infoCount<0:
            print("조회 중인 고객 정보가 없습니다..")
            continue
        print("{0}번 고객님: {1}".format(infoCount+1,infoList[infoCount]))

    elif select =="N":
        if len(infoList) == infoCount+1:
            print("다음 고객 정보가 없습니다.")
            continue
        infoCount = infoCount+1
        print("{0}번 고객님: {1}".format(infoCount+1,infoList[infoCount]))

    elif select =="P":
        if infoCount<1:
            print("이전 고객 정보가 없습니다.")
            continue
        infoCount = infoCount-1
        print("{0}번 고객: {1}".format(infoCount+1,infoList[infoCount]))

    elif select =="A":
        if len(infoList) == 0:
            print("입력된 고객 정보가 없습니다.")
            continue
        count = 0
        for i in infoList:
            count = count + 1
            print("{0}번 고객님: {1}".format(count,i))

    elif select =="U":
        if infoCount == -1:
            print("현재 조회하고 있는 고객 정보가 없습니다.")
            continue
        print("현재 {0}번 고객님 정보: {1}".format(infoCount+1,infoList[infoCount]))
        print("수정할 정보로 입력하십시오")
        infoList[infoCount]=inputInfo()

    elif select =="D":
        if infoCount == -1:
            print("조회 중인 고객 정보가 없습니다.")
            continue
        if len(infoList) == 0:
            print("현재 고객 정보가 없습니다")
            continue
        del infoList[infoCount]
        print("현재 고객 정보를 삭제합니다")
        if len(infoList) == infoCount + 1:
            print("마지막 페이지 고객 정보를 삭제하셨습니다. 이전 고객 정보를 불러 옵니다.")
            if infoCount == -1:
                print("이전 고객 정보가 없습니다. 모든 고객 정보를 삭제하였습니다.")
            continue
        print("다음 고객 정보를 불러옵니다")

    else:
        print("선택지를 다시 확인해주세요!")