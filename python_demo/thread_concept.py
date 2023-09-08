

# for i in range(5):
#     print("process1")

# for i in range(5):
#     print("process2")
#
# for i in range(5):
#     print("process3")


from threading import *
#print(current_thread().name) #MainThread

def process1():
    for i in range(6):
        print("name of current thread", current_thread().name)
        print("process1\n")

def process2():
    for i in range(6):
        print("name of current thread", current_thread().name)
        print("process2\n")

t1=Thread(target=process1)
t2=Thread(target=process2)
print("name of current thread", current_thread().name)
t1.start()
t1.join()
t2.start()
t2.join()
print("name of current thread", current_thread().name)
for i in range(6):
    print("main process\n")