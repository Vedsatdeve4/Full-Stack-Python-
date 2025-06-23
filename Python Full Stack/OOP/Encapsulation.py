#Encapsulation

#Public: Can be acessible inside and ouside of the class.

#Protected: Can be acessible inside and ouside of the class.But it is a hit to
# the developer to not change the values.

#Private: Can only be acessible inside the class.

class A:
    x = 10     #Public
    _y = 20    #Protected
    __z = 30   #Private

a = A()
print(a.x)
print(a._y)
#print(a.__z)  #Error
print(a._A__z) # Illegal way to acesses private data
print()

class Student:
    __roll = 0
    __name = " "
    __marks = 0.0

    def setRoll(self, r):
        self.__roll = r
        
    def setName(self, n):
        self.__name = n
        
    def setMarks(self, m):
        self.__marks = m
        
    def getRoll(self):
        return self.__roll
    
    def getName(self):
        return self.__name
    
    def getMarks(self):
        return self.__marks

s1 = Student()

print("Roll number: " , s1.getRoll())
print("Name: " , s1.getName())
print("Marks: " , s1.getMarks())
print()

s1.setRoll(101)
s1.setName("Ved")
s1.setMarks(93.21)

print("Roll number: " , s1.getRoll())
print("Name: " , s1.getName())
print("Marks: " , s1.getMarks())
print()



class Empeloy:
    __department = " "
    __name = " "
    __assign = " "

    def setDepartment(self, d):
        self.__department = d
        
    def setName(self, n):
        self.__name = n
        
    def setAssign(self, a):
        self.__assign = a
        
    def getDepartment(self):
        return self.__department
    
    def getName(self):
        return self.__name
    
    def getAssign(self):
        return self.__assign

s1 = Empeloy()

print("Department: " , s1.getDepartment())
print("Name: " , s1.getName())
print("Assign: " , s1.getAssign())
print()

s1.setDepartment("Management")
s1.setName("Ved")
s1.setAssign("Digital MArketing")

print("Department: " , s1.getDepartment())
print("Name: " , s1.getName())
print("Assign: " , s1.getAssign())
print()




        
