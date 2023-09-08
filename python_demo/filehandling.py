# modes r - reading w - writeing - a -  appened

# fh = open("file1.txt", "r")
# print(fh.read())
# fh.close()


# if file not exist, fh creates new file and writes the content
# if file already exist fh overwrites the existing content with new content
# fh = open("file1.txt", "w") #
# fh.write("this is my second line")
# fh.close()
#
# fh = open("file2.txt", "w") #
# fh.write("this is my second line")
# fh.close()

# append
# if file not exist, fh creates new file and writes the content
# if file already exist fh appends with the existing content with new content

# fh = open("file2.txt", "a")
# fh.write("this is my third line")
# fh.close()
#
# fh = open("file3.txt", "a")
# fh.write("this is my third line")
# fh.close()

# with function
# with open("file1.txt", "r") as reader:
#     #print(type(reader.read())) # string
#     # print(reader.readlines()) # list of lines
#     # for i in reader.readlines():
#     #     print(i)
#     print(reader.readline())
#     print(reader.readline())
#     print(reader.readline())

# binary files
# with open("file1.txt", "wb") as writer:
#     writer.write(b"binary file writer")
#
# with open("file1.txt", "ab") as writer:
#     writer.write(b"binary file writer second")
#
# with open("file1.txt", "rb") as reader:
#     print(reader.read())

# serialization - content -> byte code
# deserialization - bycode -> content
# pickle

import pickle
pooja={"Name": "pooja", "age":"15", "education":"10"}
sita={"Name": "sita", "age":"17", "education":"12"}

db={"student1":pooja, "student2": sita}
with open("file4.txt", "wb") as writer:
    pickle.dump(db, writer)# convert to byte codes

with open("file4.txt", "rb") as writer:
    data= pickle.load(writer) # convert bytes to human readable form
    print(data)
    print(data["student1"])
    print(data["student2"])