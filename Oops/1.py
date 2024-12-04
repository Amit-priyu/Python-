# oops in python..
# to map real world scenario

# object and class
# class it is a blueprint for creating an object.
# Methods are functions that belong to objects.

# class Car:
#     color="Blue"
#     model="mercedes"
# class student:
#     # constructor default
#     def __init__(self):
#         pass
#     # parametrise constructor.
#     college_name="Nit Trichy"
#     name="anonymous"  # class attribute.
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#         print("Adding new student in Database")
#     def hello(self):
#         print("Welcome student",self.name)
#     def get_marks(self):
#         return self.marks
    
# s1=student("amit priyadarshi",90)
# print(s1.college_name)
# s1.hello()
# print(s1.get_marks())


# s2=student("rinka yadav",98)
# print(s2.name)
# print(s2.marks)
# c1=Car()
# print(c1.color)
# print(c1.model)


# consturutor---  __init__ function 
# all classes have a func called __init__() which is always executed
#  when class is being initiated.


class student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getavg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"Hi",self.name , "your avg score is",sum/3)
        
s1=student("amit Priyadarshi",[100,98,78])
print(s1.name)
print(s1.getavg())