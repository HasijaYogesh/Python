# Q1. INPUT A NUMBER AND CALCULATE IT'S SQAURE********** 
# num=int(input("Enter the number for square: "))
# print("The square of number is",num**2)


# Q2. SWAP VALUE OF TWO VARIABLES USING THIRD VARIABLE*************
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))

# c=a
# a=b
# b=c
# print("The value of a is",a)
# print("The value of b is",b)


# Q3. SWAP VALUE OF TWO VARIABLE WITHOUT USING THIRD VARIABLE*********
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))

# a,b=b,a
# print("The value of a is",a)
# print("The value of b is",b)


# Q4. CALCULATE THE AREA OF TRIANGLE**********
# base=int(input("Enter the base of triangle: "))
# height=int(input("Enter the height of triangle: "))

# area=(base*height)/2

# print("The area of triangle is",area)


# Q5. CALCULATE THE AREA OF CIRCLE**********
# radius=int(input("Enter the radius of circle: "))
# area=3.14*radius*radius
# print("The area of circle is",area)


#Q6. CALCULATE THE SIMPLE INTEREST**********
# principle=int(input("Enter the principle amount: "))
# rate=int(input("Enter the interest rate: "))
# years=int(input("Enter the number of years: "))

# simple_interest=(principle*rate*years)/100

# print("The simple interest is:",simple_interest)


#Q7. CONVERT KILOMETER IN MILEMETER*********
# kilometer=int(input("Enter kilometer to convert to miles: "))
# miles=kilometer*0.621371
# print(f"The {kilometer} kilometer in miles is {miles}")


# Q8. CALUCLATE AVERAGE OF THREE NUMBER**********
# a=int(input("Enter the value of 1st number: "))
# b=int(input("Enter the value of 2nd number: "))
# c=int(input("Enter the value of 3rd number: "))
# average=(a+b+c)/3
# print("The average of three number is",average)


# Q9. CONVERT CELSIUS TO FAHRENHEIT*********
# celsius=int(input("Enter temperature in celsius: "))
# fahrenheit=(9/5)*celsius+32
# print("The temperature in fahrenheit is:",fahrenheit)


# Q10. CONVERT FAHRENHEIT TO CELSIUS*********
# fahrenheit=int(input("Enter temperature in fahrenheit: "))
# celsius=(fahrenheit-32)*5/9
# print("The temperature in celsius is:",celsius)


# Q11. CALCULATE NUMBER OF NOTES IN AN AMOUNT - 2000,1000,500,100,50,20,10,5,1**********
# amount=int(input("Enter amount: "))
# note2000=note1000=note500=note100=note50=note20=note10=note5=note1=0
# if amount>=2000:
#     while amount>=2000:
#         note2000+=1
#         amount=amount-2000
# print("2000 x",note2000,"=",note2000*2000)

# if amount>=1000:
#     while amount>=1000:
#         note1000+=1
#         amount=amount-1000
# print("1000 x",note1000,"=",note1000*1000)

# if amount>=500:
#     while amount>=500:
#         note500+=1
#         amount=amount-500
# print(" 500 x",note500,"=",note500*500)

# if amount>=100:
#     while amount>=100:
#         note100+=1
#         amount=amount-100
# print(" 100 x",note100,"=",note100*100)

# if amount>=50:
#     while amount>=50:
#         note50+=1
#         amount=amount-50
# print("  50 x",note50,"=",note50*50)

# if amount>=20:
#     while amount>=20:
#         note20+=1
#         amount=amount-20
# print("  20 x",note20,"=",note20*20)

# if amount>=10:
#     while amount>=10:
#         note10+=1
#         amount=amount-10
# print("  10 x",note10,"=",note10*10)

# if amount>=5:
#     while amount>=5:
#         note5+=1
#         amount=amount-5
# print("   5 x",note5,"=",note5*5)

# if amount>=1:
#     while amount>=1:
#         note1+=1
#         amount=amount-1
# print("   1 x",note1,"=",note1*1)


# Q12. CALCULATE SUM OF FIRST AND LAST DIGIT IN FOUR DIGIT NUMBER**********
# number=int(input("Enter the 4 digit number: "))

# last_digit=number%10

# while number>10:
#     number=number/10

# first_digit=int(number)
# sum=first_digit+last_digit

# print("The sum of first and last digit is:",sum)


# Q13. TAKE INPUT OF 5 MARKS AND CALCULATE TOTAL MARKS AND TOTAL PERCENTAGE**********
# marks1=int(input("Enter the marks of first subject(out of 100): "))
# marks2=int(input("Enter the marks of second subject(out of 100): "))
# marks3=int(input("Enter the marks of third subject(out of 100): "))
# marks4=int(input("Enter the marks of fourth subject(out of 100): "))
# marks5=int(input("Enter the marks of fifth subject(out of 100): "))

# totalmarks=marks1+marks2+marks3+marks4+marks5
# percentage=(totalmarks/500)*100

# print("The total marks are:",totalmarks)
# print("The percentage are:",percentage,"%")


# Q14. TAKE INPUT OF CHARACTER AND PRINT IT'S ASCII VALUE***********
# a=input("Enter the character for Ascii value: ")
# print(ord(a))


# Q15. PROGRAM WHICH ACCEPT THREE DIGIT NUMBER AND REVERSE IT AND THEN CALCULATE SUM OF ALL DIGITS*******
# number=int(input("Enter three digit number: "))
# remainder=0
# reversenum=0
# while number>0:
#     remainder=int(number%10)
#     reversenum=int(reversenum*10) + int(remainder)
#     number=int(number/10)

# print("The reverse number is:",reversenum)

# sum=0
# while reversenum>0:
#     sum = sum + int(reversenum%10)
#     reversenum = int(reversenum/10)

# print("The sum of all digits is:",sum)


# Q16. WRITE A PROGRAM THAT ACCEPTS A NUMERIC VALUE FROM USER AND PRINT ITS CORRESPONDING CHARACTER*********
# number=int(input("Enter numberic value for corresponding character: "))
# print(chr(number))


#  Q17. CALUCULATE GROSS SALARY AND NET SALARY FROM BASIC SALARY***********
# basic_salary=int(input("Enter the basic salary: "))
# travel_all = basic_salary*0.1
# provident_fund = basic_salary*7.8/100
# dearness_all = 500

# gross_salary = basic_salary + dearness_all + travel_all
# print("The gross salary is:",gross_salary)

# net_salary = gross_salary - provident_fund
# print("The net salary is:",net_salary)


# Q18. ACCEPT AND NUMBER AND CHECK IF NUMBER IS POSITIVE OR NEGATIVE**********
# number=int(input("Enter the number: "))

# if number<0:
#     print("Negative")
# elif number>0:
#     print("Positive")
# else:
#     print("0 is neither positive nor negative")


# Q19. CALUCLATE THAT FIRST INPUT NUMBER IS DIVISIBLE BY SECOND INPUT NUMBER**********
# first_num=int(input("Enter first number: "))
# second_num=int(input("Enter second number: "))

# if first_num%second_num==0:
#     print("Its divisible")
# else:
#     print("Its not divisible")


# Q20. CHECK IF INPUT NUMBER IS PALINDROME OR NOT**********
# number=int(input("Enter the number: "))
# actualnum=number
# remainder, reversenum=0,0
# while number>0:
#     remainder=int(number%10)
#     reversenum=int(reversenum*10+remainder)
#     number=int(number/10)

# if actualnum==reversenum:
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")


# Q21. CHECK IF THE NUMBER IS ARMSTRONG OR NOT********
# number=int(input("Enter the number to check for Armstrong: "))
# temp=number
# sum=0
# while number>0:
#     sum=sum+((number%10)**3)
#     number=number//10

# if temp==sum:
#     print("Its an Armstrong number")
# else:
#     print("Its not an Armstrong number")


# Q22. ACCEPT 3 DIGIT NUMBER FROM USER AND FIND THE GREATEST DIGIT******
# number=int(input("Enter the number: "))
# lst=[]
# while number>0:
#     lst.append(number%10)
#     number=number//10
# maxnum=max(lst)
# print(maxnum)


# Q23. CLACULATE WHEATHER YEAR IS LEAP YEAR OR NOT********
# year=int(input("Enter year to check for leap year: "))

# if year%400==0:
#     print("Its a leap year")
# elif year%4==0 and year%100!=0:
#     print("Its a leap year")
# else:
#     print("Its not a leap year")


# Q24. PROGRAM TO CHECK IF CHAR IS A VOWEL OR A CONSONANT******
# char=input("Enter character: ")
# lst=['a','e','i','o','u','A','E','I','O','U']
# if char in lst:
#     print("Its a vowel")
# else:
#     print("Its a consonant")


# Q25. CHECK IF CHARACTER IS LOWERCASE OR UPPERCASE******
# char=input("Enter charcter: ")

# if ord(char)>=97 and ord(char)<=122:
#     print("Lowercase")
# elif ord(char)>=65 and ord(char)<=90:
#     print("Uppercase")
# else:
#     print("Not defined")


# Q26. CALCULATE SMALLEST NUMBER OF GIVEN THREE NUMBER******
# lst=[]
# num1=int(input("Enter first number: "))
# lst.append(num1)
# num2=int(input("Enter second number: "))
# lst.append(num2)
# num3=int(input("Enter third number: "))
# lst.append(num3)

# minnum=min(lst)
# print(minnum)


# Q27. CALCULATE LARGEST NUMBER OUT OF GIVEN FOUR NUMBER*******
# lst=[]
# num1=int(input("Enter first number: "))
# lst.append(num1)
# num2=int(input("Enter second number: "))
# lst.append(num2)
# num3=int(input("Enter third number: "))
# lst.append(num3)
# num4=int(input("Enter fourth number: "))
# lst.append(num4)

# maxnum=max(lst)
# print(maxnum)


# Q28. PROGRAM THAT ACCEPT THE MARKS(100), CALULATE SUM AND DISPLAY GRADE ACCORDING TO THE GIVEN CONDITION******
# marks1=int(input("Enter marks of first subject: "))
# marks2=int(input("Enter marks of second subject: "))
# marks3=int(input("Enter marks of third subject: "))
# marks4=int(input("Enter marks of fourth subject: "))
# marks5=int(input("Enter marks of fifth subject: "))
# sum=marks1+marks2+marks3+marks4+marks5
# percentage=(sum/500)*100

# if percentage>=60 and percentage<=100:
#     print("You got grade 'A'")
# elif percentage>=50:
#     print("You got grade 'B'")
# elif percentage>=40:
#     print("You got grade 'C'")
# else:
#     print("You got grade 'D'")


# Q29. PROGRAM FOR GENERATING ELECTRICITY BILL THAT ACCEPTS LAST AND CURRENT MONTH UNIT AND CALCULATE THE BILL AS:
# 0-100 - RS 2, 101-200 - RS 3, 201-300 - RS 4, ABOVE 300 - RS 5************
# num1=int(input("Enter current month unit: "))
# num2=int(input("Enter last month unit: "))
# num3=num1-num2
# sum=0
# if num3>300:
#     sum=sum+(num3-300)*5
#     num3=300
# if num3>201 and num3<=300:
#     sum=sum+((num3-200)*4)
#     num3=200
# if num3>101 and num3<=200:
#     sum=sum+((num3-100)*3)
#     num3=100
# if num3>0 and num3<=100:
#     sum=sum+(num3*2)

# print("Your electricity bill is:",sum)

# 266
# 266-200=66*4=264+500=764
# 



# Q30. PROGRAM TO CALCULATE FACTORIAL OF ANY NUMBER**********
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i

#     return fact

# num=int(input("Enter the number for factorial: "))
# factnum=factorial(num)
# print(f"The factorial of {num} is {factnum}")


# Q31. PRINT THE TABLE OF GIVEN NUMBER*******
# def table(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")

# num=int(input("Enter the number for table: "))
# table(num)


# Q32. PROGRAM TO PRINT FIBONACCI SERIES*******
# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
    
#     return fibonacci(n-1)+fibonacci(n-2)

# num=int(input("Enter the index of fibonacci series: "))
# for i in range(0,num+1):
#     print(fibonacci(i), end=" ")


# Q33. PROGRAM THAT ACCEPTS N NUMBER FROM USER AND CALCULATE MAXIMUM AND MINIMUM NUMBER********
# n=int(input("Enter the count of number: "))
# lst=[]
# for i in range(1,n+1):
#     i=int(input(f"Enter {i} number: "))
#     lst.append(i)

# maxnum=max(lst)
# minnum=min(lst)
# print(f"The maximum number is {maxnum} and minimum number is {minnum}")


# Q34. PROGRAM TO CALCULATE SUM OF SQAURE OF GIVEN N NUMBERS*********
# num=int(input("Enter the number: "))
# sum=0
# for i in range(1,num+1):
#     sum=sum+(i**2)

# print(f"The sum of sqaure is {sum}")


# Q 35.PROGRAM TO CALULCATE SUM OF SERIES 1/1+1/2+1/3+1/4+....1/N**********
# num=int(input("Enter the number: "))
# sum=0
# for i in range(1,num+1):
#     sum=sum+1/i

# print(f"The sum of series is {sum}")


# Q36. CALCULATE THE SUM OF SERIES 1/1! + 1/2! + 1/3! +1/4! +.....+1/N!*********

# def factorial(n):
#     fact=1

#     for i in range(1,n+1):
#         fact=fact*i

#     return fact

# num=int(input("Enter the number: "))
# sum=0
# for i in range(1, num+1):
#     sum=sum + (1/factorial(i))

# print(sum)

# Q37. CALCULATE SUM OF DIGITS OS GIVEN NUMBER**********
# number=int(input("Enter number: "))
# sum=0
# while number>0:
#     sum=sum+(number%10)
#     number=number//10

# print(f"The sum of all digits is {sum}")


# Q38. CHECK WHEATHER THE NUMBER IS ARMSTRONG OR NOT*******
# actualnum=int(input("Enter the number to check for Armstrong: "))
# copynum1=actualnum
# copynum2=actualnum
# count=sum=0
# while copynum1>0:
#     count+=1
#     copynum1=copynum1//10

# while copynum2>0:
#     sum=sum+((copynum2%10)**count)
#     copynum2=copynum2//10

# if actualnum==sum:
#     print("Its an Armstrong number")
# else:
#     print("Its not an Armstrong number")


# Q39. PROGRAM TO FIND THE FACTORS OF ANY NUMBERS********
# num=int(input("Enter the number for its factor: "))

# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=" ")


#Q40. PROGRAM TO CHECK THE NUMBER IS PERFECT OR NOT*******
# num=int(input("Enter the number to check for perfect number: "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i

# if num==sum:
#     print("The number is perfect number")
# else:
#     print("The number is not a perfect number")


# Q41. ACCEPT N NUMBERS FROM USER AND CALUCLATE NUMBER OF EVEN OND ODD********
# num=int(input("Enter no. of elements: "))

# lst=[]
# for i in range(1,num+1):
#     item=int(input(f"Enter {i} elements: "))
#     lst.append(item)

# even=odd=0

# print(lst)

# for item in lst:
#     if item%2==0:
#         even+=1
#     else:
#         odd+=1

# print(f"The even numbers are {even} and odd numbers are {odd}")


# Q42. PROGRAM TO FIND LCM OF TWO NUMBERS*********
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# startnum=0
# lcm=0

# if num1>num2:
#     startnum=num1
# else:
#     startnum=num2

# for i in range(startnum,(num1*num2)+1):
#     if i%num1==0 and i%num2==0:
#         lcm=i
#         break

# print("The lcm of two numbers is",lcm)


# Q43. WRITE A PROGRAM TO CALCULATE FACTORIAL USING FUNCTION WITH ARGUMENT AND RETURN TYPE********
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i

#     return fact

# num=int(input("Enter the number for factorial: "))
# result=factorial(num)
# print(f"The factorial of {num} is {result}")


# Q44. CHECK FOR PRIME NUMBER USING FUNCTION WITH RETURN TYPE AND ARGUMENT***********
# def checkprime(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1

#     if count==2:
#         return True
#     else:
#         return False

# num=int(input("Enter number to check for prime: "))
# if checkprime(num)==True:
#     print("Its a prime number")
# else:
#     print("Its not a prime number")


# Q45. PROGRAM TO TAKE N NUMBER FROM USER AND STORE IN LIST. ALSO, PERFORM OPERATION MAX, MIN, SUM & AVERAGE***
# count=int(input("Enter the number of element in a list: "))
# lst=[]
# for i in range(1,count+1):
#     num=int(input(f"Enter the {i} num: "))
#     lst.append(num)

# max=max(lst)
# min=min(lst)
# sum=sum(lst)
# avr=sum/count
# print(f"The maximum element is: {max}")
# print(f"The minimum element is: {min}")
# print(f"The sum of all elements is: {sum}")
# print(f"The average of all element is: {avr}")


# Q46. WRITE A PROGRAM TO SEARCH A NUMBER AND DELETE ALL (IF REPEAT) IN LIST************
# lst=[10,20,50,10,50,80,40]
# print("The list of numbers is",lst)

# num=int(input("Enter number you want to search: "))

# print(f"The index of {num} is {lst.index(num)}")

# lst1=lst[:(lst.index(num))+1]
# lst2=lst[lst.index(num):]

# for item in lst2:
#     if item==num:
#         lst2.remove(num)

# print("The list after deleteing the duplicate number",lst1+lst2)


# Q47. COMPARE TWO LIST AND PRINT ALL COMMON ITEMS**************
# lst1=[10,20,30,40,50,30,50]
# lst2=[15,25,30,45,50,30,50]
# lst3=[]
# for item in lst1:
#     if item in lst2:
#         lst3.append(item)

# lst3=set(lst3)
# print(lst3)

# Q48. WRITE A PROGRAM TO CONVERT KEYS INTO VALUE AND VALUE INTO KEYS IN DICTIONARY*********

# dict = {"Name": "Shubham", "Age": "23", "Language":"Python"}

# print("The orginal dict is:",dict)

# dict = {value:key for key,value in dict.items()}

# print("The reverse dict is:",dict)


# Q49. 
# num =int(input("Enter the number of Student: "))

# lst=[]

# for i in range(1,num+1):
#     print("")
#     print(f"Enter data of {i} studnet")
#     roll=(input("Enter Studnet's roll no.: "))
#     name=(input("Enter Studnet's name: "))
#     branch=(input("Enter Studnet's branch: "))
#     mark1=int(input("Enter marks of 1st subject: "))
#     mark2=int(input("Enter marks of 2nd subject: "))
#     mark3=int(input("Enter marks of 3rd subject: "))
#     mark4=int(input("Enter marks of 4th subject: "))
#     mark5=int(input("Enter marks of 5th subject: "))

#     dict={"Roll no.": roll, "Name": name, "Branch": branch, "Marks": (mark1,mark2,mark3,mark4,mark5)}
#     lst.append(dict)


# Q50. IT WAS IN COUNTINUATION WITH QUESTION 49***********
# PART A - FIND THE FIRST 5 TOPPER IN LIST**********
# lst=[{'Roll no.': '101', 'Name': 'bantu', 'Branch': 'cs', 'Marks': (66,66,66,66,66)},
#      {'Roll no.': '102', 'Name': 'prakash', 'Branch': 'cs', 'Marks': (44,44,44,44,44)},
#      {'Roll no.': '103', 'Name': 'aadarsh', 'Branch': 'cs', 'Marks': (88,88,88,88,88)},
#      {'Roll no.': '104', 'Name': 'kaber', 'Branch': 'tech', 'Marks': (22,22,22,22,22)},
#      {'Roll no.': '105', 'Name': 'umang', 'Branch': 'tech', 'Marks': (99,99,99,99,99)}, 
#      {'Roll no.': '106', 'Name': 'bholu', 'Branch': 'tech', 'Marks': (55,55,55,55,55)},
#      {'Roll no.': '107', 'Name': 'gopal', 'Branch': 'me', 'Marks': (11,11,11,11,11)},
#      {'Roll no.': '108', 'Name': 'harish', 'Branch': 'me', 'Marks': (33,33,33,33,33)},
#      {'Roll no.': '109', 'Name': 'gaurav', 'Branch': 'me', 'Marks': (77,77,77,77,77)},
#       ]

# print("")
# print("The Top 5 student are as follows :-")
# copy_lst = lst

# topper = copy_lst[0]
# topper_index=0


# for i in range(1,len(copy_lst)):
#     if sum(copy_lst[i]['Marks']) > sum(topper['Marks']):
#         topper = copy_lst[i]
#         topper_index=i
# print("1st Student is",topper)
# copy_lst.pop(topper_index)

# topper = copy_lst[0]
# topper_index=0
    
# for i in range(1,len(copy_lst)):
#     if sum(copy_lst[i]['Marks']) > sum(topper['Marks']):
#         topper = copy_lst[i]
#         topper_index=i
# print("2nd Student is",topper)
# copy_lst.pop(topper_index)

# topper = copy_lst[0]
# topper_index=0

# for i in range(1,len(copy_lst)):
#     if sum(copy_lst[i]['Marks']) > sum(topper['Marks']):
#         topper = copy_lst[i]
#         topper_index=i
# print("3rd Student is",topper)
# copy_lst.pop(topper_index)

# topper = copy_lst[0]
# topper_index=0

# for i in range(1,len(copy_lst)):
#     if sum(copy_lst[i]['Marks']) > sum(topper['Marks']):
#         topper = copy_lst[i]
#         topper_index=i
# print("4th Student is",topper)
# copy_lst.pop(topper_index)

# topper = copy_lst[0]
# topper_index=0

# for i in range(1,len(copy_lst)):
#     if sum(copy_lst[i]['Marks']) > sum(topper['Marks']):
#         topper = copy_lst[i]
#         topper_index=i
# print("5th Student is",topper)
# copy_lst.pop(topper_index)


# PART B - FIND THE TOPPER BRANCH WISE************
# lst=[{'Roll no.': '101', 'Name': 'bantu', 'Branch': 'cs', 'Marks': (66,66,66,66,66)},
#      {'Roll no.': '102', 'Name': 'prakash', 'Branch': 'cs', 'Marks': (44,44,44,44,44)},
#      {'Roll no.': '103', 'Name': 'aadarsh', 'Branch': 'cs', 'Marks': (88,88,88,88,88)},
#      {'Roll no.': '104', 'Name': 'kaber', 'Branch': 'tech', 'Marks': (22,22,22,22,22)},
#      {'Roll no.': '105', 'Name': 'umang', 'Branch': 'tech', 'Marks': (99,99,99,99,99)}, 
#      {'Roll no.': '106', 'Name': 'bholu', 'Branch': 'tech', 'Marks': (55,55,55,55,55)},
#      {'Roll no.': '107', 'Name': 'gopal', 'Branch': 'me', 'Marks': (11,11,11,11,11)},
#      {'Roll no.': '108', 'Name': 'harish', 'Branch': 'me', 'Marks': (33,33,33,33,33)},
#      {'Roll no.': '109', 'Name': 'gaurav', 'Branch': 'me', 'Marks': (77,77,77,77,77)},
#       ]

# print("Topper Branch wise are as follows :-")

# lst_cs=[]
# for item in lst:
#     if item['Branch']=='cs':
#         lst_cs.append(item)

# topper_cs = lst_cs[0]

# for i in range(1,len(lst_cs)):
#     if sum(lst_cs[i]['Marks'])>sum(topper_cs['Marks']):
#         topper_cs = lst_cs[i]
# print("The Topper of CS Branch is:",topper_cs)

# lst_tech=[]
# for item in lst:
#     if item['Branch']=='tech':
#         lst_tech.append(item)
# topper_tech = lst_tech[0]

# for i in range(1,len(lst_tech)):
#     if sum(lst_tech[i]['Marks'])>sum(topper_tech['Marks']):
#         topper_tech = lst_tech[i]
# print("The Topper of TECH Branch is:",topper_tech)

# lst_me=[]
# for item in lst:
#     if item['Branch']=='me':
#         lst_me.append(item)
# topper_me = lst_me[0]

# for i in range(1,len(lst_me)):
#     if sum(lst_me[i]['Marks'])>sum(topper_me['Marks']):
#         topper_me = lst_me[i]
# print("The Topper of ME Branch is:",topper_me)
# print("")