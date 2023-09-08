import threading
from threading import Thread
class sharedres:
    def tables(self,num):
        for i in range(1,11):
            print(f"{num} X {i} = {num*i}")

class myclass(Thread):
    def __init__(self,num, tableobj):
        Thread.__init__(self)
        self.num=num
        self.tableobj=tableobj

    def run(self):
        threadlock.acquire()# lock the thread
        self.tableobj.tables(self.num)
        threadlock.release()

table_obj=sharedres()
threadlock = threading.Lock()
myclass_obj1=myclass(5,table_obj)
myclass_obj2=myclass(8,table_obj)
myclass_obj3=myclass(2,table_obj)

myclass_obj1.start()
myclass_obj2.start()
myclass_obj3.start()
myclass_obj1.join()
myclass_obj2.join()
myclass_obj3.join()
