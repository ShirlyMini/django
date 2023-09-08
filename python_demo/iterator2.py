# userdefined iter

class mynumber:

    def __iter__(self):# initialize
        self.num=1
        return self

    def __next__(self):
        #self.num+=1
        self.num1=self.num**2
        self.num += 1
        return self.num1

obj=mynumber()
var=iter(obj)
print(var)
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))