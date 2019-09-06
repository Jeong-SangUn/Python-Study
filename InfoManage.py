from customModel import CustomInput
from customControl import Move
from customView import Printinfo
# import pickle
import sqlite3


def main():
    control = Move()
    view = Printinfo()
    model = CustomInput()
    infoList = []
    infoCount = -1

    conn=sqlite3.connect('infodb.db')
    c = conn.cursor()
    c.execute("select * from stocks")
    items=c.fetchall()
    for item in items:
        infoList.append(item)
    conn.commit()
    conn.close()
    
    while True:
        # with open("./data.pickle","rb") as file:
        #     infoList = pickle.load(file)

        select = view.input_manual() #메뉴얼 출력 및 동작 입력

        if select == "I":    #고객 정보 입력
            model.inputInfo(infoList)

        elif select == "C":  #현재 고객 정보 출력
            if control.isnow(infoCount,infoList):     #현재 조회 중인 고객 정보가 있으면 1리턴 아니면 0리턴
                view.printInfo(infoCount,infoList)
            else:
                print("현재 조회 중인 고객 정보가 없습니다.")

        elif select == "N":  #다음 고객 정보 출력
            if control.isnext(infoCount,infoList):      #다음 고객 정보가 있으면 1리턴 아니면 0리턴
                infoCount = control.nextInfo(infoCount,infoList)
                view.printInfo(infoCount,infoList)
            else:
                print("다음 고객 정보가 없습니다.")

        elif select == "P":  #이전 고객 정보 출력
            if control.ispre(infoCount,infoList):       #이전 고객 정보가 있으면 1리턴 아니면 0리턴
                infoCount = control.preInfo(infoCount,infoList)
                view.printInfo(infoCount,infoList)
            else:
                print("이전 고객 정보가 없습니다.")

        elif select == "A":  #모든 고객 정보 출력
            view.printAllInfo(infoList)

        elif select == "U":  #현재 고객 정보 수정
            infoCount = model.updateInfo(infoCount,infoList)
            view.printInfo(infoCount,infoList)

        elif select == "D":  #현재 고객 정보 삭제
            infoCount = model.deleteInfo(infoCount,infoList)

        elif select == "Q":  #프로그램 종료
            print("프로그램을 종료합니다")
            
            break   

        else:               #제공하지 않는 기능_예외처리
            print("선택지를 다시 확인해주세요!")
        
if __name__ == "__main__":
    main()