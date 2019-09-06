class Move:
    
    # def nowInfo(self,infoCount,infoList):
    #     if infoCount<0:
    #         print("조회 중인 고객 정보가 없습니다..")
    #         return 0
    #     else:
    #         return 1

    # def nextInfo(self,infoCount,infoList):
    #     if len(infoList) == infoCount+1:
    #         print("다음 고객 정보가 없습니다.")
    #     else:
    #         infoCount = infoCount+1
    #     return infoCount

    # def preInfo(self,infoCount,infoList):
    #     if infoCount<1:
    #         print("이전 고객 정보가 없습니다.")
    #     else:
    #         infoCount = infoCount-1
    #     return infoCount

    def nextInfo(self,infoCount,infoList):
        return infoCount+1

    def preInfo(self,infoCount,infoList):
        return infoCount-1

    def isnow(self,infoCount,infoList):
        if infoCount<0:
            return 0
        else:
            return 1

    def isnext(self,infoCount,infoList):
        if len(infoList) == infoCount+1:
            return 0
        else:
            return 1

    def ispre(self,infoCount,infoList):
        if infoCount<1:
            return 0
        else:
            return 1 