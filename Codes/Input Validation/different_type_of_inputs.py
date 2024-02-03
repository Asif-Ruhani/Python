# we have to import PyInputPlus for these type of input and we have install it separately, because it is not from standard python library.
# To install it, go to cmd and write "pip install --version pyinputplus" and then search on google and download that. that's it.


import pyinputplus as py 

# for getting only numeric values
age=py.inputNum("Enter age : ") # keep asking until numeric value is entered
print("Your age is = ",age)


# we can set a instruction for input
age=py.inputNum("Enter age : ",min=6)
print("Your age is = ",age)


# we can set multiple instructions for input
num=py.inputInt("Enter a number : ",min=4,max=7)
print("Number is = ",num)



# we can set No. of input using limit
num=py.inputInt("Enter a number : ",limit=3,default='Timeout') # we can input wrong value 3 time, not more than that. when we use limit, we have to use default.
print(num)




# for getting any type of characters in keyboard
string=py.inputStr("Enter your name : ") # this get any type of character on keyboard and prompt="something" is for display something
print("Your string is = "+string)


# for getting email
email=py.inputEmail("Enter your email : ")
print("your email is = "+email)


#for menu or choice (Choice & Menu)
print("What is your name : ")
menu=py.inputMenu(['Asif','Arif','Fazlu','Achia'])
print("You have choosen = "+menu)

print("What is your name : ")
menu=py.inputChoice(['Asif','Arif','Fazlu','Achia'])
print("You have choosen = "+menu)


# for getting yes/no ans
x=py.inputYesNo("Enter yes or no for answer : ")
print(x)

# for getting date time
date_time=py.inputDatetime("Enter date and time : ")# ex: 1/25/2024 9:45 or 2024/1/25 9:45, but not the time first, always date will first enter.
print(date_time)