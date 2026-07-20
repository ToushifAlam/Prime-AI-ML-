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
    @staticmethod
    def discount(price, disc):
        final_price = price - (price*disc / 100)
        return final_price
p1 = Products("Phone", 10_000)
p2 = Products("Laptop", 40_000)
p3 = Products("Pen", 10)
p4 = Products("Watch", 5_000)
print(f"Product {p1.name} has price {p1.price}")
print(f"Product {p2.name} has price {p2.price}")
print(f"Product {p3.name} has price {p3.price}")
print(f"Total products = {Products.count}")
print(f"Final price of {p1.name} after 15% discount is {p1.discount(p1.price, 10)}")
print(f"Final price of {p2.name} after 15% discount is {p2.discount(p2.price, 15)}")
print(f"Final price of {p3.name} after 15% discount is {p3.discount(p3.price, 20)}\n")

# Encapsulation
class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name # public
        self._balance = balance # protected <- conventional but not enforced
        self.__pin = pin # private <- Enforcing works
    def get_pin(self):
        return self.__pin
    def set_pin(self, newPin):
        self.__pin = newPin

acc1 = BankAccount("Rahul Kumar", 100_000, 4653)
print(acc1.name, acc1._balance, acc1.get_pin())
acc1.set_pin(6732)
print(acc1.name, acc1._balance, acc1.get_pin())
print(acc1._BankAccount__pin) # It's not true protected in Python so ends the concept of data hiding
print()

# Inheritance
class Employee:
    start_time = "10am"
    end_time = "6pm"
    def change_time(self, new_end_time):
        self.end_time = new_end_time
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

t1 = Teacher("Math")
print(t1.subject, t1.start_time, t1.end_time)
t1.change_time("7pm")
print(t1.subject, t1.start_time, t1.end_time)
st1 = AdminStaff("manager")
print(st1.role, st1.start_time, st1.end_time)
ac1 = Accountant(25_000, "CA")
print(ac1.role, ac1.salary, ac1.start_time, ac1.end_time,"\n")

# Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar!")
class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()
cow = Cow()
cow.make_sound()
print()

# Polymorphism -- Function Overriding & Duck Typing
class Employee:
    def get_designation(self):
        print("Designation = Employee")
class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")
t1 = Teacher()
t1.get_designation()