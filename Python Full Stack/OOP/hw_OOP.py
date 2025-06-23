'''
1. Create a base class Shape with a method area().implement subclass Cricle,
 Rectangle, and Triangle that each calculate the area in their own way. 
 Write a function taht takes a list of shapes and prints the area for each.
'''
class Shape():
    def area(self): 
       pass
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area_circle(self):
        pie = 3.14
        print("Area of circle: ",pie * self.r  * self.r )

class Rectangle(Shape):
     def __init__(self, a, b):
         self.a = a
         self.b = b
     def area_rectangle(self):
         print("Area of rectangle:", self.a * self.b)

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area_triangle(self):
        hal = 0.5
        print("Area of triangle:", self.b * self.h * hal)

c = Circle(2)
r = Rectangle(2,2)
t = Triangle(2,4)

c.area_circle()
r.area_rectangle()
t.area_triangle()
print()

'''
2. Write a python program to create a class representing a shopping cart.
   Include methods for adding and removing items, and claculating the total
   price.
   Solution: Create a class with functions add_item, remve_item and
   calculate_total.
'''


dict = {}

class Shopping:
    #def __init__(self,k,v):
     #   self.key = k
      #  self.value = v
        
    def add_items(self,k,v):
        dict.update({k : v})
        print("Item added:",dict)

    def remove_items(self,k):
        remove = dict.pop(k)
        print("Item removed:", remove)

    
    def cal_total(self):
        total = dict.values()
        print(total)
        add = 0
        for i in dict.values():
            add += i
        print("total value: ", add)

s1 = Shopping()
s1.add_items('ice', 20)
s1.add_items('Wheat', 30)
s1.add_items('rice', 40)
print()
s1.remove_items('ice')
print()
s1.cal_total()
print()

'''
3.Define a vehical class with attributes like make, model, and year, and create
  a child class called Car that inherits from Vehical: Add a method in Car calss
  that prints Car_details and a method to calculate the car's age.
'''

class Vehical:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehical):
    #def __init__(self, make, model,year):
     #   Vehical.__init__(self, make, model,year)
        
    def car_details(self):
        return f"Car Info: \n Make: {self.make} \n Model: {self.model} \n Year: {self.year}"

    def car_age(self):
        age = 2024 - self.year
        return f"The age of the Car is {age}"

c = Car("Toyota", "Camry", 2015)

print(c.car_details())
print(c.car_age())















































