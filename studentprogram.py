n = int(input('Enter the number of the student:')) #2
Student = {}
    
for i in range(n): # i in range(2)
    name = input('Enter the name of the student: ')
    student_rollno  = input("Enter student roll no: ")
    section  = (input("Enter student section : "))
    address = input('Enter the student  address: ')
    Student[name] = [student_rollno,section,address]

while True:
    name = input('Enter student name: ')
    info = Student.get(name, -1)
    if info == -1:
        print('Student  does not exist')
    else:
        print(f'student details are: \n student roll: {info[0]}\n section: {info[1]}\n Address: {info[2]}')
    
    exit_choice = input('Do you want to exit [Yes|No]: ')
    if exit_choice == 'Yes' or exit_choice == 'yes':
       break 