# Object Oriented Programming (OOPs)
# Class & Object -> Object is an instance of a class
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        print("Constructor was called...")
    subject = "Python"
    college = "NSUT"
    year = 4
    def get_cgpa(self):
        return self.cgpa
st1 = Student("Rahul", 9.0)
st2 = Student("Urvashi", 8.4)
st3 = Student("Shradha", 9.2)
print(st1.subject, st1.college, st1.year, st3.name, st2.cgpa)
print(f"{st1.name} from {st1.college} in {st1.subject} has cgpa of {st1.get_cgpa()}")
print(f"{st2.name} has cgpa of {st2.get_cgpa()}")
print(f"{st3.name} has cgpa of {st3.get_cgpa()}\n")

class CollegeStudent:
    college_name = "IIT(ISM) Dhanbad"
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = CollegeStudent("Pranjali", 8.9)
print(stu1.name, stu1.college_name, CollegeStudent.college_name,"\n")

class Laptop:
    storage_type = "ssd"
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
    
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
    
    @staticmethod
    def discount(price, disc):
        final_price = price - (disc*price / 100)
        print(f"Discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
l1.get_info()
l2.get_info()
l1.get_storage_type()
l1.discount(40_000, 15)
print()

class Products:
    count = 0
    def __init__(self, name, price):
        Products.count += 1
        self.name = name
        self.price = price
    #@staticmethod
    def discount(self, disc):
        final_price = self.price - (self.price*disc / 100)
        return final_price
p1 = Products("Phone", 10000)
p2 = Products("Laptop", 40000)
p3 = Products("Pen", 10)
print(f"Product {p1.name} has price {p1.price}")
print(f"Product {p2.name} has price {p2.price}")
print(f"Product {p3.name} has price {p3.price}")
print(f"Total products = {Products.count}")
print(f"Final price of {p1.name} after 15% discount is {p1.discount(15)}")
print(f"Final price of {p2.name} after 15% discount is {p2.discount(15)}")
print(f"Final price of {p3.name} after 15% discount is {p3.discount(15)}")