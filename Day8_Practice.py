# 9/10 실습

# 클래스 실습

class Car:
    def __init__(self, user, color):
        self.user = user
        self.color = color


class Sports(Car):
    def __init__(self, user, color):
        self.baegi = '5000cc'
        self.gudong = '후륜'
        self.high = '300km/h'


class Suv(Car):
    def __init__(self, user, color):
        self.baegi = '3000cc'
        self.gudong = '4륜'
        self.high = '200km/h'


class Truck(Car):
    def __init__(self, user, color):
        self.baegi = '6000cc'
        self.gudong = '4륜'
        self.high = '200km/h'


def search(name):
    print('''
    차량주인 : {}
    차량색깔 : {}
    차종 : {}
    배기량 : {}
    구동 : {}
    최고속도 : {}
    '''.format(name, user_dict[name][0], user_dict[name][1], user_dict[name][2], user_dict[name][3], user_dict[name][4]))


def more():
    while True:
        choice_more = input("\n\n계속해서 사용하시겠습니까?(y or n): ").lower()
        while True:
            if choice_more not in ['y', 'n']:
                print("y 또는 n을 입력해주세요.")
                continue
            else:
                break
        if choice_more == 'y':
            return True
        else:
            return False


user_dict = {}
car_list = ['sports', 'suv', 'truck']

menu = '''
============
    메뉴
A. 차량등록
B. 차주검색
C. 나가기
============
메뉴를 선택하세요.

'''

while True:
    while True:
        choice = input(menu).upper()
        if choice not in ['A', 'B', 'C']:
            print("메뉴를 정확히 입력해주세요.")
            continue
        else:
            break
    
    if choice == 'C':
        print("시스템을 종료합니다.")
        break
    
    if choice == 'A':
        user_name = input("차주 : ")
        user_color = input("색깔 : ")
        while True:
            user_car = input("차종 : (sports, suv, truck 중 택일) ").lower()
            if user_car not in car_list:
                print("차종을 확인해주세요.")
                continue
            else:
                break

        if user_car == "sports":
            user_name_class = Sports(user_name, user_color)
            user_dict[user_name] = (user_color, user_car, user_name_class.baegi, user_name_class.gudong, user_name_class.high)
        elif user_car == "suv":
            user_name_class = Suv(user_name, user_color)        
            user_dict[user_name] = (user_color, user_car, user_name_class.baegi, user_name_class.gudong, user_name_class.high)
        elif user_car == "truck":
            user_name_class = Truck(user_name, user_color)        
            user_dict[user_name] = (user_color, user_car, user_name_class.baegi, user_name_class.gudong, user_name_class.high)
    
    if choice == 'B':
        print("차주 리스트")
        print("============")
        for i in list(user_dict):
            print(i)
        print("============")
        while True:
            user_find = input("차주 검색: ")
            if user_find not in user_dict.keys():
                print("차주가 존재하지 않습니다. 확인해주세요.")
                continue
            else:
                break
        if user_find in user_dict.keys():
            search(user_find)
            
    if more():
        continue
    else:
        print("시스템을 종료합니다.")
        break
        
    
# 모듈 실습

