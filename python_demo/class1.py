# class empty:
#     pass
#     # variable
#     # methods
#
# obj=empty()
# print(obj)

# class demo_var:
#     # class var- bounded to class
#     num=100
#     print(f"class variable : {num}")
#
# obj=demo_var() # instanciate
# print(f"accessing using object {obj.num}")
# obj.num=200
# print(f"After changes....accessing using object {obj.num}")
# obj=demo_var()
# print(f"accessing using object {obj.num}")

class instance_var:
    # class var- bounded to class
    num=100 #---> static variable

    # instance variable - bounded to object
    def __init__(self, a, b): # constructor
        # self ---> indicates the class
        # self can be named in any other name but self is our coding standard
        print("inside constructor __init__ func")
        self.num=a
        self.b=b
        print(f"a:{a} \nb:{b}")

    def add(self):# instance method
        # class var can be accessed using self. and instance variable accessed using self
        #print(f"num:{self.num}\na:{self.a}\nb:{self.b} num+a+b:{self.num+self.a+self.b}")
        # class var access using class name--import
        print(f"num:{instance_var.num}\na:{self.num}\nb:{self.b} num+a+b:{instance_var.num+self.num+self.b}")


obj=instance_var(10, 20) # instantiation
# obj=instance_var(<class_name>10, 20) # instantiation
#obj=instance_var(20, 22)
obj.add()
