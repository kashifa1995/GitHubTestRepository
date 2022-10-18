# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)

# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
#     # public instance methods
#     def show(self):
#         # private members are accessible from a class
#         print(f"{self.name}'s salary is {self.__salary}.")
#
# # creating object of a class
# emp = Employee('Jessa', 10000)

# # calling public method of the class
# # emp.show()
#
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data members
#         self.name = name
#         self.salary = salary
#
#     # public instance methods
#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)
#
# # creating object of a class
# e = Employee('Jessa', 10000)
#
# # accessing public data members
# print(f"{e.name}'s salary is {e.salary}.")
#
# # calling public method of the class
# e.show()

# class Parent:
#     def sing(self):
#         print("Parent is singing")
#
#     def cook(self):
#         print("Parent is cooking")
#
#
# class Child(Parent):
#     def sing(self):
#         super().sing()
#         print("Child is singing")
#
#
# p1 = Parent()
# c1 = Child()
# p1.sing()
# c1.sing()

l1 = [2, 6, 8, 9, 3, 9, 3, 6, 8, 5]
l1 = sorted(l1)
l2 = []
for i in range(len(l1)):
    if l1[i] == l1[i + 1]:
        l2.append(l1[i])
print(l2)
