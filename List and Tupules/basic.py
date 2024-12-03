# list --- mutuable---which can be changed
# string-- immutable- can't be changed.
# marks=[10,20,40,50,70]
# print(marks)
# print(type(marks))
# print(marks[0])

# student=["amit",21,95.45,"Bihar"]
# print(student)

# slicing is also applicable in list with same rule 

# Methods in the list.
# append- add one element in the end


#list=[1,3,2]
list=["banana","litchi","Apple"]
# list.append(4)
print(list)

# sort method
print(list.sort()) # ascending order
print(list)
print(list.sort(reverse=True))
print(list)
 
 
# reverse--- it will do in the original 
print(list.reverse())
print(list)
list.insert(2,5)
print(list)
list.remove(2)  # remove the first occ of remove
list.pop() 
