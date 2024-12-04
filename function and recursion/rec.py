# recursion: when a function called itself.
# n-1

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
def show(n):
    if(n==0):  # Base Case.
        return
    print(n,end=" ")
    show(n-1)   # recursion 
    
# 1. first of n natural no.
def sum_n(n):
    if(n==0):
        return
    return sum_n(n-1)+n

n=int(input("Enter the Value of n: "))  
show(n)
print(factorial(n))
print(sum_n(n))


