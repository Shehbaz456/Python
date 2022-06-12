
from audioop import avg
from cgitb import text
from itertools import count
from lib2to3.pgen2.token import LESS
from operator import truediv
from xml.dom.pulldom import CHARACTERS
# Q1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter Second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# if(num1>num2):
#     f1 = num1
# else:
#     f1 = num2

# if(num3>num4):
#     f2 = num3
# else:
#     f2 = num4

# if(f1>f2):
#     # print("greaterst number is:  ",f1)
#     print(str(f1) + " is greatest number  ")
# else:
#     # print(" greaterst number is:  ",f2)
#     print(str(f2) + " is greatest number  ")


# Q2
# mark1 = int(input("Enter first marks: "))
# mark2 = int(input("Enter Second marks: "))
# mark3 = int(input("Enter third marks: "))

# total_marks = (mark1+mark2+mark3)
# Avg_marks = total_marks/3
# print("your Percentage is: ",Avg_marks)

# if( Avg_marks <40 and mark1<33 or mark2< 33 or mark3< 33):
#     print("You are fail ");
# else:
#     print(" Congatulations!  You are Pass ");


# Q4
# text = input("Enter your text: ")
# if("make a lot of money" in text):
#     spam = True
# elif("Buy now " in text):
#     spam = True
# elif("Subscribe this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam=False
# if(spam):
#     print("This is Spam Mail")
# else:
#     print("NOT a Spam Mail")

# Q4
# text = input("Enter your text: ")
# if(len(text)<10):
#     print("LESS than 10 CHARACTERS")
# else:
#     print("NOT LESS than 10 CHARACTERS")

# Q5
# names =["harry","Shehbaz","Sona","Shah rukh khan","katrina kaif","sonu"]
# name = input("Enter the name to check \n")

# if name in names:
#     print("your name is present in list")
# else:
#     print("your name is Not present in list")

# Q6
marks =int( input("Enter your marks: "));
 
if(marks>90):
    grade = "Ex"
elif(marks>80 and marks<=90):
    grade = "A"
elif(marks>70 and marks<=80):
    grade = "B"
elif(marks>60 and marks<=70):
    grade = "C"
elif(marks>50 and marks<=60):
    grade = "D"
elif(marks<50):
    grade = "F"

print("your grade is ", grade)

