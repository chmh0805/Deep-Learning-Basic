# 9.7(Mon) 실습

# 문제 1

menu = '''
-----------------------------
종류        금액
1.사과파이 : 5000
2.사과쥬스 : 2000
3.사과    : 1000
----------------------------
메뉴를 선택하시오(번호를 누르시오) : 
'''

menu_use = {'1': 5, '2': 2, '3': 1}
menu_price = {'1': 5000, '2': 2000, '3': 1000}

apple_count = int(input("사과 재고를 입력하시오 : "))

while apple_count != 0:
    user_menu = input(menu)
    
    if user_menu not in ['1', '2', '3']:
        print("NO MENU\n")
        continue
        
    if apple_count - menu_use[user_menu] < 0:
        print("해당 재고가 없습니다.")
        print("마감합니다.")
        break
    
    elif apple_count - menu_use[user_menu] >= 0:
        while True:
            user_money = input("돈을 내시오: ")
            for i in user_money:
                a = 1
                if i not in "1234567890":
                    print("숫자를 입력하지 않았습니다.")
                    a -= 1
                    break
            if a == 1:
                user_money = int(user_money)
                break
        
    if user_money - menu_price[user_menu] < 0:
        print("금액이 부족합니다.")
        continue
    else:
        print("주문하신 상품의 가격은 {}입니다. 거스름돈은 {}입니다.".format(menu_price[user_menu], user_money-menu_price[user_menu]))
        apple_count -= menu_use[user_menu]
        print("현재 재고는 {}입니다.".format(apple_count))
        continue


# 문제 2

user_subject = []
user_score = []
    
while True:
    user_subject_input = input("과목명을 입력하세요. ")
    user_subject.append(user_subject_input)
    user_score_input = int(input("점수를 입력하세요. "))
    user_score.append(user_score_input)
    user_choice = input("추가로 입력하려면 y, 아니면 n을 입력하세요.")
    
    if user_choice == 'y':
        continue
        
    elif user_choice == 'n':
        for i in range(len(user_subject)):
            print("{} : {}".format(user_subject[i], user_score[i]))
        print("평균 : {}".format(sum(user_score) / len(user_score)))
    break


# 문제 3

user_list = '''

=============================
            메뉴
  1. 더 하 기
  2. 빼    기
  3. 곱 하 기
  4. 나 누 기
  5. 자    승
  6. 나 가 기
=============================


'''

num1 = "첫번째 숫자를 입력하세요. :"
num2 = "두번째 숫자를 입력하세요. :"
while True:

    while True:
        user_input = input(user_list)
        for i in user_input:
            a = 1
            if i not in "123456":
                print("숫자가 아닙니다. 다시 입력해주세요.")
                a -= 1
                break
        if a == 1:
            break

    if user_input == '6':
        print("계산기를 종료합니다.")
        break

    while True:
        user_num1 = input(num1)
        for i in user_num1:
            a = 1
            if i not in "0123456789":
                print("정수를 제대로 입력해주세요.\n")
                a -= 1
                break
        if a == 1:
            user_num1 = int(user_num1)
            break
    
    while True:
        user_num2 = input(num2)
        for i in user_num2:
            a = 1
            if i not in "0123456789":
                print("정수를 제대로 입력해주세요.\n")
                a -= 1
                break
        if a == 1:
            user_num2 = int(user_num2)
            break
    
    if user_input == '1':
        print("더하기를 수행한 값은 {} + {} = {} 입니다.".format(user_num1, user_num2, user_num1 + user_num2))
    if user_input == '2':
        print("빼기를 수행한 값은 {} - {} = {} 입니다.".format(user_num1, user_num2, user_num1 - user_num2))
    if user_input == '3':
        print("곱하기를 수행한 값은 {} * {} = {} 입니다.".format(user_num1, user_num2, user_num1 * user_num2))
    if user_input == '4':
        print("나누기를 수행한 값은 {} / {} = {} 입니다.".format(user_num1, user_num2, user_num1 / user_num2))
    if user_input == '5':
        print("자승을 수행한 값은 {} ** {} = {} 입니다.".format(user_num1, user_num2, user_num1 ** user_num2))


# 함수 실습
# 문제1


def isnum():
    while True:
        score = input("점수를 입력하세요. ")      
        for i in score:
            a = 1
            if i not in "0123456789":
                a -= 1
                break
        if a == 1:
            break
    return score


def avg_score(list1):
    return sum(list1) / len(list1)


user_subject = []
user_score = []

while True:
    user_subject_input = input("과목명을 입력하세요. ")
    user_subject.append(user_subject_input)
    user_score_input = isnum()
    user_score.append(int(user_score_input))
    user_choice = input("추가로 입력하려면 y, 아니면 n을 입력하세요.")
    
    if user_choice == 'y':
        continue
        
    elif user_choice == 'n':
        for i in range(len(user_subject)):
            print("{} : {}".format(user_subject[i], user_score[i]))
        print("평균 : {}".format(avg_score(user_score)))
    break
    
    
# 문제 2


def num_input():
    while True:
        user_num = input("숫자를 입력해주세요. :")
        for i in user_num:
            a = 1
            if i not in "0123456789":
                a -= 1
                print("숫자를 정확히 입력해주세요.")
                break
        if a == 1:
            break
    return int(user_num)
    
    
def calcul(x, user_num1, user_num2):
    if x == '1':
        print("더하기를 수행한 값은 {} + {} = {} 입니다.".format(user_num1, user_num2, user_num1 + user_num2))
    if x == '2':
        print("빼기를 수행한 값은 {} - {} = {} 입니다.".format(user_num1, user_num2, user_num1 - user_num2))
    if x == '3':
        print("곱하기를 수행한 값은 {} * {} = {} 입니다.".format(user_num1, user_num2, user_num1 * user_num2))
    if x == '4':
        print("나누기를 수행한 값은 {} / {} = {} 입니다.".format(user_num1, user_num2, user_num1 / user_num2))
    if x == '5':
        print("자승을 수행한 값은 {} ** {} = {} 입니다.".format(user_num1, user_num2, user_num1 ** user_num2))


user_list = '''

=============================
            메뉴
  1. 더 하 기
  2. 빼    기
  3. 곱 하 기
  4. 나 누 기
  5. 자    승
  6. 나 가 기
=============================


'''

while True:

    while True:
        user_input = input(user_list)
        for i in user_input:
            a = 1
            if i not in "123456":
                print("숫자가 아닙니다. 다시 입력해주세요.")
                a -= 1
                break
        if a == 1:
            break

    if user_input == '6':
        print("계산기를 종료합니다.")
        break

    user_num1 = num_input()
    user_num2 = num_input()
    
    calcul(user_input, user_num1, user_num2)
    
# 문제 3


def money_input():
    while True:
        num = input("금액을 입력해주세요.: ")
        for i in num:
            a = 1
            if i not in "0123456789":
                a -= 1
                print("금액을 정확히 입력해주세요.")
                break
        if a == 1:
            break
    return int(num)


def now_balance(balance):
    while True:
        print("\n현재 잔고는 {}원입니다.".format(balance))
        choice = input("계속 거래 하시겠습니까?\n 예 : 1   ,   아니오 : 2\n")
        if choice == '1':
            return True
        else:
            print("통장을 파기합니다.")
            return False


balance = 10000

while True:
    cmd = input("입금, 출금을 선택해주세요 : ")
    if cmd not in ["입금","출금"]:
        print("잘못 입력하셨습니다.")
        continue
    money = money_input()
    if cmd == "입금":
        balance += money
        print("\n{}원이 입금되었습니다. 현재 잔고는 {}원입니다.\n".format(money, balance))
    elif balance >= money:
        balance -= money
        print("\n{}원이 출금되었습니다. 현재 잔고는 {}원입니다.\n".format(money, balance))
    else:
        print("\n{}원 출금을 요청하셨지만 잔액이 {}원 부족합니다. 현재 잔고는 {}원입니다.\n".format(money, money-balance, balance))
	
    if balance == 0:
        if now_balance(balance):
            continue
        else:
            break


# 문제 4

test = lambda x, y, z : x * y / z