# Day 04: Object-Oriented Programming (OOPs) in Python

# 1. Class and Object
class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)
        print("----------------------")


# Creating objects of the class
student1 = Student("Anshika", 101, "CSE")
student2 = Student("Rahul", 102, "IT")

student1.display_details()
student2.display_details()


# 2. Inheritance
class CollegeStudent(Student):
    def __init__(self, name, roll_no, branch, college):
        super().__init__(name, roll_no, branch)
        self.college = college

    def show_college(self):
        print("College:", self.college)
        print("----------------------")


cs1 = CollegeStudent("Anshika", 101, "CSE", "Sage University")
cs1.display_details()
cs1.show_college()


# 3. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
account.deposit(2000)
print("Current Balance:", account.get_balance())


# 4. Polymorphism
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()
