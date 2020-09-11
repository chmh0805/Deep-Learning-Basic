# moduletest1.py
import sys
sys.path.append('C:\\doit1')

import fourcal as fc
from fourcal1 import Morefourcal

menu = '''

=============
    계산기
A. 계산하기
B. 나가기
=============

'''

while True:
    while True:
        choice = input(menu).upper()
        if choice not in ['A', 'B']:
            print("a 또는 b를 입력하세요.")
            continue
        else:
            break
    
    if choice == 'B':
        print("계산기를 종료합니다.")
        break
    
    if choice == 'A':
        num1 = fc.numfind()
        num2 = fc.numfind()
        num3 = fc.numfind()
        while True:
            operator = input("기호: (+, -, *, /, **) ")
            if operator not in ['+', '-', '*', '/', '**']:
                print("기호를 정확히 입력하세요.")
                continue
            else:
                break

        if operator == '+':
            print("{} + {} + {} = {}".format(num1, num2, num3, fc.add(num1,num2,num3)))

        if operator == '-':
            print("{} - {} - {} = {}".format(num1, num2, num3, fc.sub(num1,num2,num3)))

        if operator == '*':
            print("{} * {} * {} = {}".format(num1, num2, num3, fc.mul(num1,num2,num3)))

        if operator == '/':
            print("{} / {} / {} = {}".format(num1, num2, num3, fc.div(num1,num2,num3)))
        
        if operator == '**':
            jasung_var = Morefourcal(num1, num2, num3)
            print("{} ** {} ** {} = {}".format(num1, num2, num3, jasung_var.jasung()))
        
    while True:
        choice1 = input("다시 계산하시겠습니까?(y or n) ").upper()
        if choice1 not in ['Y', 'N']:
            print("y 또는 n을 입력하세요.")
            continue
        else:
            break
    if choice1 == 'Y':
        continue
    else:
        print("계산기를 종료합니다.")
        break