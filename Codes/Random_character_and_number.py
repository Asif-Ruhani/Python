import random
# random.randint() always return a integer value
password=""

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # size = 26 (0-25)

spcl_chctrs=['!','@','#','$','%','^','&','*'] #size = 8 (0-7)

for i in range(0,2):
    
    password+=letters[random.randint(0,25)] #it will create 2 random value from index 0 to 25 

    password+=str(random.randint(0,9)) #it will create 2 random value from 0 to 9 and return the integer value, but we need to convert it into string to concat.we don't concat integer values.letters and spcl_chctrs are already character type array, that's why we don't need to convert them into string.

    password+=spcl_chctrs[random.randint(0,7)] #it will create 2 random value from index 0 to 7

print(password)

