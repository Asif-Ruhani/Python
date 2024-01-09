
"""
n=int(input("Enter N : "))
for i in range(0, n, 2):     # For even number
    print(i)
    if i==20:
        break
print("Loop is finished")
"""





"""
n=int(input("Enter N : "))
for i in range(0, n, 1):     # For even number
    if i==20:
        continue   # it means, when i=20, the code jump to loop line not print/next line. So the loop will print 0 to n number just not 20
    print(i)
print("Loop is finished")
"""






"""n=int(input("Enter N : "))
for i in range(0, n, 1):     # For even number
    if i>=20:
        continue   # it means, when i>=20, the code jump to loop line not print/next line. So the loop will print 0 to 19 / smaller value of 20
    print(i)
print("Loop is finished")
"""





n=int(input("Enter N : "))
for i in range(0, n, 1):     # For even number
    if i<=20:
        continue   # it means, when i<=20, the code jump to loop line not print/next line. So the loop will print 21 to n / larger value from 20
    print(i)
print("Loop is finished")
