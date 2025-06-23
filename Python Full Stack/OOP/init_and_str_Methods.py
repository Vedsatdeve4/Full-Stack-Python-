'''
class Student:
    def __init__(self, r, n, m):
        self.roll = r
        self.name = n
        self.mark = m

    def display(self):
        print('\nSTUDENT INFO')
        print("Roll No: ", self.roll)
        print("Name: ", self.name)
        print("Marks: ", self.mark)

s1 = Student(101, 'Ved', 100)
s2 = Student(102, 'Vedang', 90)

s1.display()
s2.display()
'''

'''
class Student:
    def __init__(self, r, n, m):
        self.roll = r
        self.name = n
        self.mark = m

    def __str__(self):
        return f"\n Roll No: {self.roll} \n Name: {self.name} \n Marks: {self.mark}"


s1 = Student(101, 'Ved', 100)
s2 = Student(102, 'Vedang', 90)

print(s1)
print(s2)
'''
'''
# HW
class Mobile:
    def __init__(self, b, c, s):
        self.brand = b
        self.color = c
        self.storage = s

    def display(self):
        print("\n MOBILE INFO")
        print("Brand =" , self.brand)
        print("Color =", self.color)
        print("Storage =", self.storage)

m1 = Mobile('Apple', 'White' , '128GB')
m2 = Mobile('Samsung' , 'Black' , '256GB')

m1.display()
m2.display()
'''

class Mobile:
    def __init__(self, b, c, s):
        self.brand = b
        self.color = c
        self.storage = s

    def __str__(self):
        return f"\n Brand: {self.brand} \n Color: {self.color} \n Storage: {self.storage} "

m1 = Mobile('Apple', 'White' , '128GB')
m2 = Mobile('samsung' , 'Black' , '256GB')

print(m1)
print(m2)
