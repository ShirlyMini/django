# While
# works based on conditions
# while <condintion>:
#   statement1
#   statement2

# for i in range(10):
#     print(i)
#
# num = 0
# while num < 10:
#     print(num)
#     num+=1  # ---num=num+1
#
# num = 10
# while num > 0:
#     print(num)
#     num-=1  # ---num=num-1

# a=True
# num=0
# while a:
#     if num==5:
#         a=False
#     print(f"a:{a} .... num:{num}")
#     num+=1
#     #print(f"a:{a} .... num:{num}")
# break, continue, pass --- flow control keywords or statement
# for i in range(20):
#     if i==5:
#         continue
#     if i==12:
#         break
#     print(i) # 0 to 11 and skips 5


# a=True
# num=0
# while a:
#     if num==5:
#         num += 1
#         continue
#     if num==12:
#         break
#     print(f"a:{a} .... num:{num}")
#     num+=1

# pass = do nothing statment mostly used in function, class


# python comprehension

# 1. List comp
# 2. generator comp == tuple comp
# 3. dict comp
# 4. set comp


# print([i for i in range(10) if i<5]) # List comp
# print((i for i in range(10) if i<5))# iterator obj----generator
# print(tuple((i for i in range(10) if i<5)))
# print({i for i in range(10) if i<5})# set comp
# print(type({i for i in range(10) if i<5}))
#
# print({i:None for i in range(10) if i<5}) # dict
# print(type({i:None for i in range(10) if i<5}))
# print(type({i:i for i in range(10) if i<5}))

num=56

print(True if num==56 else False)
print(True if num==59 else False)

a="success" if num==57 else "Failure"
print(a)