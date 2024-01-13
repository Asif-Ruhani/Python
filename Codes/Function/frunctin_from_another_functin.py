def function1(x):
    print("This function is first function")
    print("Given name is : "+x)

def function3(z):
    function1(z)
    function2(z)
    print("This function is third function")
    print("Given name is : "+z)

def function2(y):
    print("This function is second function")
    print("Given name is : "+y)



name=input("Enter your name : ")
function3(name)