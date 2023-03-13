print("*-*  'Welcome To My Student Lists'  *-*")

listStudents = ["Ahmet Korkut", "Mehmet Galip", "Tekin Korkmaz", "Talha Koc", "Mert Gunok"]
print(listStudents)


def addStudent():
    print("\n***  'Add More Student Single Time' ***\n")
    addStudentName = input("Please enter name and surname for add in the list : ")
    listStudents.append(addStudentName)

addStudent()
print("Student added to the list!")
print(listStudents)


def addMoreStudents():
    print("\n***  'Add More Students Multiple Time' ***\n")
    multipleAdd = int(input("Please enter how many students you want to add as numbers "))
    for i in range(multipleAdd):
        addStudent()

addMoreStudents()
print("Student added to the list!")
print(listStudents)

def deletedStudent():
      print("\n***  'Delete Students You Want To ' ***\n")
      deletedStudents = input("Please enter the full name of the student you want deleted! :  ")
      listStudents.remove(deletedStudents)
    

deletedStudent()
print("Student deleted from list!")

def removeStudent():
    print("\n***  'Remove Students Multiple Time' ***\n")
    print("If you want to break this condition then just write 'B' ")
    while True:
        fullName = input("Please enter the student's full name : ").title().strip()
        if fullName == "B" or fullName == "b":
            break
        if fullName not in listStudents:
            print("Student not found!!! Please try again!")
            continue
        listStudents.remove(fullName)
        print("Student deleted from list!")
        if len(listStudents) == 0:
            print("All students have been successfully deleted")
            break

removeStudent()

listStudents.append("Furkan Karakus")
print("Student added to the list!")

print(listStudents)

listStudents.remove("Ahmet Korkut")
print("Student deleted from list!")

print(listStudents)

print("\n***  'Whole Students ' ***\n")
for i in range(len(listStudents)):
    print(listStudents[i])
  

print("\n***  'Student Number Finder ' ***\n")
findStudentNumber = input("If you want to learn student number then please enter student's full name : ")
for i in range(len(listStudents)):
    if listStudents[i] == findStudentNumber:
        print(f"Student number is {i}") 
        else:
            print("Student not found")
          break
        
print("\n***   'Latest Status of The List'   ***\n")
print(listStudents)
