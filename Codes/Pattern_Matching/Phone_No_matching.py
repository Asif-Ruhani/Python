# Matching this number: 411-532-9635
def pattern_matching(text):
    if not len(text)==12:#"if len(text)!=12" and "if not len(text)==12" same statement
        return 0

    for i in range(0,3):
        if not text[i].isdecimal():  #"if text[i]!=(0-9)" and "if not text[i].  isdecimal()" same statement
           return 0
   
    if not text[3]=='-':
         return 0
    
    for i in range(4,7):
        if not text[i].isdecimal():
            return 0
        
        if not text[7]=='-':
            return 0
        
    for i in range(8,12):
        if not text[i].isdecimal():
            return 0
         
    

text=input('Enter input : ')
x=pattern_matching(text)
if not x==0:
    print('This is a phone number.')
else:
    print('This is not a phone number.')