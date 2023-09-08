# print(a)---> Nameerror
# a=1+"shirly"---TypeError

# to check all eceptions in python
# import builtins
# print(dir(builtins))

# try...catch
# try:
#     #print(a)
#     a = 1 + "shirly"
# except Exception as msg:
#     print("WARNING Some error happend in try block")
#     print(msg)

# try:
#     #print(a)
#     a = 1 + "shirly"
# except (NameError,TypeError) as msg:
#     print("WARNING Some error happend in try block")
#     print(msg)

# try:
#     a=1/0
#     print(a)
# except Exception as var: # error happen in try
#     print("WARNING Some error happend in try block")
#     print(var)
# else: # no error in try block
#     print("try block executed sucessfully")
# finally:
#     print("reached finally block")

import pickle
pooja={"Name": "pooja", "age":"15", "education":"10"}
sita={"Name": "sita", "age":"17", "education":"12"}
person1={"Name": "", "age":"17", "education":"12"}
person2={"Name": "", "age":"17", "education":"12"}

db={"student1":pooja, "student2": sita, "student3": person1, "student4":person2}
with open("error_db.txt", "wb") as writer:
    pickle.dump(db, writer)# convert to byte codes

with open("error_db.txt", "rb") as writer:
    data= pickle.load(writer) # convert bytes to human readable form
    print(data)
    try:
        for key, val in data.items():
            #print(key)
            # if val["Name"] == "":
            #     raise Exception(f"No Name key for dict {key}: {val}")
            assert val["Name"] == "", f"No Name key for dict {key}: {val}" # Assertion error
    except AssertionError as msg:
        print("some error happen", msg)
"""else: print the name of that student 
    finally: delete the file"""



