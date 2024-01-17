text=input('Enter a text with phn number : ')
counter=0
length=len(text)
for i in range(0,length):
    sub_text=text[i:i+11] # when i=0,text[0:11]. When i=1, text[1:12]. When i=2,text[2:13]. every step in loop 11 characters copy into sub_text variable.

    #print('My name is = '+sub_text) # this print is only for check that how does it work

    if sub_text.isdecimal(): #check that variable(11 characters), that all are numerical or not.
        print('Given phone number is = '+sub_text)
        counter=1

if counter==0:
    print('There is no phone number in the text.')

    
