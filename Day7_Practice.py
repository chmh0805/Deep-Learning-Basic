# 9.9 실습

# open-w 실습

exam = '''

시험 종류 : 1학기중간, 1학기기말, 2학기중간, 2학기기말

입력할 시험 종류 입력 :

'''

subject_text = '입력할 과목 : '

score_text = '성적 : '


def isnum():
    while True:
        score = input(score_text)
        a = 0
        for i in score:
            if i not in "0123456789":
                print("숫자를 입력해주세요.")
                a += 1
                break
        if a == 0:
            return int(score)


def append_choice():
    while True:
        choice = input("추가로 입력하시겠습니까?(y or n) : ")
        if choice not in ['y', 'n']:
            print("\ny 또는 n을 입력해주세요.")
            continue
        elif choice == 'y':
            return True
        else:
            return False


exam_list = ["1학기중간", "1학기기말", "2학기중간", "2학기기말"]
subject_list = []
mid1_score = []
last1_score = []
mid2_score = []
last2_score = []
f = open('exam.txt', 'w')

while True:
    user_input = input(exam)
    if user_input not in exam_list:
        print("\n시험 종류를 정확히 입력해주세요.\n")
        continue
    if user_input == "1학기중간":
        user_subject = input(subject_text)
        if user_subject not in subject_list:
            subject_list.append(user_subject)
        user_score = isnum()
        mid1_score.append(user_score)
    elif user_input == "1학기기말":
        user_subject = input(subject_text)
        if user_subject not in subject_list:
            subject_list.append(user_subject)
        user_score = isnum()
        last1_score.append(user_score)
    elif user_input == "2학기중간":
        user_subject = input(subject_text)
        if user_subject not in subject_list:
            subject_list.append(user_subject)
        user_score = isnum()
        mid2_score.append(user_score)
    elif user_input == "2학기기말":
        user_subject = input(subject_text)
        if user_subject not in subject_list:
            subject_list.append(user_subject)
        user_score = isnum()
        last2_score.append(user_score)

    if append_choice():
        continue
    else:
        print("시험성적 입력 프로그램을 종료합니다.")
        i = 0
    
    if i == 0:
        f.write("시험\t")
        for subject in subject_list:
            f.write("\t{}".format(subject))
        f.write("\n1학기중간\t")
        for i in mid1_score:
            f.write("{}\t".format(str(i)))
        f.write("\n1학기기말\t")
        for i in last1_score:
            f.write("{}\t".format(str(i)))
        f.write("\n2학기중간\t")
        for i in mid2_score:
            f.write("{}\t".format(str(i)))            
        f.write("\n2학기기말\t")
        for i in last2_score:
            f.write("{}\t".format(str(i)))
        i = 1
    
    if i == 1:
        f.close()
        break


# open-r 실습

menu = '''
성적확인

1. 시험별 성적
2. 시험별 평균
3. 과목별 점수
4. 종료

'''

test_menu = '''
확인하고자 하는 시험은?
(1학기중간, 1학기기말, 2학기중간, 2학기기말)
'''


def more():
    while True:
        user = input("추가로 검색하시겠습니까?(y or n) : ")
        if user not in ['y', 'n']:
            print("y 또는 n을 입력해주세요.")
            continue
        elif user == 'y':
            return True
        else:
            return False


test_list = ['1학기중간', '1학기기말', '2학기중간', '2학기기말']

f = open('exam.txt', 'r')
lines = f.readlines()

while True:
    choice = input(menu)
    if choice not in "1234":
        print("올바른 메뉴를 입력해주세요.")
        continue
    
    if choice == '4':
        print("성적확인 프로그램을 종료합니다.")
        break
        
    if choice == '1':
        while True:
            choice1 = input(test_menu)
            if choice1 not in test_list:
                print("정확하게 입력해주세요.\n")
                continue
            else:
                break
        if choice1 == "1학기중간":
            for i in range(1, len(lines[0].split())):
                print("{}: {}점".format(lines[0].split()[i], lines[1].split()[i]))
        if choice1 == "1학기기말":
            for i in range(1, len(lines[0].split())):
                print("{}: {}점".format(lines[0].split()[i], lines[2].split()[i]))
        if choice1 == "2학기중간":
            for i in range(1, len(lines[0].split())):
                print("{}: {}점".format(lines[0].split()[i], lines[3].split()[i]))
        if choice1 == "2학기기말":
            for i in range(1, len(lines[0].split())):
                print("{}: {}점".format(lines[0].split()[i], lines[4].split()[i]))
        
        if more():
            continue
        else:
            break
    
    if choice == '2':
        sum = 0
        while True:
            choice2 = input(test_menu)
            if choice2 not in test_list:
                print("정확하게 입력해주세요.\n")
                continue
            else:
                break

        if choice2 == "1학기중간":
            for i in lines[1].split()[1:]:
                sum += int(i)
            print("{}의 평균은 {}입니다.".format(choice2, sum/len(lines[1].split()[1:])))
        if choice2 == "1학기기말":
            for i in lines[2].split()[1:]:
                sum += int(i)
            print("{}의 평균은 {}입니다.".format(choice2, sum/len(lines[2].split()[1:])))
        if choice2 == "2학기중간":
            for i in lines[3].split()[1:]:
                sum += int(i)
            print("{}의 평균은 {}입니다.".format(choice2, sum/len(lines[3].split()[1:])))
        if choice2 == "2학기기말":
            for i in lines[4].split()[1:]:
                sum += int(i)
            print("{}의 평균은 {}입니다.".format(choice2, sum/len(lines[4].split()[1:])))

        if more():
            continue
        else:
            break

 
    if choice == '3':
        while True:
            choice3 = input("검색하고자하는 과목 :")
            if choice3 not in lines[0].split()[1:]:
                print("과목이 존재하지 않습니다.\n")
                continue
            
            if choice3 in lines[0].split()[1:]:
                break
        
        if choice3 == lines[0].split()[1]:
            for i in range(1,5):
                print("{}: {}점".format(lines[i].split()[0], lines[i].split()[1]))
        if choice3 == lines[0].split()[2]:
            for i in range(1,5):
                print("{}: {}점".format(lines[i].split()[0], lines[i].split()[2]))
        if choice3 == lines[0].split()[3]:
            for i in range(1,5):
                print("{}: {}점".format(lines[i].split()[0], lines[i].split()[3]))
        if choice3 == lines[0].split()[4]:
            for i in range(1,5):
                print("{}: {}점".format(lines[i].split()[0], lines[i].split()[4]))
        if choice3 == lines[0].split()[5]:
            for i in range(1,5):
                print("{}: {}점".format(lines[i].split()[0], lines[i].split()[5]))

        if more():
            continue
        else:
            print("성적확인 프로그램을 종료합니다.")
            break


# class 실습

war_skill = '''
==============
스킬을 선택하세요.
1. 베기
2. 찌르기
3. 대쉬
==============
'''

thief_skill = '''
==============
스킬을 선택하세요.
1. 암살
2. 은신
3. 훔치기
==============
'''

magician_skill = '''
==============
스킬을 선택하세요.
1. 불
2. 물
3. 바람
==============
'''

class Char:
    def __init__(self, name, him, dex, ji, job):
        self.name = name
        self.him = him
        self.dex = dex
        self.ji = ji
        self.job = job
    
    
    def first_skill(self):
        if self.job == '전사':
            while True:
                choice = input(war_skill)
                if choice not in "123":
                    print("1, 2, 3 중에 입력하세요.\n")
                    continue
                
                if choice == '1':
                    print("베기를(을) 배웠습니다.")
                elif choice == '2':
                    print("찌르기를(을) 배웠습니다.")
                else:
                    print("대쉬를(을) 배웠습니다.")
                break

        if self.job == '도적':
            while True:
                choice = input(thief_skill)
                if choice not in "123":
                    print("1, 2, 3 중에 입력하세요.\n")
                    continue
                
                if choice == '1':
                    print("암살를(을) 배웠습니다.")
                elif choice == '2':
                    print("은신를(을) 배웠습니다.")
                else:
                    print("훔치기를(을) 배웠습니다.")
                break

        if self.job == '마법사':
            while True:
                choice = input(magician_skill)
                if choice not in "123":
                    print("1, 2, 3 중에 입력하세요.\n")
                    continue
                
                if choice == '1':
                    print("불마법를(을) 배웠습니다.")
                elif choice == '2':
                    print("물마법를(을) 배웠습니다.")
                else:
                    print("바람마법를(을) 배웠습니다.")
                break

while True:
    name = input("캐릭터명을 입력하세요. : ")
    while True:
        him = int(input("힘을 입력하세요. :"))
        dex = int(input("민첩을 입력하세요. :"))
        ji = int(input("지능을 입력하세요. :"))
        if (him + dex + ji) > 30:
            print("힘, 민첩, 지능의 합이 30을 넘지 않도록 설정하세요.")
            continue
        elif him == max(him, dex, ji):
            job = '전사'
        elif dex == max(him, dex, ji):
            job = '도적'
        elif ji == max(him, dex, ji):
            job = '마법사'
        break
    
    user1 = Char(name, him, dex, ji, job)
    user1.first_skill()
    
    print("\n끝났습니다.")
    break


# class 실습 2

class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        result = 0
    
    def add(self):
        return self.first + self.second
    
    
    def sub(self):
        return self.first - self.second
    
    
    def mul(self):
        return self.first * self.second
    
    
    def div(self):
        return self.first / self.second
    
    
class Cal(Calculator):
    
    def div_zero(self):
        if self.second == 0:
            result = 0
        else:
            result = self.first / self.second
        return result


menu = '''
======================
메뉴
1. 계산하기
2. 각 계산기의 마지막 결과 확인
3. 종료
======================
'''


def isnum():
    while True:
        num = input("num: ")
        a = 1
        for i in num:
            if i not in "0123456789":
                print("정수 또는 실수를 입력해주세요.")
                a -= 1
                continue
        if a == 1:
            return int(num)

result_dict = {}

while True:
    while True:
        choice = input(menu)
        if choice not in "123":
            print("1, 2, 3 중에 선택해주세요.\n")
            continue
        else:
            break
    if choice == '3':
        print("계산기를 종료합니다.")
        break
    
    if choice == '1':
        while True:
            cal_num = input("계산기 선택 : (1, 2, 3, 4, 5 중 택 1) ")
            if cal_num not in "12345":
                print("1, 2, 3, 4, 5 중 선택해주세요.\n")
                continue
            else:
                break
        
        if cal_num == '1':
            num1 = isnum()
            num2 = isnum()
            while True:
                operator = input("기호 : (+, -, *, /) ")
                if operator not in ['+', '-', '*', '/']:
                    print("다시 입력해주세요.\n")
                    continue
                else:
                    break
            c1 = Cal(num1, num2)
            if operator == '+':
                c1.result = c1.add()
            elif operator == '-':
                c1.result = c1.sub()
            elif operator == '*':
                c1.result = c1.mul()
            else:
                c1.result = c1.div_zero()
            
            result_dict['1'] = c1.result
            print("{} {} {} = {}".format(num1, operator, num2, c1.result))

        elif cal_num == '2':
            num1 = isnum()
            num2 = isnum()
            while True:
                operator = input("기호 : (+, -, *, /) ")
                if operator not in ['+', '-', '*', '/']:
                    print("다시 입력해주세요.\n")
                    continue
                else:
                    break
            c2 = Cal(num1, num2)
            if operator == '+':
                c2.result = c2.add()
            elif operator == '-':
                c2.result = c2.sub()
            elif operator == '*':
                c2.result = c2.mul()
            else:
                c2.result = c2.div_zero()
            
            result_dict['2'] = c2.result
            print("{} {} {} = {}".format(num1, operator, num2, c2.result))
            
        elif cal_num == '3':
            num1 = isnum()
            num2 = isnum()
            while True:
                operator = input("기호 : (+, -, *, /) ")
                if operator not in ['+', '-', '*', '/']:
                    print("다시 입력해주세요.\n")
                    continue
                else:
                    break
            c3 = Cal(num1, num2)
            if operator == '+':
                c3.result = c3.add()
            elif operator == '-':
                c3.result = c3.sub()
            elif operator == '*':
                c3.result = c3.mul()
            else:
                c3.result = c3.div_zero()
            
            result_dict['3'] = c3.result
            print("{} {} {} = {}".format(num1, operator, num2, c3.result))
            
        elif cal_num == '4':
            num1 = isnum()
            num2 = isnum()
            while True:
                operator = input("기호 : (+, -, *, /) ")
                if operator not in ['+', '-', '*', '/']:
                    print("다시 입력해주세요.\n")
                    continue
                else:
                    break
            c4 = Cal(num1, num2)
            if operator == '+':
                c4.result = c4.add()
            elif operator == '-':
                c4.result = c4.sub()
            elif operator == '*':
                c4.result = c4.mul()
            else:
                c4.result = c4.div_zero()
            
            result_dict['4'] = c4.result
            print("{} {} {} = {}".format(num1, operator, num2, c4.result))
            
        elif cal_num == '5':
            num1 = isnum()
            num2 = isnum()
            while True:
                operator = input("기호 : (+, -, *, /) ")
                if operator not in ['+', '-', '*', '/']:
                    print("다시 입력해주세요.\n")
                    continue
                else:
                    break
            c5 = Cal(num1, num2)
            if operator == '+':
                c5.result = c5.add()
            elif operator == '-':
                c5.result = c5.sub()
            elif operator == '*':
                c5.result = c5.mul()
            else:
                c5.result = c5.div_zero()

            
            result_dict['5'] = c5.result
            print("{} {} {} = {}".format(num1, operator, num2, c5.result))
    
    if choice == '2':
        while True:
            choice2 = input("확인하고자 하는 계산기 번호를 입력하세요. ")
            if choice2 not in result_dict.keys():
                print("계산한 적이 없거나, 잘못 입력하셨습니다.")
                print("1, 2, 3, 4, 5 중 1개를 입력해주세요.")
                continue
            else:
                print(result_dict[choice2])
                break
        
    while True:
        choice1 = input("초기 메뉴로 돌아갈까요?(y or n) ")
        if choice1 not in ['y', 'n']:
            print("y 또는 n을 입력해주세요.\n")
            continue
        else:
            break
    if choice1 == 'y':
        continue
    elif choice1 == 'n':
        print("계산기를 종료합니다.")
        break
