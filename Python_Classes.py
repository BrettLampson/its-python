
# from pprint import pprint

# ------------------------------------------------------------------------------------------------ #
# CLASSES (object oriented programming)

# A class is a way to take a grouping of functions and data and place them inside
#   a container so you can access them with dot notation. (Ex: user.f_name)
# A class bundles up logically grouped functions (called methods) and variables (called attributes)

# ------------------------------------------------------------------------------------------------ #
# WHEN TO USE A CLASS:
# Defining the general behavior that a whole category of objects can have.
# When you create individual objects from the class, each object is equipped with
#   the general behavior; you can then give each object whatever unique traits you want.
# INSTANTIATION:  Making an object from a class.


# ------------------------------------------------------------------------------------------------ #
# Crash Course Book

# class Car:
#     """Representation of a car."""
#
#     def __init__(self, make, model, year):  # <--- Method
#         """Initialize the following attributes to describe a car."""
#         self.make = make         # <--- Attribute
#         self.model = model       # <--- Attribute
#         self.year = year         # <--- Attribute
#         self.odometer_value = 0  # <--- Attribute that will change over time
#
#     def get_full_name(self):     # <--- Method
#         """Return a neatly formatted descriptive name"""
#         full_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return full_name.title()
#
#     def display_odometer(self):
#         """Print the cars current mileage"""
#         return 'Current Miles = ' + str(self.odometer_value)
#
#     def increment_odometer(self, miles: int):
#         """Add new mileage to old mileage"""
#         self.odometer_value += miles
#         return 'Current Miles = ' + str(self.odometer_value)
#
#
# shaina_car = Car('Honda', 'CR-V', 2016)  # <--- Instance of the Car class
# print(shaina_car.get_full_name())
# print(shaina_car.display_odometer())
# print(shaina_car.increment_odometer(5))
# print(shaina_car.increment_odometer(1))


# Modify an attributes value in 3 ways:

# 1) directly through instance
# shaina_car.odometer_value = 33
# print(shaina_car.display_odometer())  # Current Miles = 33

# 2) set the value through a method
# def update_odometer(self, mileage):
#     """Updating the mileage value"""
#     self.odometer_value = mileage

# 3) increment the value
# def increment_odometer(self, miles):
#     """Add new mileage to old mileage"""
#     self.odometer_value += miles


# class ElectricCar(Car):  # <--- Inheriting attributes from Car class
#     """Represents aspects of a car, but specific to electric vehicles"""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)  # <--- super() helps pass on attributes of parent class
#         self.battery_size = 70  # <--- attribute specific to child class ElectricCar
#
#     def describe_battery(self):
#         """Returns a statement describing the battery size"""
#         pretext = 'This battery has '
#         return pretext + str(self.battery_size) + '-kWh'
#
#
# brett_car = ElectricCar('tesla', 'model s', 2018)
# print(brett_car.get_full_name())
# print(brett_car.display_odometer())
# print(brett_car.describe_battery())

# WIP try override parent class method by using same method name with different attributes...


# ------------------------------------------------------------------------------------------------ #
# Corey Schafer Example

# class Employee:
#     """This is a docstring, use it to describe the class"""
    # docstrings show up in help(emp1)
    # CamelCase for naming classes.  "()" optional for PARENT classes.

    # state_income_tax = .0892
    # Class variable / Shared amongst all instances of Employee class unless
    # it is reassigned outside of class block (ex. emp2.state_income_tax = .1055)

    # num_of_employees = 0
    # Class variable that won't change, until we increment in init method.

    # def __init__(self, fname, lname, position, salary):
    #     self.fname = fname
    #     self.lname = lname
    #     self.position = position
    #     self.salary = salary
    #     self.raises_received = 0
    #     self.email = fname + '.' + lname + '@babycorp.com'
    #     Employee.num_of_employees += 1
        # __init__ initializes an objects (emp1, emp2 below).
        # The self parameter MUST come first for EVERY method used.
        # self argument specifies that it refers to the class itself.
        # fname, lname, position, etc. are all attributes of the Employee() class.
        # All these self.things are shared amongst all instances of Employee (emp1, emp2)

    # def fullname(self):
    #     """prints full name."""
        # return '{} {}'.format(self.fname, self.lname).title()
        # fullname() is a method of the Employee class.
        # DO NOT FORGET the 'self' arguments

    # def raise_amount(self, amount):
    #     """adjusts for any raise an employee receives"""
    #     self.raises_received += 1
    #     self.salary = self.salary + amount
    #     print('raise', self.raises_received, '=', amount)
    #
    # def bimonthly_pay(self):
    #     return (self.salary / 24) * (1 - self.state_income_tax)
        # 'self' state_income_tax allows new instances to have a unique tax like real world.


# creating the instances
# emp1 = Employee('brett', 'lampson', 'data scientist', 70000)
# emp2 = Employee('shaina', 'lampson', 'ux/ui designer', 70000)
            # emp1, emp2 are instances of the Employee class.
            # When creating these objects (emp1 and emp2), the Python interpreter
            # uses the special __init__() method we defined to initialize these objects.
            # These instances share those attributes listed as args in __init__.

# adjust state_income_tax directly
# emp2.state_income_tax = .1055
            # Reassigned class variable state_income_tax, affects emp2 ONLY
            # Employee.state_income_tax = .1055, affects ALL instances



# To access these attributes of the Employee class we use dot notation.
# print(emp1.fullname())                         # Brett Lampson
# print(emp1.email)                              # brett.lampson@company.com
# print(emp1.position.title())                   # Software Engineer
# emp1.raise_amount(5000)
# emp1.raise_amount(4000)
# print('{0:.2f}'.format(emp1.salary))           # 79000.00
# print('{0:.2f}'.format(emp1.bimonthly_pay()))  # 2998.05
# print('-'*50)
#
# print(emp2.fullname().title())                 # Shaina Lampson
# print(emp2.email)                              # shaina.lampson@babycorp.com
# print(emp2.position.title())                   # Ux/Ui Designer
# print('{0:.2f}'.format(emp2.salary))           # 70000.00
# print('{0:.2f}'.format(emp2.bimonthly_pay()))  # 2656.50
# print('-'*50)
# print('Employees =', Employee.num_of_employees)     # 2


# You can also see how it works using this:
# print()
# print(Employee.fullname(emp1))
# print(emp1.fullname())


# Lookup instance namespaces using instance.__dict__
# print()
# pprint(Employee.__dict__)
# print('-'*50)
# pprint(emp1.__dict__)
# print('-'*50)
# pprint(emp2.__dict__)

# print(help(Employee))


# ------------------------------------------------------------------------------------------------ #
# Socratica Example


# class User:
#     pass
#
#
# user = User()               # instance of the User class, or aka object
# user.first_name = 'Dave'     # Fields specific to user1
# user.last_name = 'Lampson'   # Fields specific to user1
# user.age = 37
# # user.status = 'married'
# # print(user.first_name)
# # print(user.first_name)
# first_name = user.first_name
# print(first_name)

# print(help(User))

# ------------------------------------------------------------------------------------------------ #
# SOCRATICA CLASSES

# import datetime
#
# class User:
#     """A member of FriendFace."""
#     def __init__(self, full_name, birthday, sex):
#         """Initializes the Class"""
#         self.name = full_name
#         name_pieces = full_name.split(' ')
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#         self.birthday = birthday  # yyyymmdd
#         self.sex = sex
#
#     def age(self):
#         """Return the age of the user in years"""
#         today = datetime.date.today()
#         yyyy = int(self.birthday[0:4])
#         dd = int(self.birthday[4:6])
#         mm = int(self.birthday[6:8])
#         dob = datetime.date(yyyy, mm, dd)
#         age_in_days = (today - dob).days
#         age_in_years = age_in_days / 365
#         return int(age_in_years)
#
#     def gender(self):
#         sex_title = str(self.sex).title()
#         return sex_title
#
#
# user1 = User('Dave Bowman', '19780504', 'male')
# print(user1.name, user1.birthday)
# print('- OR -')
# print('Hello', user1.first_name, user1.last_name, )
# print(user1.age())
# print(user1.gender())

# print(help(user1))   # SEE ALL THE METHODS IN A CLASS WITH HELP()


# ------------------------------------------------------------------------------------------------ #
# HOW CLASSES WORK WITH DATA

# import csv
# from pprint import pprint
#
#
# class Dataset:
#     def __init__(self, data):
#         self.type = "csv"
#         self.data = data
#
#
# nfl_data = open('nfl.csv', 'r', encoding='utf-8-sig')
# print(nfl_data)
# # <_io.TextIOWrapper name='nfl.csv' mode='r' encoding='utf-8-sig'>
#
# nfl_dataset = csv.reader(nfl_data)
# print(nfl_dataset)
# # <_csv.reader object at 0x1019605f8>
#
# dataset_data = list(nfl_dataset)
# pprint(dataset_data)
# [['year', 'week', 'winner', 'loser'],
#  ['2009', '1', 'Pittsburg', 'Tennessee'],
#  ['2009', '1', 'Minnesota', 'Cleveland'],
#  ['2009', '1', 'New York Giants', 'Washington'],
#  ['2009', '1', 'San Francisco', 'Arizona'],
#  ['2009', '1', 'Seattle', 'St. Louis Rams']]