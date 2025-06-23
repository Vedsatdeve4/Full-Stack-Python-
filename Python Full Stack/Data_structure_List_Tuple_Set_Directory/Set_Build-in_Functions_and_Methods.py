# Set in Python

#Empty Set
s1 = set()
print("s1=",s1)
print("type of s1=", type(s1))
print()

#Unordered Set
s2 = {10,20,30,40,50}
print("s1=",s2)
print()

#hetrogeneous Set
s3 = {10,'Ved',3.14,False}
print("s1=",s3)
print()

#Does not allows duplicate elements
s4 = {10,20,30,40,50,10,10,10}
print("s1=",s4)
print()


#Does not supports any type indexing
# print("s4[1]=", s4[1])   #Error
# print("s4[-1]=", s4[-1])   #Error

#Does not supports slicing operation
# print("s4[0:5:1]=", s4[0:5:1])   #Error

#Build-in Function on Set
s5 = {10,20,30,40,50}
print("li5 =", s5)
print("max =", max(s5))
print("min =", min(s5))
print("len =", len(s5))
print("sorted =", sorted(s5))
print("sorted_rev =", sorted(s5, reverse= True))
print()

#Bulid-in Method on Set


#Insertion

#1. To add a single element in Set
s5.add(60)
print("s5=", s5)

#2. To add a multiple element in Set
s5.update({70,80,90})
print("s5=", s5)
print()

#Remove

#1.To remove a random element from Set
s5.pop()
print("s5=", s5)

#2.To remove a particular element from Set
s5.remove(50)
print("s5=", s5)

#3.To clear all the element from the Set
s5.clear()
print("s5=", s5)
print()


#Union:
s6 = {10,20,30,40,50}
s7 = {40,50,60,70,80}
print()

print("Union")
print("union=" , s6 | s7)
print("union=" , s7 | s6)
print("union=" , s6.union(s7))
print("union=" , s7.union(s6))
print()

#Intersection:

print("Intersection")
print("intersection=" , s6 & s7)
print("intersection=" , s7 & s6)
print("intersection=" , s6.intersection(s7))
print("intersection=" , s7.intersection(s6))
print()


#Difference

print("Difference")
print("difference=" , s6 - s7)
print("difference=" , s6.difference(s7))
print("difference=" , s7 - s6)
print("difference=" , s7.difference(s6))
print()











