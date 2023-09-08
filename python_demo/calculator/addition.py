

def sum(a, b):
    return a + b


class addition:
    def sum(self, a, b):
        print("func inside class")
        return a + b

# print("executing addition module")
# print(sum(2,3))
# obj=addition()
# print(obj.sum(4,5))
# print(__name__)
if __name__=="__main__":
    import multiplication
    print(multiplication.multiply(2, 3))
    print("executing addition module")
    print(sum(2, 3))
    obj = addition()
    print(obj.sum(4, 5))
    print(__name__)

