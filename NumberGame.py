from random import randint

def getRandomNumber():
    return randint(1, 100)

def inputGameName():
    name = ""
    while True:
        name = input("게임의 제목 입력: ")
        if name and len(name) <=25:
            break
        print("게임 제목은 1~25자로 입력")
    return name

def inputGamerName():
    name = ""
    while True:
        name = input("게이머 이름 입력: ")
        if name and len(name) <=20:
            break
        print("게이머 이름은 1~20자로 입력")
    return name

def game():
    AInumber = getRandomNumber()
    count = 0
    while True:
        print(AInumber)
        select = input("1~100 사이 중 AI의 값을 예측하여 입력하세요")
        if select == False:
            print("값을 입력하세요")
        elif select.isdigit() == False:
            print("숫자를 입력하세요")
        elif int(select) <1 and int(select) >100:
            print("1이상 100이하 숫자를 입력하세요")
        else:
            count += 1
            if AInumber>int(select):
                print("Up")
            elif AInumber<int(select):
                print("Down")
            else:
                print("{0}번만에 맞추셨습니다".format(count))
                while True:
                    gameStart = input("게임을 다시 하시겠습니까?(y/n)").upper()
                    if gameStart == "N":
                        return
                    elif gameStart == "Y":
                        count = 0
                        AInumber = getRandomNumber()
                        break
                    else:
                        print("y 또는 n 중에서 입력해주세요")

def main():
    gameName = inputGameName()
    gamerName = inputGamerName()

    print("{0:=^50}  GamerName:{1}".format(gameName,gamerName))
    
    game()
    
if __name__=="__main__":
    main()