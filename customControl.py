class Move:
    
    def nowInfo(self,infoCount,infoList):
        if infoCount<0:
            print("조회 중인 고객 정보가 없습니다..")
        return infoCount

    def nextInfo(self,infoCount,infoList):
        if len(infoList) == infoCount+1:
                print("다음 고객 정보가 없습니다.")
        else:
            infoCount = infoCount+1
        return infoCount

    def preInfo(self,infoCount,infoList):
        if infoCount<1:
                print("이전 고객 정보가 없습니다.")
        else:
            infoCount = infoCount-1
        return infoCount 