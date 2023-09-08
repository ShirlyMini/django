# multiple inheritance

class parent1:
    def __init__(self, a,b):# constructor
        print("executing parent1 constructor")
        self.a= a
        self.b= b

    def parent1method(self):
        print("executing parent1 method")
        print(f"a:{self.a}  b:{self.b} c:{self.c}  d:{self.d}")

class parent2:
    def __init__(self, a, b):# constructor
        print("executing parent2 constructor")
        self.c = a
        self.d = b

    def parent2method(self):
        print("executing parent2 method")
        print(f"a:{self.a}  b:{self.b} c:{self.c}  d:{self.d}")

class child(parent2, parent1):
    def __init__(self):
        parent1.__init__(self, 10,20)
        parent2.__init__(self, 100,200)

    def childmethod(self):
        print("executing child method")
        print(f"a:{self.a}  b:{self.b} c:{self.c}  d:{self.d} ")#e:{self.e}  f:{self.f}

obj_child=child()# calls constructor
obj_child.childmethod()

# MRO-method resolution order
# 1) child construtor
# 2) will execute in order given in the parameter