'''
mark = int(input("Enter any no: "))
if mark < 40:
    print("F")
elif mark >= 80:
    print("A")
elif mark >= 60:
    print("B")
elif mark >= 40:
    print("P")

n = int(input("Enter any no"))
if n%2 == 0:
    print("Even no")
else:
    print("Odd no")
'''


while True:
    n = int(input("Enter any no"))
    
    if n>=0 and n <= 100:
        print(500)
        print("to exit enter -1")
    
    elif n > 100 and n <= 200:
        n = n - 100
        print(500 + n * 5)
        print("to exit enter -1")

    elif n>200:
        n = n - 200
        print(500 + 500 + n * 10)
        print("to exit enter -1")

    else:
        print('Exit')
        break

 
