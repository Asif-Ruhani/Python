from pathlib import Path
file_name=['file1.txt','file2.docx','file3.pdf'] # this is my file names

for i in file_name:
    file_path=Path(r'program & software\python\File',i) # file path is set as my wish
    print(file_path)