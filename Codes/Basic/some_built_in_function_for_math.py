
from math import *  # all below library functions are in this package, that's why it has to be written

print("Maximum number is : ", max(10, 45, 86, 78, 85, 86, 87, 82))     # max() function
print("minimum number is : ", min(10, 45, 86, 78, 85, 86, 87, 82))     # min() function
print("positive of (-45) is : ", abs(-45))     # abs() function
print("2 to the power 5  is : ", pow(2, 5))     # pow() function
print("Square root of 25 is ", sqrt(25))
print("Round value of 5.56  is ", round(5.56))
print("Round value of 5.46  is ", round(5.46))
print("floor value of 3.7 is ", floor(3.7))
print("ceilling value of 3.7 is ", ceil(3.7))

# sorted the values in ascending order
x=(45, 62, 2, 42, 23, 35,12, 25)
y=("h", "a", "d", "c", "k")
print("numerical sorted values ascending", sorted(x))
print("alphabetical sorted values ascending", sorted(y))

# sorted the values in descending order
x=(45, 62, 2, 42, 23, 35,12, 25)
y=("h", "a", "d", "c", "k")
print("numerical sorted values descending ", sorted(x, reverse=1))
print("alphabetical sorted values descending", sorted(y,reverse=1))

# if the value of reverse is 0 then the order will be ascending order
#is the value of reverse is 1 then the order will be descending order
