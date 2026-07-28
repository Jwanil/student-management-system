mytuple = (1, 2, 3, "Jwanil", 0.45, "ok", False)


#Ordered
#Unchangable
#Allow duplicate values

print(mytuple)

print(len(mytuple))#List Length

print(type(mytuple))

print(mytuple[0])#Access List
print(mytuple[-1])#reverse indexing
#slicing
print(mytuple[1:3])
print(mytuple[:3])
print(mytuple[1:])
print(mytuple[-4:-1])
#checking in list
if "Jwanil" in mytuple:
    print("Yes")


tuple2list = list(mytuple)
#convert tuple to list to make changes in tuple as tuple cannot be directly changes

tuple2list[1] = 5
mytuple = tuple(tuple2list)
print(mytuple)

tuple2list[1:3] = [4, 6]
mytuple = tuple(tuple2list)
print(mytuple)

#inserting
tuple2list.insert(4, "python")
mytuple = tuple(tuple2list)
print(mytuple)

#append
tuple2list.append("bye")
mytuple = tuple(tuple2list)
print(mytuple)

#extend (can be done with tuples too)
tuple2list.extend(["super", 7])
mytuple = tuple(tuple2list)
print(mytuple)

#remove
tuple2list.remove("ok")
mytuple = tuple(tuple2list)
print(mytuple)

#delete
temptuple = (1, 2, 3)
print(temptuple)
del temptuple
# print(mytuple) # ERROR

#clear
# mytuple.clear() # ERROR
# print(mytuple)

#Tuple unpacking

(one, two, three, four, five, six, seven) = mytuple
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)

# * used to store remaining items in a list
(one, two, three, *rest) = mytuple
print(one)
print(two)
print(three)
print(rest)

(one, *inbetween, last) = mytuple
print(one)
print(inbetween)
print(last)


#looping

for x in mytuple:
    print(x)

for i in range(len(mytuple)):
    print(mytuple[i])

i = 0
while i < len(mytuple):
    print(mytuple[i])
    i+= 1

#list comprehension
#newlist = [expression for item in iterable if condition == True]
[print(x) for x in mytuple]


#sorting
sortlist = [4,7,2,9,3,6]
sortlist.sort()
print(sortlist)

sortlist.reverse()
print(sortlist)


#list
thistuple2 = list(mytuple)
print(thistuple2)

#join
thistuple3 = (1,2)
thistuple4 = (3,4)
thistuple5 = thistuple3 + thistuple4
print(thistuple5)

#multiply
numtuple = (1,2,3)
print(numtuple * 2)

