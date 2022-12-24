

from ast import For
import re
from sqlite3 import Timestamp


# def maximum(num1,num2,num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m= maximum(3,5,134)
# print("the value of the maximum is " + str(m))



# **************************************************
# Q WAP using function to convert celsius to Fahrenheit.

# (30°C x 1.8) + 32 = F
#  c   = f - 32 / 1.8

# def temp_conversion(celsius):
#     F = (celsius * 1.8) + 32
#     return F


# # celsius = input("Enter temp celsius to convert fahrenheit")
# Fahrenheit =temp_conversion(34)

# print("temprature in fahrenheit "+str(Fahrenheit))





# *****************************************************
# WAP to prevent new line in print function

# note end=" " use for skiping new line character
# print("how" , end=" ")
# print("are" , end=" ")
# print("you" , end=" ")
# print("I am Good" , end=" ")


# ******************************************************
# sum =0
# def Sum_of_n_natural_num(n):
#     for num in range(0, n+1, 1):
#     # for(i=n;i>=0;i--)
#         sum = sum+num
#     return sum

# f = Sum_of_n_natural_num(5)
# print("output " + str(f))



# n = input("Enter Number to calculate sum")
# n = int (n)
# sum = 0
# for num in range(0, n+1, 1):
#     sum = sum+num
# print("SUM of first ", n, "numbers is: ", sum )



# **********************************************
# Timestamp 6:46:10

# Q WAP to print pattern
# * * *         
# * *
# *

n=3
# for i in range(n):
#         print(" *" *(n-i))
    
 
this = "        Shehbaz khan cool       "
print(this)
print(this.strip())
#  strip function use for skiping space 





