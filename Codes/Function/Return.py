# First function
def function1(x): # any type of value will be returned
    x=x*x
    return x

# Second function
def function2(x,y):
    return x*y


# These are for first function
num1=int(input("Enter any number for function 1 : ")) # convert the input into integer using int() function

f1=function1(num1)
print("Square of the number is : ",f1) # integer number print. use (,) not (+),,, (+) for string or character

print("Square of the number is : ",function1(num1)) # we can write like this also




#These are for second funtion
num2=int(input("Enter fisrt number for function 2 : "))
num3=int(input("Enter second number for function 2 : "))
f2=function2(num2,num3)
print("Multiplication of two numbers is : ",f2)