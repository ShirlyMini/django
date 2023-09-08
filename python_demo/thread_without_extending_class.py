from threading import *

class myclass:

    def myfunc(self, a):
        print(a)
        for i in range(a):
            print("name of current thread", current_thread().name)

obj=myclass()
t1=Thread(target=obj.myfunc, args= [5])
t1.start()
t1.join()
t2=Thread(target=obj.myfunc, args= [8])
t2.start()
t2.join()
