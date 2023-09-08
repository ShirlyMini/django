import re

lst = ["google.com", "amazon.in"]
# search and replace
for str in lst:
    print(re.sub("com|in", "biz", str))

lst = ["text1.txt", "text2.log", "text3.xml", "text4.html"]
lst1=[]
for str in lst:
    lst1.append(re.sub("txt|log|xml", "html", str))

print(lst1)

