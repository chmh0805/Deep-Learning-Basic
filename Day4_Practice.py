# 9.4 실습

# 튜플 실습

tu1 = ('a1', 'b1', 'c1')
tu2 = ('a2', 'b2', 'c2')

tu3 = tu1 + tu2

print(tu3[3])
print(tu3[2:6])
tu4 = tu3 * 3
print(tu4.count('a1'))
print(tu4.index('b2'))

tu5 = tu4 + ([1, 2, 3], ['a', 'b', 'c'])
# 튜플은 수정 불가


# 딕셔너리 실습

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(list(dic.keys()))
print(list(dic.values()))
print('e' in dic.keys())
print(5 in dic.values())

keywords = ['group', 'name', 'age', 'area']
info = {}
i = 0
while True:
    val = input("{:>10} : ".format(keywords[i]))
    info[keywords[i]] = val
    i += 1
    if i == 4:
        for j in range(len(list(info.keys()))):
            if j == 2:
                print("내 {}은 {}이며 {}대입니다.".format(list(info.keys())[j], list(info.values())[j], str(int(list(info.values())[j])//10*10)))
            else:
                print("내 {}은 {}입니다.".format(list(info.keys())[j], list(info.values())[j]))
        break;
'''  또는
for i in keywords:
    val = input("{:>10} : ".format(i))
    info[i] = val

print(info)
for i, j in info.items():
    if i == age:
        print("내 {}은 {}이며 {}대입니다.".format(i, j, str(int(j)//10*10)))
    else:
        print("내 {}은 {}입니다.".format(i, j))
'''


# 집합 실습

s1 = set(['a', 'c', 'e', 'b', 'd', 'f', 1])
s2 = set([1, 2, 3, 'b', 'd', 'f'])
string1 = "BOYS, BE AMBITIOUS"
s3 = set(string1.lower())

print(s1 & s2 & s3) # s1.intersection(s2.intersection(s3))
print(s1 | s2 | s3) # s1.union(s2.union(s3))
print(s3 - s2 - s1) # s3.difference(s2.difference(s1))

s1.update(['g', 'h'])
s2.add('A')


# if & for & while 실습

#1
srp1 = ['가위', '바위', '바위', '바위', '보', '가위', '가위', '보', '가위', '보']
result = []
for i in range(len(srp1)):
    user_srp = input("가위, 바위, 보 : ")
    if user_srp == '가위':
        if srp1[i] == '가위':
            result.append('비김')
        elif srp1[i] == '보':
            result.append('승')
        else:
            result.append('패')
    elif user_srp == '바위':
        if srp1[i] == '바위':
            result.append('비김')
        elif srp1[i] == '가위':
            result.append('승')
        else:
            result.append('패')
    elif user_srp == '보':
        if srp1[i] == '보':
            result.append('비김')
        elif srp1[i] == '바위':
            result.append('승')
        else:
            result.append('패')
    else:
        result.append('패')

print("{}승 {}패 {}비김".format(result.count('승'), result.count('패'), result.count('비김')))


#2
balance = 10000
while True:
    money = 0
    if balance == 0:
        print("통장을 파기합니다.")
        break;
    user_input = input("출금 또는 입금을 입력해주세요.: ")
    
    if user_input == '출금':
        money = int(input("출금 금액을 입력해주세요. : "))
        if balance >= money:
            balance -= money
            print("{}원이 출금되었습니다. 현재 잔고는 {}입니다.".format(money, balance))
        elif balance < money:
            print("현재 잔고 부족입니다. {}원이 부족합니다.".format(abs(balance - money)))
            continue
    elif user_input == '입금':
        money = int(input("입금 금액을 입력해주세요. : "))
        balance += money
        print("{}원이 입금되었습니다. 현재 잔고는 {}입니다.".format(money, balance))
        continue
    else:
        print("출금 또는 입금을 입력해주세요.")
        continue


#3
total = 30
menu = '''
    아메리카노(A를 눌러주세요.)
    라떼(L를 눌러주세요.)
    에스프레소(E를 눌러주세요.)
    '''
menu_list = ['L', 'A', 'E']
    
while True:
    print("현재 남은 샷 : {}shot\n".format(total))
    user_input = input(menu).upper()
    
    if user_input not in menu_list:
        print("No Menu")
        continue
    
    if total - (menu_list.index(user_input)+1) < 0:
        print("재료가 부족해서 주문 불가합니다.")
    elif total - (menu_list.index(user_input)+1) == 0:
        if user_input.upper() == 'L':
            print("라떼 선택하셨습니다.")
        elif user_input.upper() == 'A':
            print("아메리카노 선택하셨습니다.")
        elif user_input.upper() == 'E':
            print("에스프레소 선택하셨습니다.")
        print("마감합니다.")
        break
    else:
        if user_input.upper() == 'L':
            print("라떼 선택하셨습니다.")
            total -= (menu_list.index(user_input)+1)
        elif user_input.upper() == 'A':
            print("아메리카노 선택하셨습니다.")
            total -= (menu_list.index(user_input)+1)
        elif user_input.upper() == 'E':
            print("에스프레소 선택하셨습니다.")
            total -= (menu_list.index(user_input)+1)


#4
subject_list = ['국어', '영어', '수학', '과학', '사회']
user_score_list = []
user_score_sum = 0

for subject in subject_list:
    val = int(input("{}: ".format(subject)))
    user_score_sum += val
    if val >= 60:
        user_score_list.append(subject)

print("60점 이상인 과목: {}, 평균: {}".format(user_score_list, user_score_sum/5)) 


#5

a = 0

while True:
    num1 = input("숫자를 입력하세요: ")
    
    for c in num1:
        a = 1
        if c not in "0123456789":
            print("숫자를 입력하지 않았습니다.")
            a -= 1
            continue
        else:
            print("입력한 값은 {} 입니다.".format(num1))
    if a == 1:
        break