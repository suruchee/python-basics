def add_ten(x):
    return x+10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 10))
 #lambdas
result = (lambda x: x**2)(30)
print(result)
print((lambda x: x**2)(30))



#map
def add(x):
    return  x+2
newresult = [10,20,30,40,50]
result1 = list(map(add,newresult))
print(result1)

#map and lambdas
newresult = [10,20,30,40,50]
result1 = list(map(lambda x: x+3,newresult))
print(result1)

#filters
newlist = [1,2,3,4,5,6,7,8,9]
result2 = list(filter(lambda x: x % 2 == 0, newlist))
print(result2)

#generaator
def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(even_numbers(21)))


