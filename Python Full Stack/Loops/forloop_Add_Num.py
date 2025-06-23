
s = 0
for i in range(0,11,1):
    s += i
print(s)

'''q = 0
for i in range(0,11,2):
    q += i
print(q)

p = 0
for i in range(100,9,-10):
    p += i
print(p)'''

def prim(n):
    if n > 1:
        for i in range(2,n,1):
            if n % i == 0 :
                print("not prime")
                break
            else:
                print("prime")
                break
    else:
        print("not prine")
    
m = int(input("Enter no: "))
prim(m)
'''
def prim(n):
    c = 0
    if n > 1:
        for i in range(1,n+1,1):
            if n % i == 0 :
                c = c+ 1

        if c == 2:
            print("prime")
        else:
            print("not prine")
    
m = int(input("Enter no: "))
prim(m)'''
