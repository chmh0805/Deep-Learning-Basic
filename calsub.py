def numfind(i):
    while True:
        num=input("number{} : ".format(i))
        a=0
        for c in num:
            if c not in "0123456789.":
                print("숫자로 다시 입력해주세요")
                a=1
                break
            elif num.count('.') > 1:
                print("숫자로 다시 입력해주세요")
                a=1
                break
        if a==1:
            continue
        if num.count('.') ==1:
            return float(num)
        else:
            return int(num)


class Fourcal:
    def __init__(self,num1,num2,cal):
        self.num1=num1
        self.num2=num2
        self.cal=cal
        self.result=0
        
    
    def fourcal(self):
        if self.cal == '+':
            self.result=self.num1+self.num2
            print("{}{}{}={}".format(self.num1,self.cal,self.num2,self.result))
    
        if self.cal == '-':
            self.result=self.num1-self.num2
            print("{}{}{}={}".format(self.num1,self.cal,self.num2,self.result))
            
        if self.cal == '*':
            self.result=self.num1*self.num2
            print("{}{}{}={}".format(self.num1,self.cal,self.num2,self.result))

    def div(self):
        if self.cal == '/':
            self.result=self.num1/self.num2
            print("{}{}{}={}".format(self.num1,self.cal,self.num2,self.result))
    

class safeFourcal(Fourcal):
        
    def div(self):
        if self.num2==0:
            self.result=0
            print("분모가 0입니다.")
            
        else:
            self.result=self.num1/self.num2
            print("{}{}{}={}".format(self.num1,self.cal,self.num2,self.result))

