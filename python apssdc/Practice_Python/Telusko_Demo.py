#print("Welcome to Programming world !!!")
'''
class Computer:
    def config(self):
        print("i5 ,  16GB , 1TB")


comp1 = Computer()
comp1.config()

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram=ram
    def config(self):
        print("Config is ",self.cpu,self.ram)

comp1 = Computer('i5',16)
comp2 = Computer('i3',4)

comp1.config()
comp2.config()

#Constructor
class Computer:
    name = "vinod"
    age= 20
    def __intit__(self):
        self.name="vinod"
        self.age=20
    def update(self):
        self.age=12
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c2.name
c1.update()
c1.name ="Kumar"
c1.age = 22

print(c1.name)
print(c1.age)
print(c2.name)

if c1.compare(c2):
    print("same")
else:
    print("not same")

#types of variables inpython
class Car:
    wheels = 4#static variable
    def __init__(self):
        self.mil=10 # instance variables
        self.com="BMW" # instance variables

c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 5
print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)

#types of methods in python --> instance,class,static
#instance variables
class Student:
    school="Winzcode"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3


s1 = Student(35,45,55)
s2 = Student(35,55,44)

s1.avg()
print(s1.avg())
print(s2.avg())
 
#Class method
class Student:
    school="WInzcode"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
#@class method
    def info(cls):# fetching value from outside the class is called class method
        return cls.school

print(Student.info())

dont accesing any elements from the class variables are instance variables then it is static

#inner class in python
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap= self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand = "Lenova"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("Vinod",445)
s2 = Student("Kumar",560)
#s1.show()
lap1 = Student.Laptop()

#Inheritance in python
class A:
    def feature1(self):
        print("F1")
    def feature2(self):
        print("F2")
class B(A):
    def feature3(self):
        print("F3")
    def feature4(self):
        print("F4")
class C(B,A):
    def feature5(self):
        print("F5")


#a1 = A()
#a1.feature1()
c1 = C()
c1.feature1()

#super keyword is used to refer object of super class from the sub class using syntax:- super().__init__()
class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("F1")
    def feature2(self):
        print("F2 in A")
class B(A):
    def __init__(self):
        print("In B init")
        super().feature2()
    def feature2(self):
        print("F2 in B")
a1 = B()
a1.feature2()

#Polymorphism->Many Forms
#four types of polymorphisms 1.Duck Typing 2.Operator Overloadng 3.Method Overloading 4.Method Overriding
class pycharm:
    def excute(self):
        print("Run")
        print("Compile")
class Myeditor:
    def excute(self):
        print("Spell check")
        print("Run")
class Laptop:
    def code(self,ide):
        ide.excute()

ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)

#operator overloading
a=5
b=6
print(a+b)
print(int._add__(a,b))


class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1+other
        m2 = self.m2+other
        s3 = Student(m1,m2)
        return s3

s1 = Student(2,3)
'''

















