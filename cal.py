import sys
sys.path.append('C:\\doit')

from calsub import *

while True:
    menu1=input('''메뉴
1.계산하기
2.각 계산기의 마지막 결과 확인
3.나가기

선택하시오. : ''')
    print("")
    if menu1 == '3':
        break
    while True:
        if menu1 =='1':
            calnum = input('계산기를 선택하시오.(1,2,3,4,5 중에서 선택): ')
            i=1
            num1 = numfind(i)
            num2 = numfind(i+1)
            cal=input("기호 : ")
            if calnum == '1':
                a1=safeFourcal(num1,num2,cal)
                if a1.cal == '/':
                    a1.div()
                else:
                    a1.fourcal()
                                    
            if calnum == '2':
                a2=safeFourcal(num1,num2,cal)
                if a2.cal == '/':
                    a2.div()
                else:
                    a2.fourcal()
                
            if calnum == '3':
                a3=safeFourcal(num1,num2,cal)
                if a3.cal == '/':
                    a3.div()
                else:
                    a3.fourcal()
               
            if calnum == '4':
                a4=safeFourcal(num1,num2,cal)
                if a4.cal == '/':
                    a4.div()
                else:
                    a4.fourcal()
                
            if calnum == '5':
                a5=safeFourcal(num1,num2,cal)
                if a5.cal == '/':
                    a5.div()
                else:
                    a5.fourcal()

            print("")        
            break
        else:
            calnum = input('계산기를 선택하시오.(1,2,3,4,5 중에서 선택): ')
            print("")
            if calnum == '1':
                print("{}번 계산기의 마지막 값은 {} 입니다.".format(calnum,a1.result))

            if calnum == '2':
                print("{}번 계산기의 마지막 값은 {} 입니다.".format(calnum,a2.result))                
            if calnum == '3':
                print("{}번 계산기의 마지막 값은 {} 입니다.".format(calnum,a3.result))               
            if calnum == '4':
                print("{}번 계산기의 마지막 값은 {} 입니다.".format(calnum,a4.result))                
            if calnum == '5':
                print("{}번 계산기의 마지막 값은 {} 입니다.".format(calnum,a5.result))
            print("")    
            break