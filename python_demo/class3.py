class employee:
    salary=10000

    def __init__(self, name, doj, company):
        self.name=name
        self.doj=doj
        self.company=company

    # instance methods
    # self--> instance obj
    def employee_info(self):
        print(f"name: {self.name}   doj:{self.doj}  company_name:{self.company}")

    # class method
    @classmethod    # decorator
    def employee_sal(cls, sal=10000):
        print("default salary",cls.salary)
        print("changed salary", sal)

    # classmethod constuctor
    @classmethod
    def from_database(cls, emp_info):
        emp_info_list = emp_info.split("-")
        obj=employee(emp_info_list[0], emp_info_list[1], emp_info_list[2]) # calls constuctor
        return obj

    @staticmethod
    def available_domains(domain):
        domains= ["testing", "dev"]
        if domain in domains:
            return True
        else:
            return False


obj1=employee("ram", 2018, "xyz company")
obj2=employee("sam", 2020, "abc company")

# obj1.employee_info()
# obj1.employee_sal()
# obj2.employee_info()
# obj1.employee_sal(12000)

emp1="sita-2022-abccompany"
emp2="pooja-2016-xyzcompany"

# sita=emp1.split("-")
# obj3=employee(sita[0], sita[1], sita[2])
# obj3.employee_info()
# obj3.employee_sal("15000")


class_obj = employee.from_database(emp2) # class method --> obj created--> constructor--> return obj(class_obj)
#class_obj.employee_info()
#class_obj.employee_sal("180000")

# static method
print(class_obj.available_domains("research"))
print(employee.available_domains("dev"))
