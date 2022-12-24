# timestamp 7:30:00
# Q1

# f = open('poem.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is Not present")
# f.close()



# def game():
#     return 6443

# score = game()
# with open("hiscore.txt") as f:
#     hiscoreStr = f.read()

# if hiscoreStr =='':
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))

# if int(hiscoreStr)<score:
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))



# for i in range(2,21):
#     with open(f"tables{i}",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}x{j} = {i*j}\n")
#     break

# timestamp 7:44:00
#        Q = 4

# with open("hell.txt") as f:
#     content = f.read()

# content = content.replace("donkey","%$%@$^#")

# with open("hell.txt","w") as f:
#     content = f.write(content)  


# Q 5
 
# words = ["donkey","kaddu","mote"]
# with open("hell.txt") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word,"%$%@$^#")

#     with open("hell.txt","w") as f:
#         f.write(content)  
# python

# # Q 6

# with open("log_file.txt") as f:
#     content = f.read()
# if "python" in content:
#     print("yes python is present ")
# else:
#     print("No python is present ")


# Q 7

# content = True
# i=1
# with open("log_file.txt") as f:
#     while content:
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print("yes python is present ")
#             print(i)
#         i+=1

# implemention 
# content = True
# i =1
# with open("like_log.txt") as f:
#     while content:
#         content = f.readline()
#         if '3307' in content.lower():
#             print(f"password is present on line number {i} ")
#         i+=1

# Q 8 copy to file

# with open("hello.txt") as f:
#      text = f.read()
#      print(text)
# with open("same_hello.txt","w")as f:
#     f.write(text)
    
# Q 9 file are identical or not

# file1 = "hello.txt"
# file2 = "same_hello.txt"

# with open(file1) as f:
#     f1 = f.read()
# with open(file2) as f:
#     f2 = f.read()
# if f1==f2:
#     print("files are identical")
# else:
#     print("files are not identical")

# Q10 wipe out all content (erase all content)

# with open("same_hello.txt",'w') as f:
#     f.write(" ")


# Q11 rename file  
import os
oldname = "dell_info.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()
with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)

  

    


    