# MAP FUNCTION
li = [1,2,3,4,5,6,7,8,9,10]

# By Using Normal way
squares = []

for i in li:
    sqr = i**2
    squares.append(sqr)

print(squares)

# Using MAP Function:
square = list(map(lambda num: num**2 ,li))
print(square)


#FILTER FUNCTION

#By Using Normal Way:

new_li = []
for i in li:
    if i%2 == 0:
        new_li.append(i)
print(new_li)


#Using Filter Function:
new_li1 = list(filter(lambda num: num%2 == 0, range(1,11)))
print(new_li1)


#REDUCE FUNCTION

li1 = [10,20,30,40,50,60,70,80,90,100]

from functools import reduce

res = reduce(lambda a,b: a+b, li1)
print(res)
