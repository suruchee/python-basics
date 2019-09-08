file = open("demo.txt",'r')
file = open("demo.txt",'w')

content = file.read()
content = file.read(10)
content = file.readline()

print(content)
file.close()


file = open("demo.txt",'w')
file.write("Hello I am from file handling write operation")
file.close()




file = open("demo.txt",'w')
file.write("Hello I am from file handling write operation")
file.close()

file = open("demo.txt",'r')
content = file.readline()
print(content)
file.close()



file = open("demo.txt",'w')
file.write("Hello I am from file handling write operation")
file.close()

file = open("demo.txt",'r')
content = file.readline()
print(content)
file.close()

file = open("demo.txt",'a')
file.write("Hello I am from file handling append operation")
file.close()

