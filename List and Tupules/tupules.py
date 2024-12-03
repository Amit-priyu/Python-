# # tupules- let us to create immutalbe sequence of value
# l1=(1,)
# list=(1,2,3,4,5)
# print(type(list))

# # slicing is also similar 

# #method
# print(list.index(1))
# print(list.count(2))


# 1. take 3 fav movie name from user and store them in list
# s1=input("Enter the first movie :")
# s2=input("Enter the second movie :")
# s3=input("Enter the third movie :")
# movies=[]
# movies.append(s1)
# movies.append(s2)
# movies.append(s3)
# print(movies)

#2.check if the list is palindrome or not, -- use copy method.
# list=[1,2,3,2,1,5]
# list_copy=list.copy()
# list_copy.reverse()
# if(list==list_copy):
#     print("List is palindrome")

#3. no of a grade studen in tupules
# tup=("c","d","a","a","b","b","a")
# count=tup.count("a")
# print(count)

#4. store the above value and sort them from a to d.
tup=["c","d","a","a","b","b","a"]
tup.sort()
print(tup)
