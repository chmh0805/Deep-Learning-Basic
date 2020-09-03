# 4번
a = "Hi, Kitri\n"
print(a * 3)

# 5번
name = "Minhyuk"
print("name은 {}".format(name))

# 6번
season = '겨울'
print("이번 '{}'은 추울 것 같습니다.".format(season))

# 7번
print("--------------------------")
print("이 문장은 출력이 됩니다.")
'''주석은
실행되지 않습니다.'''
print("이 문장도 출력이 됩니다.")
print("--------------------------")

# 8번
srp = "보자기"
if srp == "가위":
    print("이겼다")
else:
    if srp == "바위":
        print("졌다")
    else:
        if srp == '보':
            print("비겼다")
        else:
            print("잘못냈다")

# 9번
seasons = ['봄', '여름', '가을', '겨울']
for season1 in seasons:
    if season1 == '봄':
        print("현재 계절은 {} 입니다.".format(season1))
    else:
        print("현재 계절은 {}이 아닙니다.".format(season1))

# 10번
num = 0
while num <= 100:
    if num == 55:
        print("일치")
    else:
        print("불일치")
    num += 5

# 11번
def SRP(srp):
    if srp == "가위":
        result = "이겼다"
    else:
        if srp == "바위":
            result = "졌다"
        else:
            if srp == '보':
                result = "비겼다"
            else:
                result = "잘못냈다"
    return result
SRP("가위")    

# 자료형 실습
# 숫자형
print(17)
print(bin(17))
print(oct(17))
print(hex(17))

print(14 % 10)
print(4**20)
print(132 // 35)

# 문자열
a = "abcedf"
b = "12345"
c = a + b
print(b * 3)

print(c[2])
print(c[2], c[4], c[7])
print(c[3] + c[6] + c[7])
print(c[-4])
print(c[2:])
print(c[3:8])
print(c[-6:-2])
print(c[:])