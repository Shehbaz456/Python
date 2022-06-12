from cmath import log


age = int(input("Enter your Age: "))
if(age==40):
    print("you can make children ");
elif(age>18 and age<60):
    print("you can drive ");
    print("you can drink ");
else:
    print("you Can do new things ");
print("Done")
