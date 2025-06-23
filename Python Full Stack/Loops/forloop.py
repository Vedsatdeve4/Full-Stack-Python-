'''for i in range(1,11,1):
    print(i)
print()

for i in range(5,51,5):
    print(i)
print()


for i in range(0,21,2):
    print(i)
print()

for i in range(100,9,-10):
    print(i)
print()

for i in range(1,11,1):
    print('Hello world')'''
'''
def table(n):
   
    for i in range(2,11,1):
        mul = n * i
        print(n,'*',i,'=',mul)
m = int(input("Enter any no: "))
table(m)'''



for i in range(1,12,1):
    c = 0
    for j in range(1,i+1,1):
        if i % j == 0:
            c = c + 1
    if c == 2:
        print(i)
print()
