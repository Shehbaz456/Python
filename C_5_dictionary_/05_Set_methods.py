# Creating an Empty set
a = set()
print(type(a))

# Adding values oto an empty set
a.add(4)
a.add(5)
a.add(5)
a.add(5)
a.add(5)
a.add((4,55,65)) #you can use tuple
# a.add([4,55,65]) #throw Error you can't use list for listing element in set  
# a.add({4:5}) #throw Error you can't use dictionary for listing element in set  
print(a)

# print(len(a)) #length of set elements
# a.remove(5)
# print(a)

print(a.pop())
print(a)
# S.clear()   #Empties the set S

#s.union({5,6}) #return a new set with all items from sets => {1,3,4,3,5,6}
#s.intersection({8,11}) #comman in both set


