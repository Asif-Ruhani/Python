# we can put data into diction in two ways from user

# way 1 (using condition)

dictionary={
    'Asif':'is a good boy',
    'Fazlu':'is Asifs father',
    'Achia':'is asifs mother'
            }
for x in dictionary.items(): # each key and value will go into x and print
    print(x)
print('')
print('Started 1st way')
# Add new data
if 'Arif' not in dictionary:
    dictionary['Arif']='is Asifs brother'  # this data will be added in dictionary
# try to add new data but won't be added
if 'Fazlu' not in dictionary:
    dictionary['Fazlu']='is Asifs pops' # this data will not be added in the dictionary because the key Fazlu already in the dictionary.
# change the data
if 'Achia' in dictionary:
    dictionary['Achia']='is Asifs mummy' # this data will change the previous data where key was Achia and value was 'is Asifs Mother' now vlaue will be 'is Asifs mummy'. 

# Now check the dictionary data again
for x in dictionary.items(): 
    print(x)
    



# Way 2 (using setdefault() method)
print('')
print("Started 2nd ways ")
dictionary.setdefault('Abul','is Asifs grandfather') # this data will be added because this type of key is not in the dictionary.

dictionary.setdefault('Asif','is not a bad boy') # this data will not be added because the key already is in the dictionary and will not be changed the value. condition can change the data, as we did above, but method can not change.

for x in dictionary.items(): 
    print(x)
    
    

