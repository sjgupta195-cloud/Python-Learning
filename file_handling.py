file = open("hello.txt","w")
file.write("i love python")  
file.close()

with open("hello.txt","r") as file:
    content = file.read()

print (content)

# "a" stands for append in file similar to "w" stands for write and "r" for read