import re
# vowel matching
"""match_text1=re.compile(r'[aeiouAEIOU]')
text1=match_text1.findall("Asif Ruhani would be a very good engineer inshallah.")
print("Vowels are = ",text1)

print("\n")
#consonant matching
match_text2=re.compile(r'[^aeiouAEIOU]')
text2=match_text2.findall("Asif Ruhani would be a very good engineer inshallah.")
print("Consonats are = ",text2)"""
 
 
 
 # any user input matching
match_text3=re.compile(r'i|am|asif|ruhani|from|section|3')
search_text=input("Enter searching word : ")
text3=match_text3.search(search_text)
length=len(text3.group())
if length!=0:
    print("Yes, the word is in the text ")
    print("matching word is = ",text3.group())
