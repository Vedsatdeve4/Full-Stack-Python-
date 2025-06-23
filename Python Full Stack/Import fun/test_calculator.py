
#1 method
'''
import calculator as cal

while True:
    ch = int(input("\n Enter Choice: \n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Exit"))

    if ch == 1:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        cal.add(n1,n2)

    elif ch == 2:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        cal.sub(n1,n2)


    elif ch == 3:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        cal.mul(n1,n2)

    elif ch == 4:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        cal.div(n1,n2)

    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invali Choice")'''


#2 method

'''
import calculator

while True:
    ch = int(input("\n Enter Choice: \n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Exit"))

    if ch == 1:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        calculator.add(n1,n2)

    elif ch == 2:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        calculator.sub(n1,n2)


    elif ch == 3:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        calculator.mul(n1,n2)

    elif ch == 4:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        calculator.div(n1,n2)

    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invali Choice")'''

#3 method
'''
from calculator import add,sub,mul,div

while True:
    ch = int(input("\n Enter Choice: \n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Exit"))

    if ch == 1:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        add(n1,n2)

    elif ch == 2:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        sub(n1,n2)


    elif ch == 3:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        mul(n1,n2)

    elif ch == 4:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        div(n1,n2)

    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invali Choice")'''


#4 method
from calculator import *

while True:
    ch = int(input("\n Enter Choice: \n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Exit"))

    if ch == 1:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        add(n1,n2)

    elif ch == 2:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        sub(n1,n2)


    elif ch == 3:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        mul(n1,n2)

    elif ch == 4:
        n1 = int(input("Enter First Value: "))
        n2 = int(input("Enter Second Value: "))
        div(n1,n2)

    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invali Choice")
