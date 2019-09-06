import pickle
import sqlite3



class CustomInput:   
    def Info(self):
        name = self.inputName()
        sex = self.inputSex()
        email = self.inputEmail()
        birthDate = self.inputBirthDate()
        temp = (name,sex,email,birthDate)

        return temp

    def inputInfo(self,infoList):
        print("고객 정보를 입력하세요")
        infoList.append(self.Info())

        conn=sqlite3.connect('infodb.db')
        c = conn.cursor()
        c.execute('''
        insert into stocks(name,sex,email,year)
        values(?,?,?,?)
        ''',self.Info())
        conn.commit()
        conn.close()

        # with open("./data.pickle","wb") as file:
        #     pickle.dump(infoList, file)
        
    def updateInfo(self,infoCount,infoList):
        if infoCount == -1:
            print("현재 조회하고 있는 고객 정보가 없습니다.")
        else:
            print("수정할 정보로 입력하십시오")

            temp1 = infoList[infoCount]      #현재 고객 정보 저장

            infoList[infoCount]=self.Info()

            temp2 = infoList[infoCount]      #변경된 고객 정보 저장
            tempsql = temp2 + temp1          #update sql문을 위한 정보 저장
            
            conn=sqlite3.connect('infodb.db')
            c = conn.cursor()
            c.execute('''
            update stocks 
            set name=? , sex=? , email=? , year=?
            where name=? and sex=? and email=? and year=?
            ''',tempsql)
            conn.commit()
            conn.close()

            # with open("./data.pickle","wb") as file:
            #     pickle.dump(infoList, file)
        return infoCount

    def deleteInfo(self,infoCount,infoList):
        if len(infoList) == 0:
            print("고객 정보가 없습니다")

        elif infoCount == -1:
            print("조회 중인 고객 정보가 없습니다.")

        else:
            conn=sqlite3.connect('infodb.db')
            c = conn.cursor()
            c.execute('''
            delete from stocks
            where name=? and sex=? and email=? and year=?
            ''',infoList[infoCount])
            conn.commit()
            conn.close()

            del infoList[infoCount]
            with open("./data.pickle","wb") as file:
                pickle.dump(infoList, file)
            print("현재 고객 정보를 삭제합니다")
            if len(infoList) == infoCount:
                print("마지막 페이지 고객 정보를 삭제하셨습니다. 이전 고객 정보를 불러 옵니다.")
                infoCount -= 1
                if infoCount == -1:
                    print("이전 고객 정보가 없습니다. 모든 고객 정보를 삭제하였습니다.")
            else:
                print("다음 고객 정보를 불러옵니다")
        return infoCount

    def inputName(self):
        while True:
            name = input("이름을 입력하세요:")
            if len(name)>=2 and len(name)<=30 and self.hasNumber(name)==False:
                return name
            print("이름은 2자이상 30자 이하의 문자만 입력할 수 있습니다.")

    def inputSex(self):
        while True:
            sex = input("성별을 입력하세요(남성:M,여성:F):").upper()
            if sex == "M" or sex == "F":
                return sex
            print("성별은 M(m)/F(f)만 올 수 있습니다.")

    def inputEmail(self):
        while True:
            email = input("이메일을 입력하세요:")
            if email:
                return email

    def inputBirthDate(self):
        while True:
            birthDate = input("태어난 연도를 입력하시요(ex 1993):")
            if len(birthDate)==4 and birthDate.isdigit():
                return birthDate
            print("태어난 연도는 숫자 네글자만 올 수 있습니다.")

    def hasNumber(self,inputString):     #입력된 문자열에 숫자가 있으면 True 없으면 False
        return any(one.isdigit() for one in inputString)