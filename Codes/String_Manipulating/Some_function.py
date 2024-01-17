string="Asif Ruhani !"

print(string.upper())

print(string.lower())

string1="ASIF RUHANI !"

print(string1.isupper())

print(string1.islower())

string2="aisf ruhani !"

print(string2.isupper())

print(string2.islower())

print('')
print('')

string3="AsifRuhani"
string4="Asif Ruhani"
print(string3.isalpha()) #this will be true only when all are letters,not space or anything
print(string4.isalpha()) 
print('')
print('')
string5="Asif2743"
string6="Asif2743 !"
print(string5.isalnum()) # This will be true only when all letters and numbers. not space and any other thing 
print(string6.isalnum())


"""
Similarly
  string.isdecimal() only for numeric values
  string.isspace() only for space,tab and newline
  string.istitle() only a title, First letter of each word will be capital and others are small. EX: Asif Ruhani Is A Boro Vai
  """
