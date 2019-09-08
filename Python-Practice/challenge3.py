#Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.
#Task no 2: Create a function which displays out the square values of numbers from 1 to 9.

for x in range(5):
    print("I am a programmer")



def display_square():
    for x in range(1, 10):
        print(x**2)


display_square()




def add(a,b):
    return a+b
def square(c):
    return c*c
result = square(add(2,3))
print(result)
