#1. List Comprehension

#Normal way

li = []
for i in range(1,11):
    li.append(i**2)
print(li)

#Using List Comprehension

squares = [i**2 for i in range(1,11)]
print(squares)

#if statement in List Comprehension

res = [i for i in range(1,11)  if(i%2 == 0)]
print(res)

# if-else statement in List Comprehension

res = [i**2 if(i%2 == 0) else(i**3) for i in range(1,11)]
print(res)


#2. Set Comprehension

#Using Set Comprehension

squares = {i**2 for i in range(1,11)}
print(squares)


#3. Dictionary Comprehension

squares = {i : i**2 for i in range(1,11)}
print(squares)


#4. Generator Comprehension

squares = (i**2 for i in range(1,11))
for i in squares:
    print(i)


