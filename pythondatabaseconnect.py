import mysql.connector as db

conn = db.connect(host="localhost", user="root",password="Yogesh321", database="mydb")
mycursor = conn.cursor()


def insertStudent():
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    marks = float(input("Enter marks: "))
    qry = "insert into student values(%s,%s,%s,%s)"
    data = (id,name,phone,marks)
    mycursor.execute(qry,data)
    conn.commit()
    print("Student inserted")


def fetchStudents():
    qry = "select * from student"
    mycursor.execute(qry)
    data = mycursor.fetchall()
    if data:
        for item in data:
            print("Id =",item[0],"Name =",item[1],"Phone =",item[2],"Marks =",item[3])

    else:
        print("No Records found!!")


def fetchStudentbyid():
    id = int(input("Enter id: "))
    qry = "select * from student where id="+str(id)
    mycursor.execute(qry)
    data = mycursor.fetchone()
    if data:
        print("Id =",data[0],"Name =",data[1],"Phone =",data[2],"Marks =",data[3])

    else:
        print("No Records found!!")


def deleteStudentbyid():
    id = int(input("Enter id: "))      
    qry = "select * from student where id="+str(id)
    mycursor.execute(qry)
    data = mycursor.fetchone()
    if data:
        qry = "delete from student where id="+str(id)
        mycursor.execute(qry)
        print("Student deleted successfully")
        conn.commit()
    else:
        print("Student not found!!")
    

def exit():
    choice = input("Enter y to exit and n to continue..")
    if choice == "N" or choice == 'n':
        return False
    elif choice == "Y" or choice == 'y':
        return True
    else:
        print("Invalid input")
        print("")
        return exit()


while True:
    print("1. Register Student")
    print("2. Fetch all student")
    print("3. Fetch student by ID")
    print("4. Delete student by ID")
    print("5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        insertStudent()
        print("")

    elif choice == 2:
        fetchStudents()
        print("")

    elif choice == 3:
        fetchStudentbyid()
        print("")

    elif choice == 4:
        deleteStudentbyid()
        print("")
    
    elif choice == 5:
        data = exit()

        if data == True:
            print("Thank you....")
            print("")
            break
        else:
            print("")
            continue

    else:
        print("Invalid Choice !!")
        print("")