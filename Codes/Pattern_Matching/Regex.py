import re # this import re for re.compile() function
check_string=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d') # this 11 \d absorb the eleven numeric numbers from the text. if you input 15 numeric numbers in the text, it will not show error, it will absorb only 11, because there are 11 \d. You can write \d as you want the formate. ex: (\d\d\d-\d\d\d-\d\d\d\d) american phn number, like this. it will show only first number. if you write more than one numbers in the text, it will show only the first one.

text=input('Enter text : ')
x=check_string.search(text) # we need to store the searched text into a variable
print('Phone number is '+x.group())

# we need three functions to find a number from a text using regex. re.compile(), search() and group() functions.

# Formate:
# x=re.compile()
# y=x.search()
# z=y.group()
# print(z) 