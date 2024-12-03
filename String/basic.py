str1="This is an apple."
str2="Amit Priyadarshi"
# print(str1)
#concatenation.
print(str1+str2)


#length of string.
print(len(str1))

# indexing..in the string. staring with 0 
str="Amit Priyadarshi"
ch=str[2]
print(ch)

# Slicing..str[start_index: end_index]--ending index is not included.
print(str[0:4])
print(str[:4])
print(str[5:len(str)])
# negative indexing.
print(str[-5:-1])

# string function.
st="i am studying in nit trichy"
print(st.endswith("chy"))

print(st.capitalize()) # not do changes in the string.
print(st)

# replace function.
print(st.replace("a","Y"))
print(st.replace("studying","Learning"))

print(st.find("m"))  # give the first index.
print(st.count("m"))  # give the total no of count..