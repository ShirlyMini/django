# with parameters
# passing parameter
# def add(a, b, c, d):
#     return f"{a} + {b} + {c} + {d} = {a + b + c + d}"


#print(add(10, 20, 30, 40))
#print(add(20, 10, 30, 40))  # positional arguments
#print(add(d=20, a=10, c=30, b=40))  # positional parameters ---> called using keyword arguments

# keyword arguments

# def add(a=10, b=10, c=10, d=10): # default parameters
#     return f"{a} + {b} + {c} + {d} = {a + b + c + d}"
#
# print(add())
# print(add(a=40,b=30,c=20,d=10)) # keyword arguments
# print(add(c=20,b=30,d=10,a=40)) # unordered
# print(add(1,2,3,4)) # based on position
# print(add(1,2,c=33,d=44)) # mixing 1.positional and 2.keyword args
# #print(add(c=33,d=44, 1,2,)) # mixing 1. keyword and 2.positional args--ERROR
# #print(add(1,2,a=55,b=66)) # got multiple values for argument 'a'--ERROR
# print(add(1,2,d=55,c=66))
# print(add(1,2,3)) # value for d is default on ethet is 10

# mixing positional and keyword arguments

# def add(a, b, c=10, d=10):
#     return f"{a} + {b} + {c} + {d} = {a + b + c + d}"
#
# #print(add()) # ERROR
# print(add(1, 2))
# print(add(1, 2, 3)) # based on position c takes the value 3
# print(add(1, 2, 3, 4)) # based on position c takes the value 3 d takes the value 4
# print(add(1, 2, d=3, c=4)) # 1 + 2 + 4 + 3 = 10
# print(add(a=1, b=2, d=3, c=4)) # 1 + 2 + 4 + 3 = 10
# print(add(b=1, a=2, d=3, c=4)) # 1 + 2 + 4 + 3 = 10



# *args and **kwargs
# *args ----> array---> positional aurgs
# **kwargs ---> dict---> keyword args

# def add(*args):
#     print(args)
#     print(type(args))
#     print(list(args))
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#
#
# add(10, 20, 30, 40, 50, 60, 70)

# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     sum=0
#
#     for i in kwargs.values():
#         sum=sum+i
#         #print(sum)
#     print(sum)
#
# add(x=100, y=200, z=400, a=2, b=3, x1=100, y1=200, z1=400)


# def add(*args, **kwargs):
#     print(f"args: {args}")
#     print(type(args))
#     print(f"kwargs: {kwargs}")
#     print(type(kwargs))
#
# add(1,2,3,4,6, x=100, y=200, z=400, a=2)
# add(x=100, y=200, z=400, a=2, 1,2,3,4,6)#---ERROR

# lambda

# def add(a,b):
#     return a+b
#
# print(add(2,3))

add = lambda a,b: a+b  # anonymous function

print(add(2,3))

# def bool(a,b):
#     return a>b
#
# print(bool(2,3))

bool = lambda a,b:a>b

print(bool(2,3))