#Decorators

#Function Based Decorator:
'''
#1.
def outer(fun):
    def inner(name):
        print("Program Start")
        fun(name)
        print("Program Ends")

    return inner

@outer
def hello(name):
    print(f"Good eveining..{name}")

hello("ved")

#2.
def outer(fun):
    def inner(a,b):
        if b == 0:
            print("Division by Zero not possible")
        else:
            fun(a,b)

    return inner

@outer
def div(a,b):
    res = a/b
    print(f"Qutient is: {res}")

div(20,4)
'''

#Class Based decorator
'''
3.
class Decor:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self,name):
        print('Program Starts')
        self.fun(name)
        print('Program Ends')

@Decor
def hello(name):
    print(f'Good eveing...{name}')

hello('Ved')


4.
class Check:
    def __init__(self, fun):
         self.fun = fun
         
    def __call__(self, a, b):
        if b == 0 :
            print('Not divisible by Zero')
        else:
            self.fun(a,b)


@Check
def div(a,b):
    res = a /b
    print(f'Qutient is: {res}')

div(20,4)
'''

'''
5.
def discount(fun):
    def inner(*n):
        d_pct = int(input('How much discount do you want to give '))
        total_amt = fun(*n)
        discount_amt = (total_amt * d_pct)/100
        return total_amt - discount_amt

    return inner

@discount
def total(*n):
    res = sum(n)
    return res

print(f'total Bill : {total(10,20,30,40,50,60,70,80,90,100)}')
'''

6.
class Discount:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *n):
        d_pct = int(input('How much discount do you want to give '))
        total_amt = self.fun(*n)
        discount_amt = (total_amt * d_pct)/100
        return total_amt - discount_amt



@Discount
def total(*n):
    res = sum(n)
    return res

print(f'total Bill : {total(10,20,30,40,50,60,70,80,90,100)}')










    


