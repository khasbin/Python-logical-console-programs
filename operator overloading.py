class Student:
    def __init__(self, s1,s2):
        self.s1 = s1
        self.s2 = s2
    def __add__(self,others):
        s1 = self.s1 + others.s1
        s2 = self.s2 + others.s2
        s3  = s1+s2
        return s3

    def __gt__(self,others):
        a = self.s1+self.s2
        b = others.s1 + others.s2
        if a>b:
            return True
        else:
            return False


a = Student(50,60)
b = Student(100,30)

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print(a+b)