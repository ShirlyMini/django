from threading import *

class A_child(Thread):

    def run(self):
        for i in range(6):
            print("name of current thread", current_thread().name)
            print("process child\n")

#print(dir(Thread))

obj=A_child()
obj1=A_child()
obj.start()
obj1.start()
obj.join()
obj1.join()