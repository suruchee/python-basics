class Students:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print("Accepting data")
        self.name = input("Enter name")
        self.contact = input("Enter contact")

    def putdata(self):
        print("The name is" + self.name, "This is contact" + self.contact)

class ScienceStudent(Students):
    def __init__(self, age):
        self.age = age
    def science(self):
        print("I am science student")
John = ScienceStudent(20)
John.science()
John.getdata()
John.putdata()

#recursion
def factorial(x):
    if(x == 1):
        return 1
    else:
        return x*(factorial(x-1))
print(factorial(5))

#set
seta = {1,2,3,4,5,6}
setb = {4,5,6,7,8,9}
print(seta | setb)
print(seta & setb)
print(seta - setb)

#itertools

from itertools import count
for i in count(5):
    print(i)
    if i >= 20:
        break

from itertools import accumulate, takewhile
numbers = list(accumulate(range(9)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))

#operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.y
        y = self.y + self.y
        return Point(x,y)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

point1 = Point(1,4)
point2 = Point(2,8)
print(point1 + point2)


#datahiding
class Myclas:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

objecttone = Myclas()
objecttone.add(5)

