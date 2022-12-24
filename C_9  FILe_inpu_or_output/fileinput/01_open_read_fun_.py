# Timestamp 7:7:00

# use open function to read the content of a file!

f = open('hello.txt','r')
f = open('hello.txt') #BY default mode is r 
data = f.read()
print(data)
f.close()


#  we can specifi the data you want to read
data = f.read(4)  #first 4 character 
print(data)
f.close()