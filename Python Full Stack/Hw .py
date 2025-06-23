li1 = [10,20,30,40,50,60,70,80,90,100]

#1 W.A.P to write a custom logic for len() function on list.

def length(li):
    count = 0
    for i in li:
        count = count + 1
    return count

print(length(li1))
print()


#2 W.A.P to find out max element from a list without using a build-in function.

def ele_max(li):
    max_element = li[0]
    if len(li) > 0:
        for i in li:
            if i > max_element:
                max_element = i
        return max_element
    else:
        return "Empty list"
print(ele_max(li1))
print()


#3 W.A.P to find out total of all elements in a list without using a build-in function

def ele_sum(li):
    total = 0
    for i in li:
        total = total + i
    return total
print(ele_sum(li1))
print()

    
#4.W.A.P to find out whether a particular element is present within the list or not

def ele_pre(li , ele):
    found = False
    for i in li:
        if ele == i:
            found = True
    return found

print(ele_pre(li1 , 50))
print()

#5 W.A.P to find a prime number 

def prime(n):
    count = 0
    if n > 1:
        for i in range(1,n+1,1):
            if n % i == 0:
                count = count + 1
        
        if count == 2:
            return "prime"
        else:
            return "not prime"
    else:
        return "not prime"

print(prime(10))
print(prime(7))
print(prime(1))




    
        
