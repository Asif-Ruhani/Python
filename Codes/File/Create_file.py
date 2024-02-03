from pathlib import Path

"""file1=Path('Asif.txt') # file is created
file1.write_text("This file is created") # Write on the file
print(file1.read_text()) # read from the file





file2=open("Ruhani.txt")
text=input("Write something on the file : ")
file2.write_text(text)
print(file2.read_text())"""





"""file3=open('fazlu.txt','w') # there was no file named fazlu, so it automatically create this file then open that
file3.write('Ami asifer abba\n')
file3.close()

file3=open('fazlu.txt','a') # a for append
file3.write('Ami achiar jamai')
file3.close()

file3=open('fazlu.txt')
x=file3.read()
print(x)
file3.close()"""






file4=open('Achia.txt') # There is a file named Achia.txt, so that file will open.
y=file4.read()
print(y)
file4.close()