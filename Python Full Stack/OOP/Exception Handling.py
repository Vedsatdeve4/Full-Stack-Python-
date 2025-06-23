#Exceptoin Handling

#1. using Try and Except

print("Program Start")

try:
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))

    res = a/b
    print(f"Quotient is: {res}")

except ValueError:
    print("Enter correct value")

except ZeroDivisionError:
    print("Cannot be divide by zero")

print("End Program")
print()

#2. using Try and Except in Function
print("2.")
def div(a,b):
    try:
        res = a/b
        print(f"Quotient is: {res}")
    
    except ZeroDivisionError:
        print("Cannot be divide by zero")

div(20,0)
div(20,5)

print()

#3. using Try, Except and Else in Function

print("3.")
def div(a,b):
    try:
        res = a/b
    
    except ZeroDivisionError:
        print("Cannot be divide by zero")

    else:
        print(f"Quotient is: {res}")

div(20,0)
div(20,5)
print()



#4. types of exception Handling

#ArithmeticError: Raised when an error occurs in numeric calculations
#1.OverFlowError
#2.ZeroDivisionError
#3.FloatingPointError

print("4.")

try:
  a = 5/0
  print(a)
except ArithmeticError:
  print('You have just made an Arithmetic error')


#AttributeError : Raised when attribute reference or assignment fails

try:
    x = 3
    x.append(4)
    print(x)
except AttributeError:
    print("Attribute Error has occured please check your code again")



# EOFError: Raised when the input() method hits an "end of file" condition (EOF)
'''
try:
    num = int(input())
    print(num * 10)
    
except EOFError:
    print("end of file error occured")
'''


#NameError: Raised when a variable does not exist

def assign():
    a = "Ved"

assign()
try:
    print(a)
except NameError:
    print("NameError has occured")


#IndexError : Raised when an index of a sequence does not exist

try:
    li = [1,2,3,4]
    print(li[5])
except IndexError:
    print("IndexError has occured")

# KeyError : Raised when a key does not exist in a dictionary

dict = {'a' : 10,
        'b' : 20,
        'c' : 30}
try:
    print(dict['d'])
except KeyError:
    print('KeyError has occured')

#TypeError: Raised when two different types are combined

try:
    a = 1
    b = 'abc'
    print(a+b)
except TypeError:
    print("TypeError has occured")
print()



#5. Finally block

print("5.")

def div(a,b):
    try:
        res = a/b
    except ZeroDivisionError:
        print("Cannot be divide by zero")
    else:
          print(f"Quotient is: {res}")
    finally:
        print("Div Ends")

div(20,0)
print()

div(20,5)

print()


#6. Exception propagation

print("6.")

#1.

def div(a,b):
    res = a/b
    print(res)
try:
    div(20,0)
except ZeroDivisionError:
    print("Cannot be divide by zero")

print()

#2.

li = ['a', 'b', 'c', 'd', 'e', 'f']

ele = input("Enter the Elements: ")
try:
    print(f"Index position of {ele}:{li.index(ele)}")
except ValueError:
    print(f'Element : {ele} not present in the list')

print()



#7. Rasie Keyword
#8. Custom Exception in python

class VotingEligibility(BaseException):

    def __init__(self, msg):
        self.msg = msg

try:
    age = int(input("Enter your Age: "))

    if age < 18:
       raise VotingEligibility('Sorry you cannot vote')

except (VotingEligibility, ValueError):
    print("Exception handeled")

else:
    print("You are eligible to vote")
    






