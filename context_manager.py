''' when in file handling we used with open style i.e.
    context manager and it ensures that file resources are cleaned up after using it '''


with open("hello.txt","r") as file :
    content = file.read()

print(content)