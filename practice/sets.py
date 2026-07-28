myset = {"Jwanil", 22, 0.45, True}

print(myset)
print(type(myset))
print(len(myset))

#sets are unordered
#sets are unchangable
#sets do not allow duplicate values

#print 
for x in myset:
    print(x)

print("Jwanil" in myset)
print("Hello" not in myset)

#add items
myset.add("Hello")
print(myset)


newset = {1, 2, 3} #also works with tuple, lists and dictionary
myset.update(newset) 
print(myset)

#remove
myset.remove("Jwanil")
print(myset)

myset.discard("Jwanil")# it will not give any error if item is not present
print(myset)

myset.pop() #remove random item
print(myset)

newset.clear() #remove all items
print(newset)

#looping
for x in myset:
    print(x)

#union
setA = {1, 2}
setB = {2, 3}
setC = setA.union(setB)
print(setC)

setC = setA | setB
print(setC)

setA.update(setB)
print(setA)

setD = setA.intersection(setB) #or & operator
print(setD)

setE = setA.difference(setB) #or - operator
print(setE)

