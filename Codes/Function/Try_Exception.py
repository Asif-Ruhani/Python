def function(x):
    return 100/x

try:
    print(function(2))
    print(function(50))
    print(function(10))
    print(function(0)) 
    print(function(-5))
    print(function(230))

except ZeroDivisionError: # if 100 divide by 0, try will stop and this line will execute. and (100/-5) and (100/230) will not execute. (line 9,10)
    print("Undefined")
