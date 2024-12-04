# python is used to perform operation on a file
# types of file: text files and binary files.
f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))


f.close()