def decorator(func) :

    def wrapper():
        print("Starting")

        func()

        print("finished")
        
    return wrapper 

@decorator
def greet() :
    print ("Hello")



@decorator
def forgive ():
    print("sorry")


greet()

forgive ()