#single inheritance- single parent to child

class parent:
    def __init__(self, a,b):# constructor
        print("executing parent constructor")
        self.a= a
        self.b= b

    def parentmethod(self):
        print("executing parent method")
        print(f"a:{self.a}  b:{self.b} c:{self.c}  d:{self.d}")

class child(parent):
    def __init__(self,a, b, c, d):# constructor
        print("executing child constructor")
        # 1. can pass arguments directly
        # parent.__init__(self, 10,20)
        # 2. get the arguments from child class
        parent.__init__(self, a,b)
        self.c = c
        self.d = d

    def childmethod(self):
        print("executing child method")
        print(f"a:{self.a}  b:{self.b} c:{self.c}  d:{self.d}")

obj_child=child(20, 30, 40, 50)# calls constructor
obj_child.childmethod()
obj_child.parentmethod()

# obj_parent=parent()
# obj_parent.parentmethod()
#obj_parent.childmethod()---ERROR

# 1. if parent and child has constuctor(def __init__)
#  Method resolution order :
# r1. if child has constuctor.. at the time of obj creation child constuctor will be called
# if child doesnt have constructor ... at the time of obj creation prarent constrctor will be called
# priority--> child---> parent
#
