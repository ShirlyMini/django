# encapsulation

# access modifiers- __private, public, _protected
class calculator:

    def __init__(self):
        self.a=0
        self.__b=0 # priavte
        self._c=0 # protected

    def __add(self):  # private function
        print("addition")

    def _multiply(self): # protected fuction
        print("multiplication ", self._c)

    def sub(self):
        print("private variable b", self.__b)
        self.__add()
        print("subration")

# obj=calculator()
# obj.add()
# obj.a

# to access private method
# 1) can be accessed using public method
# 2)

# obj=calculator()
# print(obj.a)
# obj.sub()

# obj=calculator()
# #var1=obj.sub()
# print(_calculator__add)


# protected variable--- psudoprotection

obj=calculator()
obj._multiply()
obj._c=100
obj._multiply()
