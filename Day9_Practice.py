# 예외처리 실습

try:
    a = {'a': 1, 'b': 3, 'c': 5}
    print(a['d'])
except:
    print("오류가 발생하였습니다.")
    

try:
    print(5 / 0)
except ZeroDivisionError:
    print("분모가 0입니다.")
    

try:
    print(a)
except NameError:
    print("존재하지 않는 변수입니다.")
    

try:
    print(5 / 0)
    print(a)
except (ZeroDivisionError, NameError):
    print("다시 코딩하시오.")


try:
    print(a)
except NameError as e:
    print(e)
    
    
f = open("test.txt", 'r')

try:
    print(a)
finally:
    f.close()
    

class Test:
    def test(self):
        raise NotImplementedError

class Test1(Test):
    def test(self):
        print("Test1의 함수입니다.")


class MyError(Exception):
    def __str__(self):
        return "'A'를 입력하지마시오."

try:
    string = input("string을 입력하시오 : ")
    if 'A' in string:
        raise MyError()
    else:
        print(string)
except MyError as e:
    print(e)