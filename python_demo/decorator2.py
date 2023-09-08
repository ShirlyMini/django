# def printer():
#     print("hello python!!")
#
# def display_info(func):
#     def inner():
#         print("executing ", func.__name__, "function")
#         func()
#         print("finished execution")
#     return inner
#
# inner_ref = display_info(printer)
# inner_ref()

###############################################3
# def display_info(func):
#     def inner():
#         print("executing ", func.__name__, "function")
#         func()
#         print("finished execution")
#     return inner
#
# @display_info
# def printer():
#     print("hello python!!")
#
# @display_info
# def printer2():
#     print("welcome python!!")
#
# printer()
# printer2()

##################################################

# division

# def divide(a,b):
#     return a/b
#
# def dec_division(func):
#     def inner(a, b):
#         print(f"Dividing {a} by {b} function")
#         if b!=0:
#             return func(a, b)
#         else:
#             print("cannot divide by 0!!")
#             return
#     return inner
#
# inner_ref = dec_division(divide)
# print(inner_ref(15,3))

###############################################333

# def dec_division(func):
#     def inner(a, b):
#         print(f"Dividing {a} by {b} function")
#         if b!=0:
#             return func(a, b)
#         else:
#             print("cannot divide by 0!!")
#             return
#     return inner
#
# @dec_division
#
# def divide(a,b):
#     return a/b
#
# print(divide(15,3))
# print(divide(15,0))

################################################
# chaining decorator
def star(func):
    def inner():
        print("*"*30)
        func()
        print("*"*30)
    return inner

def hash(func):
    def inner():
        print("#"*30)
        func()
        print("#"*30)
    return inner

@star
@hash
def printer():
    print("welcome python")

printer()


# area square = num
# volume square = num