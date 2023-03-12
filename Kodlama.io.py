print("*-*  'Welcome To My Student Lists'  *-*")

listStudents = ["Ahmet Korkut", "Mehmet Galip", "Tekin Korkmaz"]
print(listStudents)

print("Please enter name and surname for add to the list")
def addStudent():
    addStudentName = input("Please enter name and surname for add in the list : ")
    listStudents.append(addStudentName)

addStudent()
print("Student added to the list!")
print(listStudents)

def addMoreStudents():
    list = []
    while True:
        addMore = input("Please enter full name for add more students  : ")
        list.append(addMore)
        x = input("If you want to add more student just write yes or no")
        if x == "no":
            break
        listStudents.extend(list)

addMoreStudents()
print("Student added to the list!")
print(listStudents)

def deletedStudent():
    deletedStudent = input("Please enter the full name of the student you want deleted! :  ")
    listStudents.remove(deletedStudent)
    

deletedStudent()
print("Student deleted from list!")

listStudents.append("Furkan Karakus")
print("Student added to the list!")

print(listStudents)

listStudents.remove("Ahmet Korkut")
print("Student deleted from list!")

print(listStudents)

for i in range(len(listStudents)):
    print(listStudents[i])
  
findStudentNumber = input("If you want to learn student number then please enter student's full name : ")
for i in range(len(listStudents)):
    if listStudents[i] == findStudentNumber:
        print(f"Student number is {i}") 
        else:
          break
        
print(listStudents)
