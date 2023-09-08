# dictionary - unodrered seq
# key:value pair
# key should be unique, value can be duplicates

# d1={} # initialze empty dict
# d2=dict()
#
# print(d1)
# print(d2)
#
# d1={1:"one", 2:"second", 3:"third"}
#
# print(d1[1])
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.clear() # returns empty
# print(d1)
# del d1
# print(d1) ---throws error

d1 = {"name": "sita", "age": 20, "education": "bsc"}
d2 = {1: "one", 2: "second", 3: "third"}
# print(d1)
# # add/updating the dict
# d1["college"]="sathyabama"
# print(d1)
# d1.update({"phone no": "9000000123"})
# print(d1)
#
# d1.pop("phone no")
# print(d1)
# d3=d1.copy()
# print(d3)
# # combine
# d1.update(d2)
# print(d1)
# formkeys
# d4={}
# d2.fromkeys([1,2,3,4])
# print(d2)

# list1 = [1, 2, 3, (10, 20, 30)]
# #list1[3][2]=60 # throws error
# #print(list1[3][2])
#
# tuple1 = (1, 2, 3, [10, 20, 30])
# ##tuple1[3]=(10, 20, 30)  --- Throws error
# tuple1[3][2] = 60
# print(tuple1)
#
#
# d1 = {"name": "sita", "age": 20, "education": "bsc", "key":{1: "one", 2: "second", 3: "third"}}
# print(d1["key"][1])

# set= unordered list
# eliminates duplicates
# set1={3,1,2,3,4}
# print(type(set1))
# print(set1) # removes duplicates
# set1.update("5")
# print(set1)
# for i in set1:
#     print(i)
#
# # if condition
#
# if 3>5:
#     print("3 is greater than 5")
# else:
#     print("3 is not greater than 5")

# leap year

year = 2001
if year % 4 == 0:
    print("leap year")
#elif year % 4 != 0:
else:
    print("not leap year")
