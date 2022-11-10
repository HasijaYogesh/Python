# *******STAR PATTERN******
# *****
# *****
# *****
# *****
# *****

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print("")


# ******STAR PATTERN*******
# *****
# *   *
# *   *
# *   *
# *****

# for i in range (1,6):
#     if i==1 or i==5:
#         for j in range(1,6):
#             print("*",end="")
#         print("")
#     else:
#         for j in range(1,6):
#             if j==1 or j==5:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print("")

# ******STAR PATTERN********
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")


# *******STAR PATTERN********
#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")


# ********STAR PATTERN*********
# *****
# ****
# ***
# **
# *
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end="")
#     print("")


# ******STAR PATTERN*******
# *****
#  ****
#   ***
#    **
#     *
# for i in range(1,6):
#     for k in range(1,i):
#         print(" ",end="")
#     for j in range(6,i,-1):
#         print("*",end="")
#     print("")


# ********STAR PATTERN********
# *
# **
# * *
# *  *
# *   *
# ******
# for i in range(1,7):
#     if i==1 or i==6:
#         for j in range(1,i+1):
#             print("*",end="")
#     else:
#         for j in range(1,i+1):
#             if j==1 or j==i:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print("")


# *********STAR PATTERN**********
#     *
#    ***
#   *****
#  *******
# *********
# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):    
#             print("*",end="")
#     for l in range(0,i-1):
#         print("*",end="")
#     print("")


# ********STAR PATTERN******** ****INCOMPLETE PATTERN********
#     *
#    * * l=0,i=2
#   *   * l=1,i=3
#  *     *l=2,i=4
# *********
# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if j==1 or i==5:   
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for l in range(0,i-1):
#         if l==int(i/2):
#             print("*",end="")
#         else:
#             print(" ",end="")
            
#     print("")



# ********STAR PATTERN********
# *********
#  *******
#   *****
#    ***
#     *
# for i in range(0,5):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(2*(5-i)-1):
#         print("*",end="")        
#     print("")


# ********STAR PATTERN*******
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
# n=5
# n=int(input("Enter number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print("")
# for i in range(0,n-1):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for j in range(0,2*(n-i)-3):
#         print("*",end="")
#     print("")


# ********STAR PATTERN******
#    *
#   * *
#  *   *
# *     *
#*       *
# *     *
#  *   *
#   * *
#    *

# n=5
# for i in range(0,n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         if j==0 or j==2*i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

# for i in range(0,n-1):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for j in range(2*(n-i-1)-1):
#         if j==0 or j==2*(n-i-1)-2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")


# ********STAR PATTERN**********
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(2*(n-i)-1):
#         print("*",end="")
#     print("")

# for i in range(n-1):
#     for j in range(n-i-2):
#         print(" ",end="")
#     for k in range((n//2)+(2*i)+1):
#         print("*",end="")
#     print("")


# **********STAR PATTERN**********
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print("")

# for i in range(n-1):
#     for j in range(n-i-1):
#         print("*",end="")
#     print("")

# *****STAR PATTERN*******
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print("")

# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print("*",end="")
#     print("")

# ***********CREATING OUR FIRST CLASS, OOPS CONCEPT**********
# class Employee:
#     no_of_leaves=8
#     pass

# harry=Employee()
# rohan=Employee()

# harry.salary=450
# harry.role="Developer"

# rohan.salary=500
# rohan.role="Programmer"

# harry.name="Harry"
# rohan.name="Rohan"

# print(Employee.no_of_leaves)
# rohan.no_of_leaves=10
# print(rohan.__dict__)
# print(Employee.no_of_leaves)

# *************REMOVE SPACE FROM A STRING**************
# str="Hello World"
# str1=""
# for c in str:
#     if ord(c)!=32:
#         str1=str1+c

# print(str1)

# *************REMOVE 0 FROM ANY INTEGER NUMBER*********
# num=50250890603
# str1=str(num)
# str2=""
# for i in str1:
#     if i!='0':
#         str2=str2+i
# num=int(str2)
# print(num)

# **********USING TRY AND EXCEPT********
# print("Hello World")
# try:
#     x=int(input("Enter 1st number: "))
#     y=int(input("Enter 2nd number: "))
#     z=x/y
#     print("Result is",z)

# except ValueError:
#     print("Please enter numbers!!")
# except ZeroDivisionError:
#     print("Any number divisible by 0 is infinite, hence cannot be divide by 0!!")

# print("Bye..")

# **********REVERSE THE STRING WITHOUT USING INBUILT FUNCTION**************
# str="shivani is a programmer"
# print("The orginal string is ",str)
# revstr=""
# count=len(str)
# for i in str:
#     if count>0:
#         revstr=revstr+str[count-1]
#         count=count-1
# print("The reverse string is",revstr)

# ***********CONSTRUCTOR IN CLASS**************
# class Employee:
#     no_of_leaves=8
#     def __init__(self, aname, asalary, arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole

#     def printdetails(self):
#         return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"

# harry=Employee("Harry",5500,"Developer")
# yogesh=Employee("Yogesh",1500,"Manager")

# print(harry.printdetails())
# print(yogesh.printdetails())

# *********DECORATORS EXAMPLE**********
# def dec1(func1):
#     def nowexec():
#         print("Executing the function")
#         func1()
#         print("Fucntion Executed")
#     return nowexec

# @dec1
# def who_is_yogesh():
#     print("Yogesh is a good boy..")

# who_is_yogesh()

# **********EXAMPLE OF CLASS METHOD********
# class Employee:
#     no_of_leaves=8
#     def __init__(self, aname, asalary, arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole

#     def printdetails(self):
#         return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves

# harry=Employee("Harry",5500,"Developer")
# yogesh=Employee("Yogesh",1500,"Manager")
# harry.change_leaves(20)
# print(Employee.no_of_leaves)
# print(yogesh.no_of_leaves)

# ***********CLASS FOR ADDING 2 NUMBER***********
# class Sum:
#     def add(self,x,y):
#         print("The sum is",x+y)
    
# comp1=Sum()
# comp2=Sum()
# comp1.add(5,6)
# Sum.add(comp2,10,20)

# ***************CREATING CLASS AND INIT METHOD****************
# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram

#     def printdata(self):
#         print(f"The config is {self.cpu} & {self.ram}")

# comp1=Computer("intel", 8)
# comp2=Computer("Ryzen", 12)
# comp1.printdata()
# comp2.printdata()

# **********PRINT DICT OF CLASS************
# class Student:
#     def __init__(self,sid,sname,sclass):
#         self.sid=sid
#         self.sname=sname
#         self.sclass=sclass

# s1=Student(101,"Yogesh","10th")
# print(s1.__dict__)

# **********READING A FILE AND WRITING A DATA OF FILE 1 IN FILE 2********
# f=open("file.txt","r")
# data=f.read()
# f1=open("file1.txt","w")
# f1.write(data)
# f.close()
# f1.close()

# **********USING TRY, EXCEPT, RAISE AND FINALLY FOR THE ERROR HANDLING, WITHDARWING AMOUNT FROM THE ATM*************
# def checkbalance(withdrawamt,balance):
#     if withdrawamt<0:
#         raise ValueError("The amount can not be negative!!")
#     elif withdrawamt>balance:
#         raise Exception("Insufficent Balance in your account!!")
#     else:
#         print("Withdrawing the amount, please wait for the cash....")

# balance=100000
# print("Welcome to the ATM..")
# try:
#     withdrawamt=int(input("Enter the withdraw amount: "))
#     checkbalance(withdrawamt,balance)
# except ValueError as verr:
#     print(verr)
# except Exception as err:
#     print(err)
# finally:
#     print("Thank you for using our ATM..")

# ***********SINGLE INHERITENCE**********
# class A:
#     def feature1(self):
#         print("This is feature 1")
#     def feature2(self):
#         print("This is feature 2")

# class B(A):
#     def feature3(self):
#         print("This is feature 3")
#     def feature4(self):
#         print("This is feature 4")

# b1=B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# ***********MULTILEVEL INHERITENCE*************
# class A:
#     def feature1(self):
#         print("This is feature 1")
#     def feature2(self):
#         print("This is feature 2")

# class B(A):
#     def feature3(self):
#         print("This is feature 3")
#     def feature4(self):
#         print("This is feature 4")

# class C(B):
#     def feature5(self):
#         print("This is feature 5")

# c1=C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

# ***********MULTIPLE INHERITENCE*************
# class A:
#     def feature1(self):
#         print("This is feature 1")
#     def feature2(self):
#         print("This is feature 2")

# class B():
#     def feature3(self):
#         print("This is feature 3")
#     def feature4(self):
#         print("This is feature 4")

# class C(A,B):
#     def feature5(self):
#         print("This is feature 5")

# c1=C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

# ***********NEGATIVE ERROR HANDLING WITH THE RECURSIVE FUNCTION*************
# def addition(num):
#     if num>0:
#         return num+addition(num-1)
#     elif num==0:
#         return 0
#     else:
#         raise Exception("Negative value!!")

# try:
#     num=int(input("Enter number: "))
#     result=addition(num)
#     print("Result is:",result)
# except Exception as err:
#     print(err)
# finally:
#     print("Bye..")


# ***************STUDENT MANAGEMENT SYSTEM BY CLASS AND OBJECT***********
# class Student:

#     def __init__(self,id,name,marks,phone):
#         self.id=id
#         self.name=name
#         self.marks=marks
#         self.phone=phone

#     def showDetails(self):
#         print(self.id,self.name,self.marks,self.phone)


# Students=[]

# print("\n******Welcome to the Student Management System******")
# print("")

# while True:
#     print("1. Register Student..")
#     print("2. Fetch all Student..")
#     print("3. Fetch student by id..")
#     print("4. Remove student by id..")
#     print("5. Exit..")
#     print("")
#     choice=int(input("Enter choice: "))

#     if choice==1:
#         id=int(input("Enter id: "))
#         name=input("Enter name: ")
#         marks=float(input("Enter marks: "))
#         phone=input("Enter phone no.: ")
#         s=Student(id,name,marks,phone)
#         Students.append(s)
#         print("Student registered successfully...")
#         print("")

#     elif choice==2:
#         for s in Students:
#             s.showDetails()
#         print("")

#     elif choice==3:
#         id=int(input("Enter the id: "))
#         flag=0
#         student=None
#         for s in Students:
#             if s.id==id:
#                 flag=1
#                 student=s
#         if flag==1:
#             student.showDetails()
#             print("")
#         else:
#             print("Student not found!!")
#             print("")

#     elif choice==4:
#         id=int(input("Enter id: "))
#         flag=0
#         index=None
#         for i in range(0,len(Students)):
#             if Students[i].id==id:
#                 flag=1
#                 index=i
#         if flag==1:
#             Students.pop(index)
#             print("Student removed successfully..")
#             print("")
#         else:
#             print("Student not found!!")
#             print("")

#     elif choice==5:
#         break
#     else:
#         print("Please enter valid choice!!")
#         print("")

# **************EXAMPLE OF CLASS AND OBJECT*************
# class Sum:
#     def getValues(self):
#         Value1=int(input("Enter first num: "))
#         Value2=int(input("Enter second num: "))
#         return Value1+Value2

# s1=Sum()

# a=s1.getValues()
# print(a)

# **********FIND AREA AND PERIMETER OF SHAPE USING CLASS AND OBJECT**************
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def getArea(self):
#         pass

#     @abstractmethod
#     def getPerimeter():
#         pass

# class Square(Shape):
#     def __init__(self,side):
#         self.side=side

#     def getArea(self):
#         return self.side**2
    
#     def getPerimeter(self):
#         return self.side*4

# class Rectangle(Shape):
#     def __init__(self,length,breath):
#         self.length=length
#         self.breath=breath

#     def getArea(self):
#         return self.length*self.breath
    
#     def getPerimeter(self):
#         return 2*(self.length+self.breath)

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def getArea(self):
#         return self.radius*self.radius*3.14
    
#     def getPerimeter(self):
#         return 2*3.14*self.radius


# while True:
#     print("")
#     print("Enter as follows:-")
#     print("1. Calculate Area and Perimeter of Sqaure..")
#     print("2. Calculate Area and Perimeter of Rectangle..")
#     print("3. Calculate Area and Perimeter of Circle..")
#     print("4. Exit..")
#     choice=int(input(""))

#     if choice==1:
#         side=int(input("Enter the Side of Sqaure: "))
#         sq=Square(side)
#         print("The Area of Square is",sq.getArea())
#         print("The Perimeter of Square is",sq.getPerimeter())
#         print("")

#     elif choice==2:
#         length=int(input("Enter the Length of Rectangle: "))
#         breath=int(input("Enter the Breath of Rectangle: "))
#         rec=Rectangle(length,breath)
#         print("The Area of Rectangle is",rec.getArea())
#         print("The Perimeter of Rectangle is",rec.getPerimeter())
#         print("")

#     elif choice==3:
#         radius=int(input("Enter the Radius of Circle: "))
#         cir=Circle(radius)
#         print("The Area of Circle is",cir.getArea())
#         print("The Perimeter of Circle is",cir.getPerimeter())
#         print("")

#     elif choice==4:
#         break

#     else:
#         print("Invalid Input!!")
#         print("")

# *********CHANGE LIST USING FUNCTION WITH ARUGMENT AS LIST (NOT CHANGING ACTUAL LIST)***********
# def change_lst(lst):
#     print(id(lst))
#     lst.append(50)
#     print(id(lst))


# lst1=[10,20,30,40]
# print(lst1)
# change_lst(lst1 [:])
# print(lst1)

# ************ATM PROGRAM BY CLASS AND OBJECT**********
# class ATM:
#     def __init__(self):
#         self.pin=""
#         self.balance=0
#         self.menu()

#     def menu(self):
#         while True:
#             user_input=input("""
#                 Hello, how would you like to proceed:-
#                 1. Enter 1 to creat pin..
#                 2. Enter 2 to deposit..
#                 3. Enter 3 to withdraw..
#                 4. Enter 4 to check balance..
#                 5. Enter any other key to exit..
#                 """)

#             if user_input=="1":
#                 self.create_pin()
#             elif user_input=="2":
#                 self.deposit()
#             elif user_input=="3":
#                 self.withdraw()
#             elif user_input=="4":
#                 self.check_balance()
#             else:
#                 print("Bye")
#                 break

#     def create_pin(self):
#         self.pin=input("Enter the pin: ")
#         print("Pin set successfully..")

#     def deposit(self):
#         temp=input("Enter the pin: ")
#         if temp==self.pin:
#             amt=int(input("Enter the amount: "))
#             self.balance=self.balance+amt
#             print("Deposit successful..")
#         else:
#             print("Invalid pin!!")
#     def withdraw(self):
#         temp=input("Enter the pin: ")
#         if temp==self.pin:
#             amt=int(input("Enter the amount: "))
#             if amt<=self.balance:
#                 self.balance=self.balance-amt
#                 print("Withdraw successful..")
#             else:
#                 print("Insufficent balance!!")
#         else:
#             print("Invalid pin!!")
#     def check_balance(self):
#         temp=input("Enter the pin: ")
#         if temp==self.pin:
#             print("Your balance is",self.balance)
#         else:
#             print("Invalid pin!!")
    
# sbi=ATM()

# **************LIBRARY MANAGEMENT SYSTEM BY OOPS***********
class Library:

    list_of_lended_book = []

    def __init__(self, library_name, list_of_books):
        self.library_name = library_name
        self.list_of_books = list_of_books
        self.Menu()

    def Menu(self):
        print("""Enter choice as follows:-
        1. Display the books available
        2. Lend the book
        3. Donate the book
        4. Return Book
        5. List of Lended Books
        6. Exit
        """)
        while True:
            choice = int(input("Enter: "))

            if choice==1:
                self.Display_book()
            elif choice==2:
                self.Lend_book()
            elif choice==3:
                self.Donate_book()
            elif choice==4:
                self.Return_book()
            elif choice==5:
                self.Lended_books()
            elif choice==6:
                break
            else:
                print("Incorrect Value!!")

    def Display_book(self):
        print("The Books avaliable now are: ")
        print(self.list_of_books)

    def Lend_book(self):
        name=input("Enter your name: ")
        name_of_book=input("Enter the name of book you want to take: ")
        self.list_of_books.remove(name_of_book)
        print("Please collect the book from the counter and make sure to return it on or before the deadline..")
        dict = {name:name_of_book}
        self.list_of_lended_book.append(dict)

    def Lended_books(self):
        print("The lended books are:-")
        if len(self.list_of_lended_book)==0:
            print("No book lended!!")
        else:
            print(self.list_of_lended_book)

    def Donate_book(self):
        name_of_book=input("Enter the name of book you want to donate: ")
        self.list_of_books.append(name_of_book)
        print("Thank you donating the book :):)")

    def Return_book(self):
        name = input("Enter your name:- ")
        name_of_book=input("Enter the name of book you want to return: ")
        self.list_of_books.append(name_of_book)
        print("Thank you returning the book..")
        dict = {name : name_of_book}
        self.list_of_lended_book.remove(dict)


yogesh = Library("Yogesh's Library", [ "Rich Dad Poor Dad", "Think And Grow Rich", "Life's Amazing Secret", "Law of Attraction", "Zero to One" ])


# ************GENEATORS IN PYTHON FACTORIAL EXAMPLE****************
# def gen(n):
#     fact=1

#     for i in range(1,n+1):
#         fact = fact * i
#         yield fact

# factorial = gen(10)
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())
# print(factorial.__next__())


# ************GENEATORS IN PYTHON, PRINTING PATTERN USING GENERATOR****************
# def gen(n):
#     fact = ""

#     for i in range(0,n):
#         fact = fact + "*"
#         yield fact

# itr = gen(10)
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())
# print(itr.__next__())


# *********REVERSE THE KEY VALUE PAIR IN DICTIONARY USING LIST COMPREHENSIONS*************
# dict = {"Name": "Yogesh", "Language": "English", "City": "Indore"}

# dict1 = {value : key for key,value in dict.items()}

# print(dict)
# print(dict1)
