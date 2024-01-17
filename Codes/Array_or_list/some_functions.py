
n=[ "F", "B", "A", "R", "F", "E" ]
print(len(n))   # size/length of the array

n.append("I H G")  # add data to array
print(n)

n.insert(3,"K")  # add K in index 3 but R will not delete, for that data will be shifted to right 1 index
print(n)

n.remove("E")  # E will be removed
print(n)

n.sort()  # sort in ascending order
print(n)

n.reverse()  # sort in descending order
print(n)

n.pop()  # last value will me popped 
print(n)

m=n.copy()  # All data of n array will be copied into m array
print(m)

n.clear()  # all data will be cleared, array will be empty
print(n)

x=m.index("F")  # it will find the index of F data
print(x)

y=m.count("F")  # It will count how many F in the data
print(y)

z=list(range(10))  # range() function generate (0-9) total 10 values and list() function is an array. We put that 10 values into an array using list() function
print(z)

w=list(range(4, 14))  # range() function generate (4-13) total 10 values
print(w)

v=list(range(8, 22, 2))  # range() function generate 8 to till 22 and interval will be 2
print(v)

