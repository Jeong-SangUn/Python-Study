import re

start_explanation="="*40+"""
I : 고객정보 입력
P/C/N : 이전/현재/다음 고객정보 조회
U : 고객정보 수정
D : 고객정보 삭제
A : db 모두 보여주기
Q : 프로그램 종료
auto : 고객정보 테스트 자동넣기(아직구현중)
명령어를 입력해 주세요
"""+"="*40
table=[]
#-1일때 아무것도 없음
index=-1

def inputName():
    while True:
        name=input("이름을 입력해 주세요 :")
        re_kor=re.compile('[ㄱ-ㅣ가-힣]')
        if re_kor.match(name):
            dic['name']=name
            break
        else :
            print("한국이름만 받습니다")

def inputGender():
    while True:
        gender=input("성별을 입력해 주세요(F/M) :")
        re_gen=re.compile('[FM]')
        if re_gen.match(gender):
            dic['gender']=gender
            break
        else:
            print("F 나 M만 받습니다")

def inputEmail():
    while True:
        email = input("이메일을 입력해 주세요 :")
        if email:
            dic['email'] = email
            break

def inputBornYear():
    while True:
        year=input("태어난 년도를 입력해 주세요 :")
        re_year=re.compile('[0-9]')
        if re_year.match(year):
            dic['born-year']=year
            break
        else:
            print("숫자가 이상한걸요?")

def printHead(order):
    print("#\t", "이  름\t\t", "성별\t","이메일\t\t", "출생년도")
    dic=table[index]
    if order != 'A':
        print(str(index),'\t',dic['name']+'\t\t',dic['gender']+'\t',dic['email']+'\t\t',str(dic['born-year']))
    else:
        print("{0:=^40}".format("모두보기"),"\n")
        for n, i in enumerate(table):
            print(n,'\t',i['name'],'\t\t',i['gender'],'\t',i['email'],'\t\t',i['born-year'])

while True:
    order=input(start_explanation+"\n").upper()
    if order=="I":
        dic={'name':'name','gender':'F/M','email':'email','born-year':"1900"}
        inputName()
        inputGender()
        inputEmail()
        inputBornYear()
        table.append(dic)
        index=len(table)-1

        printHead(order)   
    
    elif order=="P":
        if index>0: 
            index=index-1
            print("이전 고객 정보입니다")
            
            printHead(order)
        else:
            print("이전고객정보가 없습니다")

    elif order=="C":
        if index!=-1:
            print("현재 고객정보입니다")
            printHead(order)
            
        else:
            print("고객정보가 없습니다")
    elif order=="N":
        if index<len(table)-1:
            index=index+1
            print("다음 고객정보입니다")
            printHead(order)
        else:
            print("마지막 고객정보입니다")

    elif order=="U":
        print("고객정보를 수정합니다")
        
        dic={'name':'name','gender':'F/M','email':'email','born-year':"1900"}
        inputName()
        inputGender()
        inputEmail()
        inputBornYear()
        table[index]=dic

        printHead(order)

    elif order=="D":
        if len(table)!=0:
            del table[index]
            if len(table) == index:
                index=index -1
            print("현재 고객정보를 삭제하였습니다")
        else:
            print("삭제할 고객정보가 없습니다.")

    elif order=="A":
        printHead(order)        
        
    elif order=="Q":
        print("콘솔을 종료합니다")
        break
    else:
        print("잘못된 명령")
    