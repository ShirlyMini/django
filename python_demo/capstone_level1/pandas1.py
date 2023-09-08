import pandas as pd
data=["apple", "banana","carrot"]
index = ["a","b","c"]


s = pd.Series(data, index=index)# List
print(s)

data_dict = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
index = ["a","b","c", "d"]

d=pd.DataFrame(columns=["one", "two"])# Dict
print(len(d))
d.loc[1]=["a","b"]
d.loc[2]=["a1","b1"]
print(len(d))
print(d)