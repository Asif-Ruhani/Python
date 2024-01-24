"""\d is only for numeric 0-9
\D is for all character without 0-9
\w is for letter,numeric and underscore
\W all without letter,numeric and underscore
\s is for space,tab, newline
\S all without space,tab,newline"""

import re
match_string1=re.compile(r'\d+\s\w+') # this can match firstly(starts from) combination or numeric(d+), secondly one space/tab/newline(s) and thirdly combination of letter/numeric/underscore
text1=match_string1.findall(" we have 10 apples, 20 orange and 3 umbrella. ")
print("Matching text is = ",text1)


match_string2=re.compile(r'\d+\s') # this can match firstly (starts from) combination or numeric(d+), secondly space/tab/newline(s)
text2=match_string2.findall(" we have 10 apples, 20 orange and 3 umbrella. ")
print("Matching text is = ",text2)


match_string3=re.compile(r'\D+\s') # this can match firstly (starts from) combination of characters(D+), secondly space/tab/newline(s) not any numeric value
text3=match_string3.findall(" we have 10 apples, 20 orange and 3 umbrella. ")
print("Matching text is = ",text3)


match_string4=re.compile(r'\D+\d+') # this can match firstly (starts from) combination of characters(D+), secondly space/tab/newline(s)
text4=match_string4.findall(" we have 10 apples, 20 orange and 3 umbrella. ")
print("Matching text is = ",text4)