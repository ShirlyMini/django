# function as parameter
# function as ref
# function as return statement

def hello():
    print("python world")

# hello()
# var1=hello # fun Ref
# print(var1)
# var2=hello # fun Ref
# print(var2)
# var1()
# var2()

# def func1():
#     print("inside func 1 ")
#
# def func2(func):
#     func()
#     print("inside func 2 ")
#
# func2(func1)

# def func1():
#     return "Hello "
#
# def welcome():
#     return "Welcome "
#
# def func2(ref_var):
#     str1 = ref_var()
#     print(str1 + "python !!!")
#
# func2(func1)
# func2(welcome)

# nested function
# def outerfunction():
#     msg1="python"
#     def innerfunction(msg2):
#         #msg2 = "world"
#         str1 = msg1 + msg2
#         return str1.upper()
#     return innerfunction
#
# ref_innerfunc=outerfunction()
# print(ref_innerfunc("world"))


