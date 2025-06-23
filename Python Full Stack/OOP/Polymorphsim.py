#Polymorphism

#1. Overriding

class A:
    def add(self,x,y):
        print("add = ", x+y)
class B(A):
    def add(self,x,y,z):
        print("add = ", x+y+z)
b = B()
b.add(10,20,30)
#b.add(10,20) #Error
print()

#2. Overloading: using third party library

from multipledispatch import dispatch

@dispatch(str,str)
def add(x,y):
    print("add = ", x+y)
@dispatch(int, int, int)
def add(x,y,z):
    print("add = ", x+y+z)

add(10,20,30)
add("10", "20")
print()


from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def add(x,y):
        print("add = ", x+y)
    @dispatch(int, int, int)
    def add(x,y,z):
        print("add = ", x+y+z)
a = A()
a.add(10,20,30)
a.add(10,20)
print()

