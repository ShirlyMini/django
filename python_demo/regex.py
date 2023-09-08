import re
# password validator
# atleast one upper case
# atleast one lower case
# atleast one number
# atleast one special char @#$%^&*

# pat=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*]).{8,20}$")
# print(pat.search("passwordfesd"))
# print(pat.search("July@2023"))
# print(pat.match("July@2023"))
# print(pat.fullmatch("July@2023"))


# str1="this is regular expression !!!"
# str2="as"
# pat = re.compile("[a-z]{1,2}")
# #print(pat.search(str1))
# print(pat.match(str1))
# print(pat.fullmatch(str1))
# print(pat.match(str1))
# print(pat.fullmatch(str1))

# print(re.match("[a-z]{1,2}", "this is regular expression !!!"))
# print(re.findall("^[a-z]{0,4}", "this is regular expression !!!"))
# print(re.findall("\w+", "this is regular expression !!!"))
# print(re.split("\s", "this is regular expression !!!"))
# print(re.split("regular", "this is regular expression !!!"))
# m = re.match("\w+ \w+", "this is regular expression !!!")
# print(m.group(0))

# lst = ["9090909090", "8080808080", "7070707070", "234567890"]
#
# for num in lst:
#     var = re.match("^[9876][0-9]{9}$", num)
#     # if var is not None:
#     #     print(var.group(0))
#
#     try:
#         print(var.group(0))
#     except:
#         print("invalid number")

str2="""This code uses a function that checks if a given password satisfies certain conditions. It uses a single for loop to iterate through the characters in the password string, and checks if the password contains at least one digit, one uppercase letter, one lowercase letter, and one special symbol from a predefined list and based on ascii values. It sets a boolean variable “val” to True if all these conditions are satisfied, and returns “val” at the end of the function."""
lst = re.findall("\w+", str2)
#lst = re.findall(".*", str2) # wildcard
print(lst)
for word in lst:
    if len(word) == 3:
        print(word)