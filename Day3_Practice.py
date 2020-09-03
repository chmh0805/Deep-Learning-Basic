# 9.3 실습


# input() 실습
num_sum = 0
for i in range(1, 6):
    a = input("{}번째 숫자를 입력하시오. :".format(i))
    num_sum += int(a)
    a = 0

print("모든 숫자를 더한 값은 {}이고 평균은 {}입니다.".format(num_sum, num_sum/5))


# 문자열 포매팅 실습
print("나는 %s %s 시험을 보았다."%('오늘', '영어'))
print("나의 점수는 %d점으로 상위 %.1f%% 점수이다."%(98, 0.1))

day = 'today'
print("%9s"%day)
print("%-14s"%day)

float1 = 1.2345678
print("%8.5f"%float1)
print("%-10.4f"%float1)


# 문자열 함수 실습
alph = "abcd efg hijk lmnop qrs tuv wxyz"
number = "1234 567 89"
boy = "BOYS, BE AMBITIOUS"

alph1 = alph.upper()
string1 = boy + alph1
print(string1.count('B'))
print(string1.find('A'))

string2 = boy.replace("BOYS", 'girls')
string2.swapcase()

alphlist = list(alph.replace(' ',''))
print(alphlist)


# list 실습

num1 = "0,1,2,3,4,5,6,7,8,9,10"
num2 = num1.split(',')

print(num2[2])
print(num2[4:8])
print(int(num2[4]) * int(num2[6]))
num2[5] = '45'
num2[2:8] = ['31', '33', '34', '35', '36', '37']
print(num2) # check
num2[8] = '33'

for num in num2:
    if num == '33':
        num2.remove('33')

num2.sort()
num2.reverse()
num2.insert(3, ['a1', 'b1', 'c1'])
num2[4] = ['a2', 'b2', 'c2']

a1 = num2.pop(num2.index(['a1', 'b1', 'c1']))
num2.remove(['a2', 'b2', 'c2'])

num3 = [int(num) for num in num2]
print(num3)

print(alphlist[alphlist.index('i')].upper() + ' ' + alphlist[alphlist.index('l')] + alphlist[alphlist.index('i')] + alphlist[alphlist.index('k')] + alphlist[alphlist.index('e')] + ' ' + alphlist[alphlist.index('p')].upper() + alphlist[alphlist.index('y')] + alphlist[alphlist.index('t')] + alphlist[alphlist.index('h')] + alphlist[alphlist.index('o')] + alphlist[alphlist.index('n')])


# 튜플 실습

a = ('a1', 'a2', 'a3', 'a4')
b = ('b1', 'b2', 'b3', 'b4')

q, w, e, r = a
c = a + b
print(c[2])
print(c[5:])
print(c[:3])
# 튜플 : 튜플 안의 값 제거 불가
# 튜플 : 튜플 안의 값 수정 불가

d = ('a', 'b', 'c', [1, 2, 3, 4])
print(str(d[-1][0]))
print(str(d[-1][1]))


# 딕셔너리 실습

srp = {'가위': '보', '바위': '가위', '보': '바위'}
srp_keys = list(srp.keys())
srp_values = list(srp.values())
srp_items = list(srp.items())
srp['가위'] #또는 srp.get('가위')
srp['찌'] = '빠'
srp['묵'] = '찌'
srp['빠'] = '묵'
'보자기' in srp.keys() #또는 '보자기' in srp

# value로 key 찾기(1)
for i, j in srp.items():
    if j == '가위':
        print("'가위'라고 하는 value값에 해당하는 key값 : {}".format(i))

# value로 key 찾기(2)
for key in srp.keys():
    if srp[key] == '가위':
        print(key)

# value로 key 찾기(3)
print(list(srp.keys())[list(srp.values()).index('가위')])

Key = ['a', 'b', 'c', 'd']
Value = [1, 2, 3, 4]
dict1 = {}

for i in range(len(Key)):
    dict1[Key[i]] = Value[i]
'''또는
i = 0
while Key != []:
    dict1[Key.pop(i)] = Value[i]
    i += 1
'''
print(dict1)


# 튜플 실습

a = [1, 2, 3, 4]
s1 = set(a)

b = "aabbccddeeff"
s2 = set(b)

s1.update(['a', 'b', 'c'])
s2.update([1, 2])

print(s1.intersection(s2))
print(s1&s2)

print(s1.union(s2))
print(s1|s2)

print(s1-s2)
print(s2.difference(s1))

s2.remove(1)