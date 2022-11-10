
# ****************TESTING FIRST PYTHON PROGRAM*****************
# print("Hello World")
# print("Bye")
# a=7
# b=8
# print(a+b)
# a,b=b,a
# print(a,b)


# *************TAKING 2 NUMBER BY USER AND ADDING THEM***************
# print("Enter the 1st number: ")
# var1=int(input())
# print("Enter the 2nd number: ")
# var2=int(input())
# print("The sum of two numbers is",var1+var2)


# ***************STRING SLICING & SOME FUNCTION***************
# mystr="Yogesh is a good boy"
# print(mystr[::])
# print(mystr[::2])
# print(mystr[::3])
# print(mystr[::300])
# print(mystr[::-2])
# print(type(mystr))
# print(mystr.isalnum())
# print(mystr.isalpha())
# print(mystr.endswith("boy"))
# print(mystr.count("o"))
# print(mystr.capitalize())
# print(mystr.find("good"))
# print(mystr.lower())
# print(mystr.upper())
# print(mystr.replace("is","are"))
# print(mystr.casefold())
# print(mystr.center(50))
# print(mystr.encode())
# print(mystr.expandtabs(200))
# print(mystr.swapcase())


# ************SHOPPING CART BILL WITH DISCOUNT AND NET PAYABLE***************
# quantity=int(input("Enter the quantity of product: "))
# rate=float((input("Enter the price of product: ")))
# discount=float(input("Enter the discount: "))
# bill=(quantity*rate)-(quantity*rate*discount)
# print("Your Bill amount is",quantity*rate)
# print("Your Discount amount is",quantity*rate*discount)
# print("Your Net Payable amount is:",bill)


# *****************TAKE INPUT OF RADIUS AND CALCULATE AREA AND CIRCUMFRENCE OF CIRCLE*************
# radius=int(input("Enter the radius of circle:"))
# area=3.14*(radius**2)
# circumfrence=2*3.14*radius
# print("The area of circle is",area)
# print("The circumfrence of circle is",circumfrence)


# ************ACCESS ITEM OF LIST IN LIST*****************
# l1=[1,2,3,4,5,["mra","yogi","dipa","abhi","ramu"]]
# print(l1[2],l1[5][0],l1[5][4])


# ************TAKING USER INPUT AND ACCESSING VALUE IN DICTIONARY******************
# dict={"1":"Yogesh","2":"Mritunjay","3":"Abhishek","4":"Dipanshu","5":"Ramu kaka"}
# key=input("Enter number to get the person name: ")
# print(dict.get(key))

# ***********FAULTY CALCULATOR EXCERCISE************
# var=input("Enter a. for addition, s. for subtraction, m. for multiplication, d. for division: ")
# num1=int(input("Enter first num: "))
# num2=int(input("Enter second num: "))
# if (var=="a"):
#     if (((num1==56) and (num2==9)) or ((num1==9) and (num2==56))):
#         print("The sum of two number is 77")
#     else:
#         print("The sum of two number is",num1+num2)
# elif (var=="s"):
#     print("The substrction of two number is",num1-num2)
# elif (var=="m"):
#     if(((num1==45) and (num2==3)) or ((num1==3) and (num2==45))):
#         print("The multiplication of two number is 555")
#     else:
#         print("The multiplication of two number is",num1*num2)
# elif (var=="d"):
#     if ((num1==56) and (num2==6)):
#         print("The divion of two number is 4")
#     else:
#         print("The division of two number is",num1/num2)
# else:
#     print("Incorrect input")


# ************IF, ELIF, ELSE EXAMPLE***************
# age =int(input("Enter your age: "))
# if age>=0 and age<=7:
#     print("You are not born yet!")
# elif age>7 and age<18:
#     print("Oops! You are not eligible to drive.")
# elif age==18:
#     print("Sorry! We are not able to decide. Please visit our nearby office to check your driving eligibility.")
# elif age>18 and age<=100:
#     print("Great! You can drive.")
# else:
#     print("Incorrect age. Please try again")

# print("Thank you :):)")


# **************BREAK EXAMPLE**********************
# num=int(input("Enter the number: "))

# while(True):
#     if num<100:
#         num=int(input("Enter the number: "))
#     else:
#         print("Great! You have entered a number greater than 100")
#         break

# *************CONTINUE EXAMPLE*************
# i=0
# while(i<20):
#     i=i+1
#     if i>=11 and i<=15:
#         continue
#     else:
#         print(i, end=" ")


# *************IF ELIF ELSE LADDER**************
# marks=int(input("Enter your marks: "))

# if(marks>90 and marks<=100):
#     print("Your grade are A+")
# elif(marks>80 and marks<=90):
#     print("Your grade are A")
# elif(marks>70 and marks<=80):
#     print("Your grade are B")
# elif(marks>=0 and marks<=70):
#     print("You failed the exam")
# else:
#     print("Invalid marks")


# ************GUESS THE NUMBER GAME**************
# print("***You have to guess the number between 0 to 50 in 5 attempts***")

# checknum=int(input("Guess the number: "))
# attempt=5

# while(checknum!=28):
#     attempt=attempt-1
#     if attempt==0:
#         print("No attempt left. Game over")
#         break
#     else:
#         if checknum>=0 and checknum<=10:
#             print("You have to enter a higer number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         elif checknum>=11 and checknum<=20:
#             print("You have to enter a liitle higer number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         elif checknum>=21 and checknum<=27:
#             print("You are very close, enter a little higher number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         elif checknum>=29 and checknum<=30:
#             print("You are very close, enter a little lower number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         elif checknum>=31 and checknum<=40:
#             print("You have to enter a little lower number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         elif checknum>=41 and checknum<=50:
#             print("You have to enter a lower number")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))
#         else:
#             print("This number is out of reach...")
#             print("Number of attempt left",attempt)
#             checknum=int(input("Guess the number: "))

# if attempt>0:
#     print("Hurrah! You got it")


# *********CHECK PRIME NUMBER*******
# num=int(input("Enter number to check for prime: "))

# for i in range(2,num):
#     if num%i==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")


# *******PRINT REVERSED LIST***********
# list1=[10,20,30,40,50]

# for item in list(reversed(list1)):
#     print(item)

# print(list1)


# *********FIBONACCI SERIES**********
# num1=0
# num2=1

# for i in range(1,12):
#     print(num1, end=" ")
#     num3=num1+num2
#     num1=num2
#     num2=num3


# ***********FOR LOOP EXAMPLE**********
# start=1500
# end=2701

# for i in range(start,end):
#     if(i%7==0) and (i%5==0):
#         print(i,end=" ")


# *********CELCIUS TO FARHENITE***********
# celcius=int(input("Enter degree in celcius: "))
# farh=(celcius*9/5)+32

# print("Degree is farhenaite is",farh)


# **************CHECK NUMBER OF EVEN AND ODD NUMBER**************
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even,odd=0,0
# for item in numbers:
#     if item%2==0:
#         even=even+1
#     else:
#         odd=odd+1

# print("Even number are",even,"and odd number are",odd)


# ************FIZZ BUZZ*****************
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz", end=" ")
#     elif i%5==0:
#         print("Buzz", end=" ")
#     elif i%3==0:
#         print("Fizz", end=" ")
#     else:
#         print(i, end=" ")


#****************ENTER MONTH AND GET DAYS************** 
# monthday={"January":31,"Febraury":"28/29","March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
# month=input("Enter the month for days: ")

# print("The number of days are ",monthday.get(month))


# ************PRINT -10 TO -1 NUMBERS*************
# for i in range(-10,0):
#     print(i)


# **********CHECK NUMBER OF DIGIT AND LETTER IN STRING**************
# str=input("Enter string: ")
# num="0123456789"
# digit,letter=0,0
# for item in str:
#     if item in num:
#         digit=digit+1
#     else:
#         letter=letter+1

# print("Digit:",digit,"Letter",letter)


# **************CHECK FOR VOWEL*************
# alfabet="aeiou"

# letter=input("Enter character to check for vowel: ")

# if letter in alfabet:
#     print("Vowel")
# else:
#     print("Consonant")


# **********NUMBER PATTERN********
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# for i in range(10):
#     print(str(i)*(i))


# ***********STAR PATTERN***********
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
# for i in range(4,0,-1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print("")

# ************STAR PATTERN**********
#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,6):
#     for j in range(6,i+1,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")

#     * 
#    ** 
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
# for i in range(1,6):
#     for j in range(6,i+1,-1):
#         print(" ",end="")
#     for s in range(1,i+1):
#         print("*",end="")
#     print("")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for s in range(5,i,-1):
#         print("*",end="")
#     print("")

# ********STAR PATTERN**********
#     *
#    **
#   ***
#  ****
# *****
# ****
# ***
# **
# *
# for i in range(1,6):
#     for j in range(6,i+1,-1):
#         print(" ",end="")
#     for s in range(1,i+1):
#         print("*",end="")
#     print("")

# for i in range(1,6):
#     for j in range(1,i+1,-1):
#         print(" ",end="")
#     for s in range(5,i,-1):
#         print("*",end="")
#     print("")


# *********EXAMPLE OF FUNCTION AND DOCSTRING IN FUNCTION*************
# def sum1(a,b):
#     """This fuction takes two number and calculate the sum"""
#     print("The sum of a & b is",a+b)

# print(sum1.__doc__)
# sum1(5,5)


# ***************IT WILL TAKE INPUT OF NUMBER OF ROWS AND PRINT STAR PATTERN IF TRUE AND REVERSE PATTERN IF FALSE****************
# print("Enter:-")
# print("0. for star pattern")
# print("1. for reversed star pattern")
# var=bool(int(input()))
# n=int(input("Enter the number of rows: "))

# if var==False:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print("")
# if var==True:
#     for i in range(1,n+1):
#         for j in range(n+1,i,-1):
#             print("*",end="")
#         print("")

# var1=input("Enter y to continue and n to exit: ")

# while var1=="y":
#     print("Enter:-")
#     print("0. for star pattern")
#     print("1. for reversed star pattern")
#     var=bool(int(input()))
#     n=int(input("Enter the number of rows: "))

#     if var==False:
#         for i in range(1,n+1):
#             for j in range(1,i+1):
#                 print("*",end="")
#             print("")
#     if var==True:
#         for i in range(1,n+1):
#             for j in range(n+1,i,-1):
#                 print("*",end="")
#             print("")

#     var1=input("Enter y to continue and n to exit: ")


# ***********CALULATING FACTORIAL OF A NUMBER USING ITERATIVE AND RECURSIVE APPROACH***********
# def factorial(n):
#     for i in range(1,n+1):
#         if n==1:
#             return 1
#         else:
#             return n*factorial(n-1)

# n=int(input("Enter the number for factorial: "))
# # recursive approach
# fact=factorial(n)
# print("Foctorial with recursive approach is",fact)

# # iterative approach
# facto=1
# for i in range(1,n+1):
#     facto=facto*i

# print("Foctorial with iterative approach is",facto)


# ************FIBONACCI SERIES WITH RECURSIVE FUNCTION**************
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n=int(input("Enter the index of fibonacci series: "))
# fib=fibonacci(n)
# print("The value at index is:",fib)


# *************RETURN MAX VALUE OF THREE NUMBER USING FUNCTION**************
# def maximum(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# x=int(input("Enter value of x:"))
# y=int(input("Enter value of y: "))
# z=int(input("Enter value of z: "))

# max=maximum(x,y,z)
# print("The maximum number is:",max)


# *************SUM OF NUMBERS OF LIST USING FUNCTION**************
# def sum(numbers):
#     total=0
#     for item in numbers:
#         total=total+item

#     print("THe sum is",total)

# sum((100,100,100,100,100))


# ***********MULITPLICATION OF ALL NUMBERS OF LIST USING FUNCTION*************
# def multiply(numbers):
#     total=1
#     for item in numbers:
#         total=total*item

#     print("THe multiplication is",total)

# multiply((6,5,4,3,2,1))


# **************REVERSE THE STRING USING FUNCTION***************
# def reverse_string(str1):
#     rstr1=""
#     index=len(str1)
#     while index>0:
#         rstr1=rstr1+str1[index-1]
#         index=index-1

#     return rstr1

# print(reverse_string("dcba4321"))


# ***************CALUCLATE UPPERCASE AND LOWERCASE ALPHABET IN STRING***************
# def case_counter(string):
#     lower=0
#     upper=0
#     for i in string:
#         if i.islower()==True:
#             lower=lower+1
#         elif i.isupper():
#             upper=upper+1
#         else:
#             pass

#     print(lower,upper,end=" ")

# case_counter("YogEsh iS A gOOd BOy")


# ************FUNCTION WHICH RETURNS THE UNIQUE VALUE LIST OF GIVEN LIST***************
# def unique_list(str1):
#     str2=[]
#     for i in str1:
#         if i not in str2:
#             str2.append(i)

#     return str2

# print(unique_list([1,1,2,2,3,3,4,4,5,5]))


# *************PRINT PRIME NUMBER TILL THE GIVEN NUMBER***********
# def check_prime(n):
#     count=0

#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(n, end=" ")

# n=int(input("Enter range to check for prime numbers: "))
# for i in range(2,n+1):
#     check_prime(i)


# ************FUNCTION WHICH TAKES LIST AND RETURN THE NUMBER WHICH ARE EVEN**************
# def even_number(list1):
#     list2=[]
#     for item in list1:
#         if item%2==0:
#             list2.append(item)

#     return list2

# print(even_number([1,2,3,4,5,6,7,8,9,10]))


# *************FUNCTION TO CHECK IF THE STRING IS PALINDROME OR NOT*************
# def check_palindrome(str1):
#     str1=str1.lower()
#     str2=""
#     index=len(str1)
#     while index>0:
#         str2=str2+str1[index-1]
#         index-=1

#     if str1==str2:
#         print("Its a palindrome")
#     else:
#         print("Its not a palindrome")

# check_palindrome("racecaR")


# ************FUNCTION WHICH RETURNS THE LIST OF SQUARED ITEMS**************
# def squareList(numbers):
#     squareNumbers=[]
#     for item in numbers:
#         squareNumbers.append(item**2)
    
#     return squareNumbers

# print(squareList([1,2,3,4,5]))


# ***********FUNCTION TO GET KEYS AND VALUES FROM DICTIONARY*************
# def dictComposer(dict1):
#     dict1key=[]
#     dict1value=[]

#     dict1key.append(list(dict1.keys()))
#     dict1value.append(list(dict1.values()))

#     print("The key in dict are:",dict1key)
#     print("The value in dict are:",dict1value)


# dictComposer({"Name":"Yogesh","Sirname":"Hasija"})


# ***********EXAPMLE OF LAMBDA FUNCTION*****************
# addNum = lambda x,y:x+y
# print(addNum(50,501))

# multiplyNum = lambda x,y:x*y
# print(multiplyNum(8,10))


#***********RANDOM MODULE IN PYTHON************ 
# import random

# random_number=random.randint(1,10)
# print(random_number)

# rand=random.random()*100
# print(rand)

# lst=["amit","abhishek","yusuf","rakesh","ashutosh"]
# choice=random.choice(lst)
# print(choice)


# ***********EXAMPLE OF F'STRING************ 
# x=9
# y=19
# print(f"Value of x & y is {x} & {y}")


# ************ SNAKE, WATER & GUN GAME************
# SNAKE VS WATER = SNAKE
# SNAKE VS GUN = GUN
# GUN VS WATER = WATER
# GUN VS SNAKE = GUN
# WATER VS SNAKE = SNAKE
# WATER VS GUN = WATER
# import random

# def selectChoice():
#     lst=["s","w","g"]
#     choice=random.choice(lst)
#     return choice

# print("\n*****Welcome to the Game - Snake, Water & Gun*****\n")
# userPoint=0
# cpuPoint=0
# round=1

# while round<=10:
#     print("Round no.",round)
#     round+=1
#     userChoice=input("Enter s. for snake, w. water, g. for gun: ")
#     cpuChoice=selectChoice()
#     if (userChoice=='s' and cpuChoice=='w'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("You got a point!!")
#         userPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     elif (userChoice=='s' and cpuChoice=='g'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("Cpu got a point!!")
#         cpuPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     elif (userChoice=='g' and cpuChoice=='w'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("Cpu got a point!!")
#         cpuPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     elif (userChoice=='g' and cpuChoice=='s'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("You got a point!!")
#         userPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     elif (userChoice=='w' and cpuChoice=='s'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("Cpu got a point!!")
#         cpuPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     elif (userChoice=='w' and cpuChoice=='g'):
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("You got a point!!")
#         userPoint+=1
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")
#     else:
#         print("Your choose:",userChoice)
#         print("Cpu choice was:",cpuChoice)
#         print("Round was draw!!")
#         print(f"The score is you:{userPoint} cpu:{cpuPoint}\n")

# if userPoint>cpuPoint:
#     print("Congrats! You win the game:):)\n")
# elif userPoint<cpuPoint:
#     print("Oops! You lose, better luck next time...\n")
# else:
#     print("It's a draw...\n")


# ********EXAMPLE OF *ARGS*************
# def func_args(name, *actualname):
#     print(name)
#     for item in actualname:
#         print(item)

# line="These are the names:-"
# lst=["Abhi","Kikku","Pappu", "Akki", "Sallu"]
# func_args(line, *lst)


# EXAMPLE OF *ARGS AND **KWARGS***********
# def func_args(name, *actualname, **kwargs):
#     print(name)
#     for item in actualname:
#         print(item)
#     for key,value in kwargs.items():
#         print(key,value)


# line="These are the names:-"
# lst=["Abhi","Kikku","Pappu", "Akki", "Sallu"]
# kw={"1":"Hello", "2":"Bye","3":"Hii"}
# func_args(line, *lst, **kw)


# *********TWO FUNCTION OF TIME MODULE***********
# import time
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)

# p=1
# while p<61:
#     print(p)
#     p=p+1
#     time.sleep(1)


# *********TAKE USER INPUT ELEMENT AND STORE THEM IN LIST AND TUPLE**********
# n=int(input("Enter number of element to be stored in list: "))
# lst=[]
# for i in range(1,n+1):
#     i=int(input("Enter element: "))
#     lst.append(i)
# print(lst)
# tup=tuple(lst)
# print(tup)


# **********TAKE FILE NAME AS INPUT AND PRINT THE EXTENSION OF FILE*************
# abc=input("Enter the name of file: ")
# lst=abc.split(".")
# print(lst[-1])


# **********PRINT FIRST AND LAST ELEMENT OF LIST*************
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])


# **********PRINT EXACT DATE OF EXAM***********
# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)


# *********TAKE AND INTEGER 'N' AND PRINT SUM OF N+NN+NNN********** 
# n=input("Enter number: ")
# num=0
# sum=0
# lst=[]
# for i in range(1,4):
#     lst.append(n*i)

# for item in lst:
#     item=int(item)
#     sum=sum+item

# print(sum)
# ALTERNATE METHOD
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)


# **********TAKE YEAR AS INPUT AND PRINT THE CALENDAR FOR THE SAME***********
# import calendar

# year=int(input("Enter the year: "))

# print(calendar.calendar(year))


# ********TAKE INPUT OF TWO DATES AND CALCULATE THE NUMBER OF DAYS BETWEEN THEM*********
# from datetime import date
# f_date=date(2014, 7, 15)
# l_date=date(2014, 8, 11)
# days=l_date-f_date
# print(days)


# ****Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference****
# num=int(input("Enter number: "))
# num2=17

# if num>17:
#     print(2*(num-num2))

# else:
#     print(num2-num)


# ********IF STRING BEGINS WITH "IS" RETURN STRING ELSE ADD "IS" IN BEGINNING********
# prt="Yogesh"
# x=prt.startswith("Is")
# if x==True:
#     print(prt)
# else:
#     print("Is "+prt)


# *********PRINT STRING AND ITS NUMBE ROF COPIES WANTED*********
# prt="abc"
# copies=2
# print(prt*copies)


# ********COUNT NUMBER OF 4 IN LIST********
# lst=[1,4,8,6,4,3,8,4,2]
# x=lst.count(4)
# print(x)


# *******CHECK NUMBER IN LIST OR NOT***********
# lst=[1,2,3,4,5,6,7,8,9,10]

# print(11 in lst)


# ********PRINT HISTOGRAM AS MANY TIMES AS ELEMENT IN LIST********** 
# def histogram(item):
#     for i in item:
#         print("*"*i)

# histogram([2,3,6,5])


# *********CONCATINATE ALL ELEMENT OF LIST TO STRING***********
# lst=["I"," ", "am", " ", "yogi"]
# lst1=""
# for i in lst:
#     lst1 = lst1 + i

# print(lst1)


# **********PRINT EVEN NUMBER IN LIST TILL NUMBER IS EQUAL 237************
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for item in numbers:
#     if item==237:
#         print(item, end=" ")
#         break
#     elif item%2==0:
#         print(item, end=" ")


# *******PRINT ITEM WHICH ARE NOT PRESENT IN SECOND LIST**********
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2))


# *************CALCULATE GREATEST COMMON DIVICIBLE OF TWO NUMBER**********
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# lst1=[]
# lst2=[]
# for i in range(1,num1):
#     if num1%i==0:
#         lst1.append(i)

# for i in range(1,num2):
#     if num2%i==0:
#         lst2.append(i)

# set1=set(lst1)
# set2=set(lst2)
# print(max(set1.intersection(set2)))


# *********IF INPUT IS INTEGER PRINT SUM ELSE PRINT INPUT NOT INTEGER**********
# def intsum(a,b):
#     if type(a)==int and type(b)==int:
#         print(a+b)
#     else:
#         print("Input should be integer!")

# intsum(5,5)


# ***************DISTANCE BETWEEN TWO POINTS************
# import math

# x=[4,0]
# y=[6,6]
# dist=math.sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2))
# print(dist)


# *************CHECK WHEATHER THE SYSTEM IS IN 34 OR 64 BIT***********
# import struct

# print(struct.calcsize("P")*8)


# ************CHECK THE OS AND SYSTEM INFORMATION************
# import platform
# import os

# print(os.name)
# print(platform.system())
# print(platform.release())
# print(platform.architecture())
# print(platform.machine())


# ********CHECK SITE PACKAGES**********
# import site
# print(site.getsitepackages())


# **********GET PATH OF CURRENT FILR*********
# import os
# print(os.path.realpath(__file__))


# *********CHECK NUMBER OF CPUs***********
# import multiprocessing
# print(multiprocessing.cpu_count())


# *********CONVERT STRING INTO FLOAT AND INTEGER*********
# a="351.456"
# print(float(a))
# print(int(float(a)))


# *********PRINT AN ARMSTRONG NUMBER FROM 1 TO 1,00,000********
# def armstrong(number):
#     copynum=number
#     count=0
#     while copynum>0:
#         count+=1
#         copynum=copynum//10

#     temp=number
#     sum=0
#     while temp>0:
#         sum=sum+((temp%10)**count)
#         temp=temp//10

#     if number==sum:
#         print(number,end=" ")


# for i in range(0,100001):
#     armstrong(i)