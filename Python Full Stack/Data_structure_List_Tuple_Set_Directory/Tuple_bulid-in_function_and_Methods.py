#Bulid-in Functions on Tuple
li6 = (50,20,30,40,10)
print("li6 =", li6)
print("max =", max(li6))
print("min =", min(li6))
print("len =", len(li6))
print("sorted =", sorted(li6))
print("sorted_rev =", sorted(li6, reverse= True))
print()

#Bulid-in Methods on tuple

#indexing
print(li6.index(50))
print(li6.index(10))
print()

#Counting
print(li6.count(10))
print(li6.count(99))
print()


#Tricks

#1. We can create a tuple without using any notation

x = 10,20,30,40,50
print("x=", x)
print("type of x=", type(x))
print()


#2. We must use a comma in tuple, specifically if you are using a
#   single element in Tuple

x = (10)
print("x=", x)
print("type of x=", type(x))

x= (10,)
print("x=", x)
print("type of x=", type(x))

y = ('Ved')
print("y=", y)
print("type of x=", type(y))

y = ('Ved',)
print("y=", y)
print("type of y=", type(y))


