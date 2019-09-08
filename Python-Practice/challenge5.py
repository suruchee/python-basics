#Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("There is a divide by zero error")
        return 0


x = float(input('Enter a number'))
y = float(input('Enter value by which you want to divide the number'))
result = divide(x, y)
print(result)
