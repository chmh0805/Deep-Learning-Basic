# fourcal.py

def numfind():
	while True:
		num=input("number : ")
		a=0
		for c in num:
			if c not in "0123456789.":
				print("숫자로 다시 입력해주세요")
				a=a+1
				break
		if a==0:
			if num.count('.') > 1:
				print("숫자로 다시 입력해주세요")
			elif num.count('.') ==1:
				return float(num)
			else:
				return int(num)	


def add(a,b,c):
	return a+b+c

def sub(a,b,c):
	return a-b-c

def mul(a,b,c):
	return a*b*c

def div(a,b,c):
	return a/b/c
    
class Morefourcal:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def jasung(self):
        return (self.n1 ** self.n2) ** self.n3


if __name__ == "__main__":
    print(add(1,2,3))
    print(sub(1,2,3))
    print(mul(1,2,3))
    print(div(1,2,3))