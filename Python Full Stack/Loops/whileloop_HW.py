'''
# program of multipication table
i = 1
n = int(input("Enter any no"))
while i < 11:
    mul = n * i
    print(n , " * " , i , " = " , mul)
    i = i + 1'''

'''
#program of odd number
n = int(input("Enter any no"))
i = 1
a = 0
while i < n:
    if i % 2 != 0 :
        a = a + i
    i = i + 1
print(a)'''
   
'''
#program of even Number
n = int(input("Enter any no"))
i = 1
a = 0
while i < n:
    if i % 2 == 0 :
        a = a + i
    i = i + 1
print(a)'''


'''
# program of first ten natural Numbers
i = 1
while i < 11:
    print(i)
    i = i + 1'''

'''
# program of fibonaccie series
n1 = 0
n2 = 1
print(n1)
print(n2)

i = 0
while i < 8:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1
    print(n3)'''


'''
#Program to check whether the given Number is prime or Not
i = 1
c = 0
n = int(input("enter a no: "))
while i <= n:
    if n % i == 0:
        c = c + 1
    i = i +1   
if c == 2:
    print('prime')
else:
    print('not prime')'''

# program to print sequence of prime Number
i = 1
n = int(input("enter a no: "))
while i <= n:
    c = 0
    j= 1
    while j <= i:
        if i % j == 0:
            c = c + 1
        j = j + 1
    if c == 2:
        print(i)
    i = i +1  
print()

       


 
    
    
