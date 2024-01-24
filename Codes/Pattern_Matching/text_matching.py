import re
check_text1=re.compile(r'Asif|Ruhani|Fazlul|Hoque|Achia|Arif')# display one of them, that will be first matched. or operation is used

main_text1=input("Enter the main text : ")
search_text1=check_text1.search(main_text1)#search() will return the first matching pattern, not 2nd, 3rd.
grp1=search_text1.group()
print("Searching text is = "+grp1)




check_text2=re.compile(r'Asif and Arif') # 'Asif and Arif' has to be in the main string, then it will match, otherwise not. suppose, you wrote 'Asif and ami' it will not match. and operation is used

main_text2=input("Enter the main text : ")
search_text2=check_text2.search(main_text2)
grp2=search_text2.group()
print("Searching text is = "+grp2)
