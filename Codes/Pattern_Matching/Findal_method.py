import re


# we will use search() and findal() both method to compare their working process

#firstly used search()
match_string=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d') # matching the phn number from the text
search_text1=match_string.search('My phone number is 01783717408 and 01638651664,call me anytime please.')
print("first matching searched text is = "+search_text1.group()) # if we do not use group(), the will be right but different way.





# Now we will use findal()
search_text2=match_string.findall('My phone number is 01783717408 and 01638651664, call me anytime please.')
print("all matching searched text is = ",search_text2) # we can not use group() during findall().
