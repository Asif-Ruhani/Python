import pyinputplus as py
# we will use allowRegexes and blockRegexes keyword

# for getting roman symbols
"""roman_symbol=py.inputNum("Enter roman symbol : ",allowRegexes=[r'(I|V|X|L|C|D|M|i|v|x|l|c|d|m)+',r'zero']) # We can use both inputStr() and inputNum()
print("You have entered = "+roman_symbol)
"""
# fixed some characters to make word
word=py.inputNum("Write a word : ",blockRegexes=[r'[12345]+'])
print(word," is matched with characters.")

