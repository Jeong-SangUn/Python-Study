class Printinfo:   
    def printInfo(self,infoCount,infoList):
        if len(infoList) == 0:
            print("입력된 고객 정보가 없습니다.")
        else:
            print("|No|{0:^10}|{1:^5}|{2:^25}|{3:^9}|".format("Name","Sex","E-mail","BirthYear"))
            tempTuple = infoList[infoCount]
            print("|{0:<2}|{1:^10}|{2:^5}|{3:^25}|{4:^9}|".format(infoCount+1,tempTuple[0],tempTuple[1],tempTuple[2],tempTuple[3]))

    def printAllInfo(self,infoList):
        if len(infoList) == 0:
            print("입력된 고객 정보가 없습니다.")
        else:
            count = 0
            print("|No|{0:^10}|{1:^5}|{2:^25}|{3:^9}|".format("Name","Sex","E-mail","BirthYear"))
            for member in infoList:
                count += 1
                print("|{0:^2}|{1:^10}|{2:^5}|{3:^25}|{4:^9}|".format(count,member[0],member[1],member[2],member[3]))

    def input_manual(self,):
        select = input('''
    ******************************************************************************************************
    어떤 기능을 사용하시겠습니까
    I:고객정보입력          Q:프로그램종료          A:전체 고객정보 조회
    C:현재 고객정보 조회    P:이전 고객정보 조회    N:다음 고객정보 조회 
    U:현재 고객 정보 수정   D:현재 고객 정보 삭제
    ******************************************************************************************************
    ''').upper()
        return select

