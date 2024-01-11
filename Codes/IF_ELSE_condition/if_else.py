
# Normal if else

"""
mark=int(input("Enter the mark"))
if mark<33:
     print("You have failed")
else:
    print("You have passed")

"""


# if elif and else
"""
mark=int(input("Enter the mark"))
if mark<33:
    print("You have failed")
elif mark<60:
    print("You are average")
elif mark<70:
    print("You are above average")
else:
    print("you are good")
"""



# Scope of if, else
"""
x=int(input("Enter the value of x"))
if x<10:
    print("a")
    print("b")
    print("c")
else:
    print("x")
    print("y")
    print("z")
"""


# and , or use in condition

mark=int(input("Enter the mark"))
if mark<33:
    print("You have failed")
elif mark>33 and mark<=60:
    print("You are average")
elif mark>60 and mark<80:
    print("You are above average")
else:
    print("You are good")

