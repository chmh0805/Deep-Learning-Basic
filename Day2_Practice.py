# 9.2 실습
'''
name = input("name : ")
age = int(input("age : "))
birthday = int(input("birthday(XXXXXXXX) : "))

print("나의 이름은 {} 입니다.".format(name))
print("나의 나이는 {}이며 {}대 입니다.".format(age, age//10*10))
print("나의 생일은 {}입니다.".format(birthday))
'''

week = ['월', '화', '수', '목', '금', '토', '일']

print("솔로몬 그런디는")
for day in week:
    if day == '월':
        print(day + "요일에 태어나서")
    if day == '화':
        print(day + "요일에 세례받고")
    if day == '수':
        print(day + "요일에 결혼하고")
    if day == '목':
        print(day + "요일에 병들어서")
    if day == '금':
        print(day + "요일에 악화되어")
    if day == '토':
        print(day + "요일에 눈을 감아")
    if day == '일':
        print(day + "요일에 묻혔다네")
print('''솔로몬 그런디는
그렇게 살다 갔네''')

for i in range(1, 51):
    print(str(i) + ',' + ' Victory')

def average(x, y, z):
    return (x + y + z) / 3
print(average(1, 2, 3))

num1 = 40
num2 = 30
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
print(bin(num1 * num2))
print(oct(num1 * num2))
print(hex(num1 * num2))

string1 = "My life"
string2 = " is mine."
string3 = string1 + string2

print(string3[:7])
string4 = string3[-5:-1]
print(string4)

print('''Your life is
yours''')

# 문자열 포맷팅 실습

print("나는 아침마다 %d잔의 우유를 마시고 %s를 봅니다."%(1, '네이버뉴스'))
print('%-14s'%'hello')
print('%10s'%'bye')
print('%.5f'%2.5679856)
print('%15.3f'%2.5679856)

# 문자열 함수 실습

string1 = "My life is mine."
string2 = string1.upper()
print(string2)
string3 = string2.lower()
print(string3)

string4 = string1.swapcase()
print(string4)

print(string2.count('m'))
print(string3.find('M'))

print(';'.join('12345'))

string4 = string1.replace('My', 'Your')
print(string4)

print("192.168.100.40".split('.'))
print(','.join('abcdef').split(','))


# list 실습

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alpha = ['a', 'b', 'c', 'd', 'e']

numalp = number + alpha
print(numalp)

numalp[8:11]=[]
numalp.insert(7, [11, 12, 13])
print(numalp)
numalp[0:3] = [21, 22, 23]
numalp.append(100)
number[:] = []

# 에러발생 해결용
for i in range(len(numalp)):
    numalp[i] = str(i)

# 에러발생 : 정수와 문자열, 리스트 형태의 요소까지 섞여있음.
numalp.sort()
print(numalp)
numalp.reverse()
print(numalp)

numalp.insert(2, ['ㄱ', 'ㄴ', 'ㄷ'])
print(numalp)
numalp.pop(numalp.index(['ㄱ', 'ㄴ', 'ㄷ']))
print(numalp)

numalp1 = [x for x in numalp[::-1]]
# (방법 2)
numalp2 = []
for i in numalp:
    numalp2.insert(0, i)

# (방법 3)
numalp3 = []
i = 0
while i == 0 :
    numalp3.append(numalp.pop())
    if numalp == []:
        i += 1

print("numalp1 : {}".format(numalp1))
print("numalp2 : {}".format(numalp2))
print("numalp3 : {}".format(numalp3))

alpha3 = alpha*3
alpha3.sort()

new_string = ''
for i in alpha3:
    new_string += i
    
print(new_string)