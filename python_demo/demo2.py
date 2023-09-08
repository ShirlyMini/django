# str1 = "hello python"
# slicing- to get substr
# range starts from n to n+1
# print(len(str1)) # gets the length of the str n+1
# print(str1[6:12])
# print(str1[0:5])
# print(str1[3:len(str1)])

# str2="welcome to python learning"
# # slicing syntax [start: stop :step] default step value=1
# print(str2[3:])
# print(str2[3::2])
# print(str2[3:17:4])
# # reverse indexing
# print(str2[::-1])
# print(str2[len(str2):0:-1])

# list = array of heterogeneous element
# mutable = can be editted, altered, changed
# [1,2,3, "python", [],(),{}]
# l1=[1,2,3,4,5,6,7]
# l2=["ab", "bc", "cd"]
# print(l1+l2) # combines to list
# print(l1*4) # repeats and combine to list
# # elements can be accessed using index
# print(l1[3:])
# print(l1[::-1])

# split/join function
# split=converts string to list
# join=converts list to string

# s1="welcome to python"
# s2="welcome*to*python"
# print(s1.split()) # default delimiter "space"
# print(s2.split("o")) # default delimiter "space"
#
# list1=['welcome', 'to', 'python', "world"]
# print(" ^^^^^ ".join(list1))
# print(" ".join(list1))

# list methods

# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2=["ab", "bc", "cd"]
# l1.append("one")
# print(l1)
# l1.insert(2,"three") # using method
# print(l1)
# l1[2]="four" # using index
# print(l1)
# l1.pop() # deleted last elements
# print(l1)
# l1.pop(2)
# print(l1)
# l1.extend(l2) # combines l2 with l1, does the same oper like '+' operator
# print(l1)
# print(l2)
# l1 = [1, 2, 2,2,2,3, 3, 4, 5, 6, 7]
# print(l1.count(2))
# print(l1)
# l1.clear()
# print(l1)
#
# #--- initialize empty list
# l2=[]
# l3=list()
# print(l2)
# print(l3)
# l1 = [1, 2, 2,2,2,3, 3, 4, 5, 6, 7]
# l1.reverse()
# print(l1)

# tuple - immutable
# t1 = (1, 2, 3,3,3, 4, 5, 6, 7)
# t2 = ("ab", "bc", "cd")
# print(t1+t2)
# #t1[0] = "one"
# print(t1.index(3))
# print(t1.count(3))


# list to tuple
# tuple to list
# t2 = ("ab", "bc", "cd")
# print(type(t2))
#
# l2=list(t2)
# print(type(l2))
# print(l2)
#
# t2=tuple(l2)
# print(t2)

# ranges (start, stop, step) step default 1
print(range(10))
for i in range(3,10,2):
    print(i)
