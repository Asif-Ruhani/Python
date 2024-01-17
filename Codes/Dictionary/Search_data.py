student_info = {
'CSE':{
        49: {
            3: {
                112: {'Name': 'Asif Ruhani, Father: Fazlul Hoque, Mother: Achia Hoque, District: Patuakhali'},
              
                119: {'Name': 'Aminul, Father: Himel, Mother: Islam, District: Noakhali'},
    
                95: {'Name': 'Saydur, Father: Rahman, Mother: Sohan, District: Patuakhali'}
               }
           } 
      },
'EEE': {
        49:{
            3: {
                127: {'Name': 'Nurul, Father: Azim, Mother: Rahat, District: Coxs Bazar'}
               }
        },
        34:{
            2:{
               130:{'Name': 'Khalid, Father: Saifullah, Mother: Kobi Nazrul, District: Rajbari'}
            }

        }
        
    }
}

dept = input("Enter Department: ")
intake = int(input("Enter Intake: "))
sec = int(input("Enter Section: "))
id_num = int(input("Enter ID: "))

# Use try-except to handle the case when the key is not found
try:
    student_data = student_info[dept][intake][sec][id_num]
    print(student_data)
except KeyError:
    print("Student not found.")
