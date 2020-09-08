# 9.8 (Tue)

import copy


def gender():
    user = input("성별(남/여) :\t")
    if user not in ['남', '여']:
        return '남'
    else:
        return user


def user_info_view():
    while True:
        findname = input("찾는 이름 :\t")
        for i in range(len(user_list)):
            if findname in user_list[i].values():
                for j, k in user_list[i].items():
                    print("{} : {}".format(j, k))
            if findname not in user_list[i].values():
                print("없는 이름입니다.")
                continue
        break


def user_find(findname):
    for i in range(len(user_list)):
        if findname in user_list[i].values():
            return i


def birth():
    user = input("생년월일 :\t")
    for i in user:
        if i not in "0123456789":
            delimiter = i
            year, month, day = user.split(delimiter)[0], user.split(delimiter)[1], user.split(delimiter)[2]
            break
    if len(user) == 6:
        year, month, day = user[:2], user[2:4], user[4:]
    if len(user) == 8:
        year, month, day = user[:4], user[4:6], user[6:]
    if len(year) == 2:
        if int(year) >= 21:
            year = '19' + year
        else:
            year = '20' + year
    return year + '/' + month + '/' + day


def age(birth):
    return 2020 - int(birth[:4]) + 1    


def phone():
    user = input("전화번호 :\t")
    for i in user:
        if i not in "0123456789":
            delimiter = i
            a, b, c = user.split(i)[0], user.split(i)[1], user.split(i)[2]
            break
    if len(user) == 11:
        a, b, c = user[:3], user[3:7], user[7:]
    return a + '-' + b + '-' + c


def add_save():
    a=input("추가로 수정하시겠습니까?(y or n) : ")
    if a == 'n' :
        return 0
    else:
        return 1


menu = '''

==========
1.정보 입력
2.정보 확인
3.정보 수정
4.나가기
==========

'''

user_list = []
user_info = {'이름': '', '성별': '', '생년월일': '','나이': '','전화번호': '','지역': ''}

while True:
    choice = input(menu)
    if choice not in "1234":
        print("1, 2, 3, 4중 입력해주세요.")
        continue

    if choice == '4':
        print("명부 프로그램을 종료합니다.")
        break
    
    if choice == '1':
        dict1 = user_info.copy()
        dict1['이름'] = input("이름 :\t")
        dict1['성별'] = gender()
        dict1['생년월일'] = birth()
        dict1['나이'] = age(dict1['생년월일'])
        dict1['전화번호'] = phone()
        dict1['지역'] = input("지역 :\t")
        user_list.append(dict1)
        print(user_list)
    
    if choice == '2':
        user_info_view()
        
    if choice == '3':
        find_index = user_find(input("이름 검색 :\t"))
        find_dict = user_list[find_index]
        while 1:
            choice1 = input(choice1=input('''
1.생년월일
2.전화번호
3.지역

수정하고자 하는 항목을 적으시오 : '''))
            print("")
            if choice1 == '1':
                save_birth=birth()
                print("")
                save_age=age(save_birth)
                find_dict["생년월일"]=save_birth
                find_dict["나이"]=save_age
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()
                if a==0:
                    break
                else:
                    continue
            if choice1 == '2':
                save_tel = phone()
                print("")
                find_dict["전화번호"]=save_tel
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()                
                if a==0:
                    break
                else:
                    continue
            if choice == '3':
                save_area = input("지역 : ")
                print("")
                find_dict["지역"]=save_area
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()
                if a==0:
                    break
                else:
                    continue
            print("")        


# 파일 관리 실습

f1 = open('gugu.txt', 'w')
for i in range(1, 10):
    for j in range(1, 10):
        f1.write(str(i*j))


f2 = open('gugu.txt', 'w')
for i in range(1, 10):
    for j in range(1, 10):
        f1.write("{}\n".format(str(i*j)))


f1 = open('gugu.txt', 'r')
a = list(f1.readline())
'.'.join(a)


import copy


def gender():
    user = input("성별(남/여) :\t")
    if user not in ['남', '여']:
        return '남'
    else:
        return user


def user_info_view():
    while True:
        findname = input("찾는 이름 :\t")
        for i in range(len(user_list)):
            if findname in user_list[i].values():
                for j, k in user_list[i].items():
                    print("{} : {}".format(j, k))
            if findname not in user_list[i].values():
                print("없는 이름입니다.")
                continue
        break


def user_find(findname):
    for i in range(len(user_list)):
        if findname in user_list[i].values():
            return i


def birth():
    user = input("생년월일 :\t")
    for i in user:
        if i not in "0123456789":
            delimiter = i
            year, month, day = user.split(delimiter)[0], user.split(delimiter)[1], user.split(delimiter)[2]
            break
    if len(user) == 6:
        year, month, day = user[:2], user[2:4], user[4:]
    if len(user) == 8:
        year, month, day = user[:4], user[4:6], user[6:]
    if len(year) == 2:
        if int(year) >= 21:
            year = '19' + year
        else:
            year = '20' + year
    return year + '/' + month + '/' + day


def age(birth):
    return 2020 - int(birth[:4]) + 1    


def phone():
    user = input("전화번호 :\t")
    for i in user:
        if i not in "0123456789":
            delimiter = i
            a, b, c = user.split(i)[0], user.split(i)[1], user.split(i)[2]
            break
    if len(user) == 11:
        a, b, c = user[:3], user[3:7], user[7:]
    return a + '-' + b + '-' + c


def add_save():
    a=input("추가로 수정하시겠습니까?(y or n) : ")
    if a == 'n' :
        return 0
    else:
        return 1


menu = '''

==========
1.정보 입력
2.정보 확인
3.정보 수정
4.나가기
==========

'''

user_list = []
user_info = {'이름': '', '성별': '', '생년월일': '','나이': '','전화번호': '','지역': ''}
f3 = open('user_info.txt', 'a')

while True:
    choice = input(menu)
    if choice not in "1234":
        print("1, 2, 3, 4중 입력해주세요.")
        continue

    if choice == '4':
        print("명부 프로그램을 종료합니다.")
        f3.close()
        break
    
    if choice == '1':
        dict1 = user_info.copy()
        dict1['이름'] = input("이름 :\t")
        dict1['성별'] = gender()
        dict1['생년월일'] = birth()
        dict1['나이'] = age(dict1['생년월일'])
        dict1['전화번호'] = phone()
        dict1['지역'] = input("지역 :\t")
        user_list.append(dict1)
        for i in dict1.values():
            f3.write("{},".format(str(i)))
        f3.write("\n")
        print(user_list)
    
    if choice == '2':
        user_info_view()
        
    if choice == '3':
        find_index = user_find(input("이름 검색 :\t"))
        find_dict = user_list[find_index]
        while 1:
            choice1 = input(choice1=input('''
1.생년월일
2.전화번호
3.지역

수정하고자 하는 항목을 적으시오 : '''))
            print("")
            if choice1 == '1':
                save_birth=birth()
                print("")
                save_age=age(save_birth)
                find_dict["생년월일"]=save_birth
                find_dict["나이"]=save_age
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()
                if a==0:
                    break
                else:
                    continue
            if choice1 == '2':
                save_tel = phone()
                print("")
                find_dict["전화번호"]=save_tel
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()                
                if a==0:
                    break
                else:
                    continue
            if choice == '3':
                save_area = input("지역 : ")
                print("")
                find_dict["지역"]=save_area
                for i,j in find_dict.items():
                    print("{} : {}".format(i,j))        
                a=add_save()
                if a==0:
                    break
                else:
                    continue
            print("")        


with open('user_info.txt', 'r') as f:
    for i in f.readlines():
        print(i)


with open('user_info.txt', 'r') as f:
    for i in f.readlines():
        if '서울' in i:
            print(i)