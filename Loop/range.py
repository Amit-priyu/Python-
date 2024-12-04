# range function return a sequence of number , starting from 0 bydefault
#   and increment by 1(by default) and stop before a special number.

# range(start?, stop, step?)

# for el in range(5): #(stop)
#     print(el)
# for el in range(1,5,2):
#     print(el)
# for el in range (10,40,10): #( start stop,step)
#     print(el)



# pass statement: null statement, that does nothing.
# it is used as a placeholder for the future code.
# for i in range(5):
#     pass
# print("welcome Amit Priyadarshi")





# 1. sum of first n nos. 
# n=int(input("Enter the value of n: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum is:", sum)

#factorial using for loop.
n=int(input("Enter the value of n: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"Factorial of {n} is {fact}")