# age=21
# if(age>=18):
#     print("You can vote and applied for the licence")
# else:
#     print("You can't vote and can't apply for the licence")


# light="green"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# else:
#     print("Look")
# print("end")



a=int(input("Enter the Number"))
b=int(input("Enter the Number"))
c=int(input("Enter the Number"))

if(a>=b and a>=c):
    print("first no is largest",a)
elif(b>=c):
    print("second is largest",b)
else:
    print("third is largest",c)
    
if(a%2==0):
    print("even")
else:
    print("odd")