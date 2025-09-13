#File Handling:
#A school wants to maintain student records using a text file.
#You are required to write a Python program that performs the following file handling operations step by step:
#1) Write Operation:
#- Create a file named students.txt.
#- Write details of students (Name, Roll Number, Marks) into the file.
#2) Read Operation:
#- Read the content of students.txt and display it on the screen.
#3) Rename Operation:
#- Rename the file from students.txt to student_records.txt.
#4) Directory Operations:
#- Create a directory called SchoolData.
#- Move the renamed file student_records.txt into this directory.
#- List all files present in SchoolData to confirm the file is inside.
#5) Delete Operation:
#- Delete the file student_records.txt from inside the directory.
#Finally, delete the SchoolData directory.    
#Do create a menu taking the user input and then perform the operation

import os


school_info = None

students = [{
    "name": "Raj",
    "Roll": 11,
    "Marks": 67
},
{
    "name": "Lily",
    "Roll": 22,
    "Marks": 98
},
{
    "name": "Muk",
    "Roll": 33,
    "Marks": 74
}
]

try:
    school_info = open('./Assignments/Day8/students.txt', 'w')
    for st in students:
        school_info.write(f"{st['name']} {st['Roll']} {st['Marks']}\n")
    print("Students file created")
    school_info.close()
    
    school_info = open('./Assignments/Day8/students.txt', 'r')
    while True:
        student = school_info.readline().split()
        if not student:
            break
        print(f"Name: {student[0]} Roll: {student[1]} Marks: {student[2]}")
    school_info.close()
    
    os.rename('./Assignments/Day8/students.txt', './Assignments//Day8/student_details.txt')
    print("File renamed")

    os.mkdir('./Assignment/Day8/School')
    print ("Directory Created")

    os.replace('./Assignment/Day8/student_details.txt', './Assignment/Day8/School/student_records.txt')
    
    listoffiles = os.listdir('./Assignment/Day8/School')
    print (listoffiles)

    path = './Assignment/School/'
    for file in listoffiles:
        os.remove(path + file)
    print("File deleted")

    os.rmdir(path)
    print("Removed directory ")
    
except Exception as e:
    print(f"Exception occured {e}")
 