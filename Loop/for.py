

"""
n=[1, 8, 6, 3, 7, 4, 9]
for i in n:     # Every value of n will be stored in i variable one by one
    print(i)
print("Loop is finished")
"""




n=int(input("Enter N : "))
for i in range(0, n, 2):     # For even number
    print(i)
print("Loop is finished")




"""
n=int(input("Enter N : "))
sum = 0
for i in range(1, n, 1):
    sum=sum+i
print("Sum of N number is = ",sum)
print("Loop is finished")

"""



"""
n=int(input("Enter N : "))
sum = 0
for i in range(1, n, 2):
    sum=sum+i
print("Sum of N number is = ",sum)
print("Loop is finished")
"""




"""
range(1,n+1,1) means, loop will be start from 1 to (n+1) and
increment by 1

range(0,n,2) means, loop will be start from 0 to n and
increment by 2
"""
