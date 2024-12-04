# func- block of statement that perform the specific tasks.
# to remove the redundant code...

# def cal_sum(a,b):
#     return a+b
# print(cal_sum(5,6))

# def prin():
#     print("Hello, hi there")
# prin()


# avg of 3 no.
# def avg(a,b,c):
#     return (a+b+c)/3
# print(int(avg(10,20,49)))


#default parameters.(last me hone chaiye default arguments.)
def mul(a,b=10):
    return a*b
print(mul(10))


citi=["delhi","noida","hbd","patna"]
def length(citi):
    print(len(citi))
length(citi)

# print in the same lint
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(citi)


def fact(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
n=int(input("Enter the value of n: "))
# print(fact(n))


def convert(usd_val):
    inr_val=usd_val*83
    print(f"USD {usd_val} in indian rupees is {inr_val} INR")
convert(2)