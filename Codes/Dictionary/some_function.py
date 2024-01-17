
dictionary={
    'Asif':'is a good boy', # Asif is key,'is a good boy' is value
    'Fazlu':'is Asifs father',
    'Achia':'is asifs mother'
            }


print(" values() function")
for x in dictionary.values(): # values() function shows all values of dictionary
    print(x)
print(dictionary.values()) # We also print like this, but it will be different formate
print("") 


print("list() function")
for x in list(dictionary): # list() function shows all keys of dictionary
    print(x)
print(list(dictionary)) # We also print like this, but it will be different formate
print("") 


print("keys() function")
for x in dictionary.keys(): # values() function shows all keys of dictionary
    print(x)
print(dictionary.keys()) # We also print like this, but it will be different formate
print("") 


print("items() function")
for x in dictionary.items(): #values() function shows both keys & values of dictionary
    print(x)
print(dictionary.items()) # We also print like this, but it will be different formate
print("") 
print("")


x='Asif' in dictionary.keys() # It will check 'Asif' key is in dictionary or not
print(x) 
x='Arif' in dictionary.keys() # It will check 'Arif' key is in dictionary or not
print(x) 

x='is Asifs father' in dictionary.values() # It will check 'is Asifs father' value is in dictionary or not
print(x) 
x='Asifs' in dictionary.values() # It will check 'Asifs' value is in dictionary or not
print(x) 



dictionary1={'pen': 10, 'cup': 6, 'key': 3}
print("We have "+str(dictionary1.get('pen',0))+' pens') # 10 converted to string and printed
print("We have ",dictionary1.get('pen',0),' pens') # 10 printed as integer not string
#get(x,y) it requires two arguments(key,value). we will put 0 as a value. if the key and value are in the dictionary, that will be printed. here i putted 0 as a value, but there are 10 in the dictionary. so, 10 will be printed, not 0. if there was no key like pen, then the key pen will add in the dictionary and that's value will be 0.

print('we have ',dictionary1.get('mobile',0),' mobiles') # it will print "We have 8 mobiles". because there is no mobile key and 8 value. that's why value will be shown as 0.
