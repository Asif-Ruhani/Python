dictionary={}
dictionary1={}

"""print("Enter value ")
for i in range(112,115): # key will be set 112,113,114 automatically
    dictionary[i]=input()

for x in dictionary.items():
   print(x)"""


# Now key will be set as we wish (1st value and 2nd key)
"""print("Enter the values and keys sequentially ")
for i in range(0,3):
    
    dictionary1[input()]=input() # in this way first input is value & 2nd is key

for x in dictionary1.items():
    print(x)

print('These are keys')
for x in dictionary1.keys():
    print(x)
    
print('These are values')
for x in dictionary1.values():
    print(x)
"""

# Now key will be set as we wish (1st key and 2nd value)
print("Enter the values and keys sequentially ")
for i in range(0,3):
    x=input()
    dictionary1[x]=input() # in this way first input is key & 2nd is value

for x in dictionary1.items():
    print(x)

print('These are keys')
for x in dictionary1.keys():
    print(x)
    
print('These are values')
for x in dictionary1.values():
    print(x)
    

