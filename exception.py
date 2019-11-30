class MyException:
    def __init__ (self,c):
        self.c=c
    def __str__ (self):
        return str(self.c)

class Xyz:
    a=int(input())
    b=int(input())
    sum=a+b
    if sum>150:
        print(sum)
    else:
        x=MyException("Custom Exception Occurred")
        print(x)
