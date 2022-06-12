
print("hello");
i = int(input("Enter table number to print table "))
for i in range(i,10*i+1,i):
    print(i)


# print("hello");
num = int(input("Enter table number to print table "))
i=10
for i in range(1,11):
    print(f"{num}X{i}={num*i}")
    

#Q2
l1 = ["harry","Shehbaz","Sonu","Sachin","Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)

#Q3
print("hello");
num = int(input("Enter table number to print table "))
i=1
while (i<=10):
    print(f"{num}X{i}={num*i}")
    i+=1


# Q4

from sys import flags


num=int(input("Enter your number: "))

for x in range(2,num):
    if(num%x==0 and num!=2):
        flags =False
        break
    else:
        flags =True

if flags:
    print("A Prime number: ",num)
else:
    print("Not A Prime number: ",num)


# Q5
num=int(input("Enter your number: "))
sum=0
i=1
while (num>=i):
    print(i)
    sum = sum+i
    i+=1
print(sum)


# Q6
   # 5! = 5 x 4 x 3 x 2 x 1
num=int(input("Enter your number: "))
p=num
factorial= 1
print(f"like this 5! = 5 x 4 x 3 x 2 x 1 ")
for x in range(num):
        factorial = factorial*num
        num-=1
print(f"factorial of given {p} is: {factorial}")
       

