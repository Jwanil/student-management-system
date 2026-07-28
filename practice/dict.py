mydict = {
    "name" : "Jwanil",
    "age" : 21,
    "gender" : "Male",
    "hobbies" : ["reading", "coding", "gaming"],
    "address" : {
        "city" : "Surat",
        "state" : "Gujarat"
    }
}


#Ordered
#Changable
#No duplicate values

print(mydict)
print(type(mydict))
print(len(mydict))


x = mydict["age"]
print(x)
x = mydict.get("age")
print(x)

x = mydict.keys()
print(x)

x = mydict.values()
print(x)

x = mydict.items()
print(x)

#Change value
mydict["age"] = 22
print(mydict)

mydict.update({"name": "Jwanil Modi"})

#add
mydict["college"] = "PDPU"
print(mydict)

mydict.update({"email": "jwanilmodi10@gmail.com"})


#delete
del mydict["gender"]
print(mydict)

mydict.pop("email")
print(mydict)

#looping

for x in mydict:
    print(mydict[x])

for x in mydict.items(): #also works with values() and keys()
    print(x)

for x in mydict:
    if x == "hobbies":
        for y in mydict[x]:
            print(y)


    
#copy
copydict = dict(mydict)
print(mydict)

#nested dictionary
print (mydict["address"]["city"])
#looping in 

for x, y in mydict.items():
    print(x)
    if isinstance(y, dict):
        for i in y:
            print(i + ':', y[i])
    else:
        print(y)
