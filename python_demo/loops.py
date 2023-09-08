# for loop & while &

# for loop based on iterators
# while loop based on condition

# for i in range(10):
#     print(i)

# for i in range(3,10):
#     print(i)

# for i in range(0,10,3):
#     print(i)

# strings

# str1="python"
#
# for i in str1:
#     print(i)
#     if i=="t":
#         print("we caught letter t")

# list, tuple

# l1=["one", "two", "three", "four"]
# for i in l1:
#     print(i)

# dict

d1={"one":1, "two":2, "three":3, "four":4}

# for i in d1: # returns Key
#     print(i)

for i in d1.values():
    print(i)

for i in d1.keys():
    print(i)

for i in d1.items():
    print(i)# tuples
    print(i[0], i[1])

for key, val in d1.items():
    #print(i[0], i[1])
    print(key, val)