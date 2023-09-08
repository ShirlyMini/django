class instance_var:
    # class var- bounded to class
    num=100 #---> static variable

    # instance variable - bounded to object
    def __init__(self, a, b): # constructor
        # self ---> indicates the class
        # self can be named in any other name but self is our coding standard

        #print("inside constructor __init__ func")
        self.num =a
        self.a = a
        self.b = b
        #print(f"a:{a} \nb:{b}")

    def add(self, str1, str2="None"):# instance method
        # class var can be accessed using self. and instance variable accessed using self
        #print(f"num:{self.num}\na:{self.a}\nb:{self.b} num+a+b:{self.num+self.a+self.b}")
        # class var access using class name--import
        print(f"num:{instance_var.num}a:{self.num}b:{self.b} num+a+b:{instance_var.num+self.num+self.b}")
        print(f"str1 + str2 = {str1+str2}")

    def sub(self): # instance
        print("inside sub method")
        print(f"num:{instance_var.num}a:{self.num}b:{self.b} num-a-b:{instance_var.num - self.num - self.b}")
        self.add("add", "function")

    @classmethod
    def add_classmethod(cls):
         print("inside addition class method")
         #print(f"num:{instance_var.num}a:{self.num}b:{self.b} num+a+b:{instance_var.num + self.num + self.b}") # ERROR can access only class varible
         print(f"num:{instance_var.num}\n {cls.num+11}") # cls=<classname>
         #instance_var.add_instancemethod() #error

    @classmethod
    def sub_classmethod(cls):
        print("inside subraction class method")
        # print(f"num:{instance_var.num}a:{self.num}b:{self.b} num+a+b:{instance_var.num + self.num + self.b}") # ERROR can access only class varible
        print(f"num:{instance_var.num}\n {cls.num-1}")  # cls=<classname>
        # instance_var.add_instancemethod() #error
        cls.add_classmethod()
        instance_var.add_classmethod()

    # instance method
    def add_instancemethod(self):
         print("inside instance method")
         # instance variable accessed with self
         #print(f"num:{instance_var.num}a:{self.a}b:{self.b} num+a+b:{instance_var.num + self.a + self.b}")
         print(f"num:{self.num}a:{self.a}b:{self.b} num+a+b:{instance_var.num + self.a + self.b}")

         #print(f"num:{instance_var.num}a:{instance_var.a}b:{instance_var.b} num+a+b:{instance_var.num + instance_var.a + instance_var.b}") # instance variable accessed with self

         instance_var.add_classmethod()

    @staticmethod
    def add_staticmethod():
        #print(f"class var: {instance_var.num} instance var:{self.a}") ---ERROR
        print(f"class var: {instance_var.num**2}")


obj1=instance_var(10,20) # calls constructor __init__
#obj1.add("Hello", "python")
#obj1.add("Hello")
#obj1.sub()
#obj1.add_classmethod()
#obj1.add_instancemethod()
#obj1.sub_classmethod()
obj1.add_staticmethod()


# class method can only access class variable and class method
# instance method - you can access instance variable, another instance method , class method and class variable
# Self vs cls

# Class var or method---->
# 1. only class var or class method can go with classname (recommended)
# 2. also can be accessed using 'cls' when it is declared inside classmethod
# 3. also can be accessed using 'self' when it is declared inside instance method
# 4. ensure class variables are different from your instance avriable ...then only 2 and 3 rule will apply

# instance var or method---->
# can go only with 'self'(recommended)