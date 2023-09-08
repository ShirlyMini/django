# "+" List - combines 2 list
# Str concatenate
# num add-----opreator overloading
#############################################33

# len()--->str
# list-->length of list
# dict---> lent of key value pair----polymorpysm--->method overloading, method overriding

# def add(a,b):
#     return a+b
#
# print(add(1,2,3,4))# method overload
#
# # default/ keword parametrs
#
# def add(a=None, b=None, c=None):
#     return a+b+c
#
# add(1,2,3)
#
# def (*args):
#     # logic for addition
#     return

# method overriding

# def add(a, b):
#     print("fuction 1")
#
# def add(a,b,c):
#     print("function2")
#
# def add(a,b,c,d):
#     print("function3")
#
# add(1,2,3,4)

# ploy + inheritance

# class vehicle:
#     def speed(self):
#         print("executing speed func of class VEHICLE")
#
# class car(vehicle):
#     def speed(self):
#         print("executing speed func of class CAR")
#
# class truck(car):
#     def speed1(self):
#         print("executing speed func of class TRUCK")
#
# obj = truck()
# obj.speed()

class vehicle:#--parent--user1
    def speed(self):
        print("executing speed func of class VEHICLE")

class car():#---parent---user2
    def speed(self):
        print("executing speed func of class CAR")

class truck(vehicle,car):
    def speed11(self):
        print("executing speed func of class TRUCK")

obj = truck()
obj.speed()