# # dic- used to store data value in key value pair.
# # unordered, mutuable(changable), don't allow dublicate key value pairs.
# null_dict={
    
# }
# info={
#     "key":"value",
#     "name":"amit",
#     "subject":["python","c++","Java"],
#     "age": 21,
#     "marks":95
# }
# print(type(info))
# info["name"]="amit Priyadarshi"
# print(info["subject"])
# print(info["name"])

# #nested dict
# stud={
#     "name":["Amit","rinka"],
#     "subject":{
#         "phy":80,
#         "chem":90,
#         "math":100
#     },
#     "Age":21,
#     "ispassed":True
# }
# print(stud["subject"])
# print(stud["subject"]["phy"])


# METHODS IN DICTIONARY
stud={
    "name":["Amit","rinka"],
    "subject":{
        "phy":80,
        "chem":90,
        "math":100
    },
    "Age":21,
    "ispassed":True
}
# print(stud.keys())
# print(stud.values())
print(list(stud.items()))
print(stud.get("name"))
stud.update({"city":"Delhi"})
print(stud)