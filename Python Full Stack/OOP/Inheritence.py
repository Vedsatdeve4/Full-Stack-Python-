# Single Inheritence

class Parent_class:
    x= 10
    def m1(self):
        print("method of parent class ")
class Child_class(Parent_class):
    def m1(self):
        print("method of child_class")

cobj = Child_class()

cobj.m1()
cobj.m1()
print(cobj.x)
print()

#Multiple Inheritence

class Parent1_class:
    x= 10
    def m1(self):
        print("method of parent1 class ")

class Parent2_class:
    y= 100
    def m2(self):
        print("method of parent2 class ")

class C_class(Parent1_class, Parent2_class):
    def m3(self):
        print("method of child_class")

chobj = C_class()

chobj.m1()
chobj.m2()
chobj.m3()
print(chobj.x)
print(chobj.y)
print()

#Hierarchical Inheritance

class Parent:
    x = 10
    def m(self):
        print("parent class")
class Child1(Parent):
    y = 20
class Child2(Parent):
    z = 30
c1 = Child1()
c2 = Child2()

print(c1.x)
print(c1.y)
c1.m()
print()

print(c2.x)
print(c2.z)
c2.m()
print()

#Multilevel Inheritance

class A:
    x = 10
class B(A):
    y = 20
class C(B):
    z = 30

c = C()
print(c.x)
print(c.y)
print(c.z)
print()

# Hybrid Inheritance

class A:
    x = 10
class B(A):
    y = 20
class C(A):
    z = 30
class D(B,C):
    pass

d = D()
print(d.x)
print(d.y)
print(d.z)
print(D.mro())


