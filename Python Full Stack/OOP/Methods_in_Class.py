'''
class A:
    x = 10
    def m1(self):
        print("m1...called")
a1 = A()
print(a1.x)
a1.m1()
a1.name = "Ved" #Instance
print(a1.name)

a2 = A()
a2.m1()
#OR
A.m1(a2)
'''
'''
class Cal:
    def sum(self,a,b):
        print("add =", a+b)
    def sub(self,a,b):
        print("sub =", a-b)
c = Cal()
c.sum(20,10)
c.sub(20,10)
print()

class Mobile:
    company_name = " "
    storage = " "
    camera = " "
    def call(self):
        print("for calling...")
    def message(self):
        print("for Messaging...")
    def photo(self):
        print("for capturing...")

m1 = Mobile()
m1.company_name = "Apple"
m1.storage = "128GB"
m1.camera = "30px"
m1.color = "Black"

m2 = Mobile()
m2.company_name = "Samsung"
m2.storage = "256GB"
m2.camera = "48px"
m2.color = "Sliver"

print("MOBILE INFORMATION")
print("m1 object")
print("Company :" , m1.company_name)
print("Storage :" , m1.storage)
print("Camera :" , m1.camera )
print("Color :" , m1.color)
m1.call()
m1.message()
m1.photo()
print()

print("m2 object")
print("Company :" , m2.company_name)
print("Storage :" , m2.storage)
print("Camera :" , m2.camera )
print("Color :" , m2.color)
m2.call()
m2.message()
m2.photo()
print()
'''

class Student:
    Roll_No = " "
    Nmae = " "
    Marks = " "

    def lecture(self):
        print("For Lecture.....")
    def subject(self):
        print("For subject....")
    def time(self):
        print("for timing")

s1 = Student()
s1.Roll_No = "101"
s1.Name = "Ved"
s1.Marks = "90"

print("\nSTUDENT INFO")
print("Roll No: ", s1.Roll_No)
print("Name: ", s1.Name)
print("Marks ", s1.Marks)
s1.lecture()
s1.subject()
s1.time()



s2 = Student()
s2.Roll_No = "102"
s2.Name = "Vedang"
s2.Marks = "80"

print("\nSTUDENT INFO")
print("Roll No: ", s2.Roll_No)
print("Name: ", s2.Name)
print("Marks ", s2.Marks)
s2.lecture()
s2.subject()
s2.time()





    
