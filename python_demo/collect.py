# from collections import Counter
#
# print(Counter([1,2,3,3,4,5,2,3,4,5]))
# print(Counter({"a":1, "b":2, "c":3}))

from collections import OrderedDict
dct1={"a":1, "b":2, "c":3}

#print(OrderedDict(dct1))
# for k, v in OrderedDict(dct1).items():
#     print(f"{k} : {v}")

dct1["d"]=4

# for k, v in OrderedDict(dct1).items():
#     print(f"{k} : {v}")

del(dct1["a"])


dct1["a"]=1
for k, v in OrderedDict(dct1).items():
    print(f"{k} : {v}")