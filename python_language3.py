# *********SWAP FIRST AND LAST ELEMENT OF LIST**********
# def swapElement(list):

#     start, *middle, end = list
#     list = [end, *middle, start]

#     return list

# lst = [1,2,3,4,5]
# print(swapElement(lst))


# **********SWAP GIVEN TWO POSITION IN LIST*********
# def swapElement(list, a, b):
#     list[a-1],list[b-1]=list[b-1],list[a-1]

#     return list

# lst=["One", "Two", "Three", "Four", "Five"]
# print(swapElement(lst, 2, 5))


# **********CHECK ELEMENT IN LIST*********
# lst = [10,20,30,40,50]

# if 11 in lst:
#     print("True")

# else: 
#     print("False")


# **********PRINT SECOND MAXIMUM NUMBER IN LIST**********
# def secondLarge(list):
#     copy_list = list.copy()
#     maximum = max(copy_list)
#     copy_list.remove(maximum)
#     maximum = max(copy_list)
#     return maximum

# lst = [10,20,30,40]
# print(secondLarge(lst))
# print(lst)


# ***********PRINT NEGATIVE ITEM FROM LIST************
# lst = [10,-8,6,9,-6,20,-30]

# for item in lst:
#     if item<0:
#         print(item, end=" ")


# ***********PRINT NEGATIVE ITEM FROM LIST USING FILTER AND LAMBDA************
# lst = [10,-8,6,9,-6,20,-30]
# negative = list(filter(lambda x:(x<0), lst))
# print(*negative)


# ***********PRINT NEGATIVE ITEM WITHIN GIVEN RANGE FROM LIST***********
# lst = [10,-8,6,9,-6,1,5,20,-30]

# for item in lst:
#     if item>=10 and item<=20:
#         if item>=0:
#             print(item, end=" ")


# **********REMOVE EMPTY LIST FROM A LIST*************
# lst = [[],5, [], 6, [], 3, [], [], 9, []]

# for item in lst:
#     while [] in lst:
#             lst.remove(item)
# print(lst)


# ************PRINT UNCOMMAN ITEM FOR LIST1 AND LIST2***************
# lst1 = [ [1, 2], [3, 4], [5, 6] ]
# lst2 = [ [3, 4], [5, 7], [1, 2] ]

# lst3 = []

# for item in lst1:
#     if item not in lst2:
#         lst3.append(item)

# for item in lst2:
#     if item not in lst1:
#         lst3.append(item)


# print(lst3)


# **********CHOICE RANDOM NUMBER FROM LIST OF LISTS***********
# import random

# lst1 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
# lst2=[0, 1, 2]
# data = random.choice(lst2)

# print(random.choice(lst1)[data])


# ********SORT ITEMS IN LIST OF LISTS IN REVERSE ORDER************
# lst1 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

# for item in lst1:
#     item.sort(reverse=True)

# print(lst1)


# ***********NUMBER OF UNIQUE VALUE IN LIST**********
# lst = [1, 2, 2, 5, 8, 4, 4, 8]

# lst = set(lst)
# print(len(lst))


# **********FIND PRODUCT OF UNIQUE VALUE IN LIST************
# lst = [1, 3, 5, 6, 3, 5, 6, 1]

# s = set(lst)

# prod = 1

# for item in s:
#     prod = prod * item

# print(prod)


# **********FIND PRODUCT OF UNIQUE VALUE IN LIST************
# lst = [1, 3, 5, 6, 3, 5, 6, 1]
# lst1 = []

# for item in lst:
#     if item not in lst1:
#         lst1.append(item)

# print(lst1)

# prod = 1

# for item in lst1:
#     prod = prod * item

# print(prod)


#********PRINT UNIQUE VALUE WHICH ARE GREATER THEN K*************
# lst = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6, 1, 2, 5, 9, 0, -8, -10]
# k = 3
# lst1 = []
# for item in lst:
#     if item>=3:
#         lst1.append(item)

# print(list(set(lst1)))


# **********CHECK 3 CONSECUTIVE OCCURENCE OF NUMBER IN LIST***************
# lst = [4, 5, 5, 5, 3, 3, 3, 3, 8, 8, 8, 64, 64, 64]
# lst1 = []
# for item in lst:
#     if lst.count(item)>=3:
#         if lst[lst.index(item)] == item and lst[(lst.index(item)+1)] == item and lst[(lst.index(item)+2)] == item:
#             lst1.append(item)

# print(list(set(lst1)))


# **********COMPARING PAIR IN THE LIST AND PRINTING MAX NUMBER***************
# lst = [1,2,2,3,4,5]

# lst1 = []

# for i in range(len(lst)-1):
#     if lst[i]>lst[i+1]:
#         lst1.append(lst[i])
#     elif lst[i+1]>lst[i]:
#         lst1.append(lst[i+1])
#     elif lst[i+1]==lst[i]:
#         lst1.append(lst[i])
#     else:
#         continue

# print(lst1)


# *************PERMUTATIONS OF 3 NUMBERS************
# from itertools import permutations

# com = permutations([1,2,3], 3)
# count = 0
# for i in com:
#     print(i)
#     count+=1

# print("")
# print(count)


# ***************REMOVE OCUURENCE OF K FROM LIST**************
# def occurence(lst, n):
#     for item in lst:
#         if item[0]==n and item[1]==n:
#             lst.remove(item)
#     print(lst)

# lst = [(4, 5), (5, 6), (1, 3), (5,5), (0,0)]
# k = 5
# occurence(lst,0)
# occurence(lst,5)


# ***********REPLACING LIST WITH ELEMENT OF ANOTHER LIST*************
# lst1 = ["Gfg", "is", "best"]
# lst2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# for i in range(len(lst2)):
#     lst2[i]=lst1[lst2[i]]

# print(lst2)


# 

# data = "4+5*7/2"
# print(data)
# print(data.find('*'))
# data = data[:data.find('*')-1] + "(" + data[data.find('*')-1:]
# data = data[:data.find('*')+2] + ")" + data[data.find('*')+2:]
# print(data)
# data = data[:2] + "(" + data[2:]
# data = data[:data.find('/')+5] + ")" + data[data.find('/')+5:]
# print(data)


#***********************
# data = "4+5*7/2"
# # data = "9+7*9+3+6/8"
# data = list(data)

# ['4', '+', '5', '*', '7', '/', '2']
# print(data)

# for i in range(len(data)):
#     if data[i] == "*":
#         data.insert(data.index('*')-1,'(')
#         data.insert(data.index('*')+2,')')
#         break
# # print(data)
# for i in range(len(data)):
#     if data[i] == "/":
#         n = index = data.index('/')
#         data.insert(index+2,')')
#         while index!=0:
#             if data[index-1] == '(':
#                 data.insert(index-1,'(')
#             index-=1
#         break

# data1=""
# for item in data:
#     data1 = data1 + item
# print(data1)


# ***********INITIALIZE A 5X5 NUMPY ARRAY WITH ONLY ZEROES**********
# import numpy as np

# n1 = np.zeros((5,5))

# print(n1)

# ********FACTORIAL WITH RECURSION*************
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return (n*factorial(n-1))

# print(factorial(5))

#**********CHECK FOR STRING PALINDROME**********
# a = "khokho"

# if a[:]==a[::-1]:
#     print("The string is palindrome -->",a[::-1])
# else:
#     print("The string is not palindrome-->",a[::-1])


# ***********REVERSE EVERY WORD IN STRING**********
# st =" geeks quiz practice code"
# st=st.split(" ")
# print(st)

# for i in range(len(st)):
#     st[i] = st[i][::-1]

# print(st)

# st1=""

# for i in range(len(st)):
#     st1=st1+ " " +st[i]

# print(st1)


# **********REVERSE WORDS IN STRING**************
# st ="my name is laxmi"

# st = st.split(" ")

# print(st)
# print("")

# for i in range(len(st)//2):
#     st[i],st[len(st)-i-1]=st[len(st)-i-1],st[i]

# print(st)
# print("")

# st1=""

# for i in range(len(st)):
#     st1 = st1 + " " + st[i]

# print(st1)


# *************LENGTH OF STRING WITHOUT SPACES**********
# st ="my name is laxmi raj"
# print("The total length of string is",len(st))

# count=0

# for i in range(len(st)):
#     if st[i]!=" ":
#         count+=1

# print("The length of string without spaces is",count)


# ********OUTPUT ONLY HAS WORDS WHICH HAS EVEN NUMBER OF CHARACTER************
# s = "i am laxmi rani"

# s = s.split(" ")

# print(s)
# s1 = ""

# for i in range(len(s)):
#     n = len(s[i])
#     if n%2==0:
#         if len(s1)==0:
#             s1 = s[i]
#         else:
#             s1 = s1 + " " + s[i]

# print(s1)


# ******MAKE ANOTHER HALF OF STRING AS UPPER**********
# s ='geeksforgeek'

# start = (len(s)//2)
# end = len(s)

# s1 = s[0:start]
# s2 = s[start:end]
# s2 = s2.upper()

# print(s1+s2)


# **************CAPITALIZE FIRST AND LAST CHARACTER OF WORDS IN A STRING*****************
# s = 'welcome to geeksforgeeks'

# s = s.split(" ")

# t = []

# for item in s:
#     x = item[0].upper() + item[1:-1] + item[-1].upper()
#     t.append(x)

# t = " ".join(t)

# print(t)


# *********CHECK WHEATHER STRING HAS ALPHA OR NUMERIC OR BOTH*********
# s = 'ujfeiuhefiufe594'

# num = False
# alpha = False

# for i in range(len(s)):
#     if s[i].isalpha()==True:
#         alpha = True
#     elif s[i].isnumeric():
#         num = True

# if num==True and alpha==True:
#     print("The string has both alphabets and numerics")
# elif num==True and alpha==False:
#     print("The string has only numerics")
# elif num==False and alpha==True:
#     print("The string has only alphabets")

# ************CHECK IF STRING HAS ALL THE VOWELS IN IT**************
# s = 'ABeeIghiObhkUul'
# s = s.lower()
# t = []
# for i in range(len(s)):
#     if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
#         t.append(s[i])

# if 'a' in t and 'e' in t and 'i' in t and 'o' in t and 'u' in t:
#     print("The string has all vowels")
# else:
#     print("The string does not have all vowels")


# *************BASIC PATTERN PRINTING**************
# for row in range(1,6):
#     for col in range(1,6):
#         print('*',end='')
#     print('')


# *****************THIS PROGRAM WILL CALCULATE THE MATCHING NUMBER FROM TWO STRINGS*******************
# str1 = 'aabcddekll12@'
# str2 = 'bb22ll@55k'
# str1 = 'abchytjkl'
# str2 = 'anvditopld'
# str3 = ""

# if len(str1) > len(str2):
#     for i in range(len(str1)):
#         for j in range(len(str2)):
#             if str2[j]==str1[i]:
#                 str3 = str3 + str1[i]
# else:
#     for i in range(len(str2)):
#         for j in range(len(str1)):
#             if str2[i]==str1[j]:
#                 str3 = str3 + str1[i]

# print(set(str3))
# print(len(set(str3)))


# ***********COUNT VOWEL IN STRING*************
# def count_vowel(str1):
#     str1 = str1.lower()
#     set1 = {'a','e','i','o','u'}
#     count = 0

#     for i in range(len(str1)):
#         if str1[i] in set1:
#             count+=1

#     return count

# str1 = 'Hello World'
# a = count_vowel(str1)
# print(a)


# *************REMOVE DUPLICATES FROM STRING*************
# str1 = 'geeksforgeeks'

# lst = list(set(list(str1)))
# str2 = ''.join(lst)

# print(str2)


# ***********FIND MINIMUM FREQUENCY ELEMENT IN STRING************
# str1 = 'geeksofrgeeksggg'

# dict = {}

# for item in str1:
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict[item] = 1

# print(dict)
# fr = min(dict, key = dict.get)
# print(fr)


# ****************FIND MAXIMUM FREQUENCY ELEMENT IN STRING************
# str1 = 'geeksofrgeeksggg'

# dict = {}

# for item in str1:
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict[item] = 1

# print(dict)
# fr = max(dict, key = dict.get)
# print(fr)


# **********SIZE OF TUPLE*********
"""
from sys import getsizeof

tup = (2,6,9,8,7,6,10)

print(getsizeof(tup))
"""


# ********FIND MIN AND MAX IN TUPLE*************
"""
tup = (2,6,9,8,7,6,10)

print("Minimum value in tuple is",tup[0])
print("Maximum value in tuple is",tup[-1])
"""

"""
tup = (2,6,9,8,7,6,10)
print(min(tup))
print(max(tup))
"""


# **********FROM GIVEN LIST MAKE A LIST OF TUPLE HAVING A ITEM FROM EARLIER LIST AND ITS CUBE***********
"""
list = [1, 2, 3]
list1 = []

for item in list:
    tup = (item, item**3)
    list1.append(tup)

print(list1)
"""


# *********STAR SPATTERN***********
"""
num = int(input("Enter the number: "))
for row in range(1, num+1):
    for col in range(1, row+1):
        print('*', end="")
    print('')
"""

# **********STAR PATTERN**********
"""
num = int(input("Enter the number: "))
for row in range(num, 0, -1):
    for col in range(1, row+1):
        print('*', end="")
    print('')
"""


# ***********STAR PATTERN***********
"""
num = int(input("Enter the number: "))
num = num * 2
for row in range(1, num+1):
    if row%2!=0:
        for col in range(1, row+1):
            print('*', end="")
        print('')
"""


# ***********STAR PATTERN**********
"""
num = int(input("Enter number: "))
for row in range(1,num+1):
    for col in range(1,num-row+1):
        print(" ", end="")
    for col in range(1,row+1):
        print(row, end=" ")
    print("")
"""


# *******COUNT CHARACTER IN STRING************
"""
tst = "geeksforgeeks is best for geeks"
chr = ['e','b', 'g', 'f'] 
dict = {}

for i in tst:
    if i in chr:
        cout = tst.count(i)
        dict[i]=cout

print(dict)
"""


# **********COUNT NUMBERS FROM STRING***********
"""
st = "geeks4feeks is No. 1 4 geeks"
num = ['1','2','3','4','5','6','7','8','9']
count = 0

for i in st:
    if i in num:
        count+=1

print(count)
"""


# *********CHECK FOR SPECIAL CHARACTER IN STRING***********
"""
st = "Geeks$For$Geeks"
li = '[@_!#$%^&*()<>?/\|}{~:]'
bol = True

for i in st:
    if i in li:
        bol = False
        break

if bol:
    print("String accepted !!")
else:
    print("String not accepted !!")
"""


# *******GENERATE RANDOM NUMBER TILL IT MATCHES WITH ORIGINAL NUMBER**********
"""
import random

num = int(input("Enter any number between 0 to 1000: "))
i = 0

while True:
    a = random.randint(0,1000)

    if a==num:
        print("The number generated after",i, "iteration")
        break
    else:
        i+=1
"""


# *********PRINT WORDS GREATER THAN 'K' LENGTH**********
"""
st = "string is fun in python" 
k = 3
li = st.split()
st1 = ""

for i in li:
    if len(i)>k:
        st1 = st1 + " " + i

print(st1)
"""