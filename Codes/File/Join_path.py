from pathlib import Path
main_folder=r'program\path' # run with 'r' without 'r', and see the difference
sub_folder=r'python' # r is one kind of optional
sub_sub_folder='asifvai'

join_path=main_folder+sub_folder+sub_sub_folder
print(join_path)

join_path=main_folder+'\\'+sub_folder+'\\'+sub_sub_folder #'\\' is for backslash 
print(join_path)

join_path='\\'.join([main_folder,sub_folder,sub_sub_folder]) # join file name using join() method
print(join_path)

 # Run the code and watch the difference
print('\n\n')
# we can join in another way 
file_name=Path('Asif vai\Ruhani') # we can use 'r' or not.
sub_file_name=Path('ami nai')
print(file_name / sub_file_name)