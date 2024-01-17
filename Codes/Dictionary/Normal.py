
dictionary1={1:'Asif',2:'Ruhani'}
#here 1 and 2 are keys and Asif & Ruhani are values
print(dictionary1)
print(dictionary1[1]+" " + dictionary1[2])

# key could be any data type. such as integer,double,character,string
dictionary2={
    'Asif':'is a good boy', # Asif is key,'is a good boy' is value
    'Fazlu':'is Asifs father',
    'Achia':'is asifs mother'
            }
print(dictionary2['Fazlu']) # by this print we can easily understand the difference between array/list and dictionay

# let's findout the difference more
dictionary3={112:'Name: Asif Ruhani '
             'Department: CSE '
             'Intake: 49 '
             'Section: 03',

             119:'Name: Aminul Islam '
             'Department: CSE '
             'Intake: 49 '
             'Section: 05',

             95:'Name: Saydur Rahman '
             'Department: CSE '
             'Intake: 50 '
             'Section: 07',

             127:'Name: Nurul Azim '
             'Department: CSE '
             'Intake: 49 '
             'Section: 03',

             100:'Name: Khalid Saifullah '
             'Department: Bangla '
             'Intake: 34 '
             'Section: 03'

            }

id=int(input("Enter the id to know information : "))
print(dictionary3[id])
# We can easily know the information of a student using his id or any other key value.
print(list(dictionary3)) # We can print the all keys of dictionary3 using list(dictionary name)
print(dictionary3.values()) # We can print the all values of dictionary3 using dictionary name.values()
