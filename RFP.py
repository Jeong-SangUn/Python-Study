infoList = []
infoCount = -1
while True:
    select = input('''
------------------------------------------------------------------------------------------------------------------------------------------
어떤 기능을 사용하시겠습니까
(I:고객정보입력 Q:프로그램종료 A:전체 고객정보 조회 C: 현재 고객정보 조회 P:다음 고객정보 조회 N:이전 고객정보 조회 D:현재 고객 정보 삭제)
------------------------------------------------------------------------------------------------------------------------------------------
''').upper()
    if select =="I":
        print("고객 정보를 입력하세요")
        name = input("이름을 입력하세요:")
        sex = input("성별을 입력하세요(남성:M,여성:F):")
        email = input("이메일을 입력하세요:")
        birthDate = int(input("태어난 연도를 입력하시요(ex 1993):"))
        infoList.append((name,sex,email,birthDate))
    elif select =="Q":
        print("프로그램을 종료합니다")
        break
    elif select =="C":
        if infoCount<0:
            print("현재 고객 정보가 없습니다.")
            continue
        print("{0}번 고객님: {1}".format(infoCount+1,infoList[infoCount]))
    elif select =="P":
        if len(infoList) == infoCount+1:
            print("다음 고객 정보가 없습니다.")
            continue
        infoCount = infoCount+1
        print("{0}번 고객님: {1}".format(infoCount+1,infoList[infoCount]))
    elif select =="N":
        if infoCount<1:
            print("이전 고객 정보가 없습니다.")
            continue
        infoCount = infoCount-1
        print("{0}번 고객님: {1}".format(infoCount+1,infoList[infoCount]))
    elif select =="A":
        count = 0
        for i in infoList:
            count = count + 1
            print("{0}번 고객님: {1}".format(count,i))
    elif select =="U":
        print("현재 {0}번 고객님 정보: {1}".format(infoCount+1,infoList[infoCount]))
        print("수정할 정보로 입력하십시오")
        name = input("이름을 입력하세요:")
        sex = input("성별을 입력하세요(남성:M,여성:F):")
        email = input("이메일을 입력하세요:")
        birthDate = int(input("태어난 연도를 입력하시요(ex 1993):"))
        infoList[infoCount]=(name,sex,email,birthDate)
    elif select =="D":
        if len(infoList) == 0:
            print("현재 고객 정보가 없습니다")
            continue
        del infoList[infoCount]
        print("현재 고객 정보를 삭제합니다")
        if len(infoList) == infoCount:
            print("마지막 고객 정보를 삭제하셨습니다. 이전 고객 정보를 불러옵니다")
            infoCount = infoCount - 1
            continue
        print("다음 고객 정보를 불러옵니다")
    else:
        print("선택지를 다시 확인해주세요!")
            