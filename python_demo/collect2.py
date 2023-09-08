# from collections import defaultdict
#
# d = defaultdict(list())
# #d={}
# lst = [1,2,3,4,5]
#
# for i in lst:
#     d[i]=i
#
# print(d)

# Python program to demonstrate
# defaultdict


# from collections import defaultdict
#
# # Defining a dict
# d = defaultdict(list)
#
# for i in range(5):
#     d[i].append(i)
#
# print("Dictionary with values as list:")
# print(d)

# from collections import ChainMap
#
# d1 = {1: "One", 2: "Two", 3: "Three"}
# d2 = {4: "four", 5: "five"}
# d3 = {6:"Six", 7:"seven"}
# c=ChainMap(d1,d2,d3)
# print(c)
# print(c[2])
# print(list(c.values()))
# print(list(c.keys()))
# d4={8:"eight", 9:"nine"}
# c1=c.new_child(d4)
# print(c1)

# from collections import namedtuple
#
# n=namedtuple("emp",["name", "doj", "empid"])
#
# add_values=n("shirly", "16thaug", "12345")
# print(add_values[0])
# print(add_values.name)
# print(add_values.doj)

#deque- double ended queue
# from collections import deque
#
# que = deque([1,2,3,4,5,6,7])
# print(que)
# que.pop()
# print(que)
# que.popleft()#--FIFO
# print(que)
#
# que.append("a")
# print(que)
# que.appendleft("z")
# print(que)



