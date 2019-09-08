people = {"John":32,"Rob":34}
print(people["John"])


numbers = {
    1: "one",
    2: "two",
    3: "three"
}
print(3 in numbers)
print(numbers.get(2))
print(numbers.get(5), "Key not found")

#tuples
fruits = ("Apple","Mango","Peach")
fruits1 = "Apple","Mango","Peach"

print(fruits[0])
#slicing
numberss = [0,1,2,6,3,4,5,7]
print(numberss[2:6])
print(numberss[0:2])
print(numberss[:2])
print(numberss[3:])
print(numberss[0:7:3])


#list comprehension
list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)

#string formatting
numbers1 = [4,5,6]
newstring = "Numbers:{0},{1},{2}".format(numbers1[0],numbers1[1],numbers1[2])
newdate = "date:{0}/{1}/{2}".format(numbers1[0],numbers1[1],numbers1[2])

print(newstring)
print(newdate)
print("{x}/{y}".format(x=100,y=200))

#String function
print(":".join(["Apple","Banana","Mango"]))
print("Hello there".replace("there","world"))

newstringg = "Hello there"
print(newstringg.replace("there","world"))


stringg = "This is a string test"
print(stringg.startswith("Thisa"))
print(stringg.endswith("test"))
print(stringg.upper())

#numeric function
print(min(1,2,4,56,9))
print(max(1,2,4,56,9))
print(abs(-200))






