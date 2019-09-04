import infoModule
import infoMoveModule
import printModule

def main():
    move = infoMoveModule.Move()
    infoList = []
    infoCount = -1
    while True:
        select = printModule.input_manual() #메뉴얼 출력 및 동작 입력

        if select == "I":    #고객 정보 입력
            infoModule.inputInfo(infoList)

        elif select == "C":  #현재 고객 정보 출력
            move.nowInfo(infoCount,infoList)
            printModule.printInfo(infoCount,infoList)

        elif select == "N":  #다음 고객 정보 출력
            infoCount = move.nextInfo(infoCount,infoList)
            printModule.printInfo(infoCount,infoList)
            
        elif select == "P":  #이전 고객 정보 출력
            infoCount = move.preInfo(infoCount,infoList)
            printModule.printInfo(infoCount,infoList)
    
        elif select == "A":  #모든 고객 정보 출력
            printModule.printAllInfo(infoList)

        elif select == "U":  #현재 고객 정보 수정
            infoCount = infoModule.updateInfo(infoCount,infoList)
            printModule.printInfo(infoCount,infoList)

        elif select == "D":  #현재 고객 정보 삭제
            infoCount = infoModule.deleteInfo(infoCount,infoList)

        elif select == "Q":  #프로그램 종료
            print("프로그램을 종료합니다")
            break   

        else:               #제공하지 않는 기능_예외처리
            print("선택지를 다시 확인해주세요!")

if __name__ == "__main__":
    main()