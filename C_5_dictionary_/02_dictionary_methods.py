from turtle import update


mydict ={
    "Fast" : "in a quick manner",
    "Harry" : "A Coder",
    "Marks": [1,2,4],
    "anotherdict": {'Shehbaz': 'player'},
    1:2
}

# dictionary methods
# print(mydict.keys())           #print the keys of the dictionary 
# print(list(mydict.keys()))     #print the keys in list form of the dictionary  
# print(list(mydict.values()))     #print the values in list form of the dictionary  
# print(mydict.values())     #print the values of the dictionary  
print(mydict.items())     #print the items(key,values) for all contents like tuple of the dictionary  
print(mydict)
                               #timestamp 3:40:00
updatedict ={
    "lovish": "friend"
}
mydict.update(updatedict) #updates the dictionary by adding key value pair from updatedict
print(mydict)


print(mydict.get("Harry2")) #print value associated with key "Harry"
print(mydict["Harry2"]) #print value associated with key "Harry"

print(mydict.get("Harry2")) #returns none as Harry2 is not persent in the dictionary
print(mydict["Harry2"]) #throws an error Harry2 is not persent in the dictionary

