mylist = [1, 2, 3, "Jwanil", 0.45, "ok", False]


#Ordered
#Changable
#Allow duplicate values

print(mylist)

print(len(mylist))#List Length

print(type(mylist))

print(mylist[0])#Access List
print(mylist[-1])#reverse indexing
#slicing
print(mylist[1:3])
print(mylist[:3])
print(mylist[1:])
print(mylist[-4:-1])
#checking in list
if "Jwanil" in mylist:
    print("Yes")


mylist[1] = 5
print(mylist)

mylist[1:3] = [4, 6]
print(mylist)

#inserting
mylist.insert(4, "python")
print(mylist)

#append
mylist.append("bye")
print(mylist)

#extend (can be done with tuples too)
mylist.extend(["super", 7])
print(mylist)

#remove
mylist.remove("python")
print(mylist)

#pop
mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)

#delete
del mylist[2]
print(mylist)

#clear
# mylist.clear()
# print(mylist)

#looping

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

i = 0
while i < len(mylist):
    print(mylist[i])
    i+= 1

#list comprehension
#newlist = [expression for item in iterable if condition == True]
[print(x) for x in mylist]


#sorting
sortlist = [4,7,2,9,3,6]
sortlist.sort()
print(sortlist)

sortlist.reverse()
print(sortlist)

#copy
thislist = mylist.copy()
print(thislist)

#list
thislist2 = list(mylist)
print(thislist2)

#join
thislist3 = [1,2]
thislist4 = [3,4]
thislist5 = thislist3 + thislist4
print(thislist5)
