# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:21:53 2017

@author: Administrator
"""

#Why Use class:-A class is just a way of organizing 
#and producing objects with similar attributes and methods.

class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()



#Class Syntax: A basic class consists only of the class keyword, 
#the name of the class, and the class from which the new class inherits in parentheses.
#pass keyword doesn't do anything, but it's useful as a placeholder in areas of your
# code where Python expects an expression

class Animal(object):
  pass


"""we started our class definition off with an odd-looking function: 
__init__(). This function is required for classes, and it's used to 
initialize the objects it creates. __init__() always takes at least 
one argument, self, that refers to the object being created. 
You can think of __init__() as the function that "boots up" each
object the class creates.Python will use the first parameter that
__init__() receives to refer to the object being created; this is
why it's often called self, since this parameter gives the object 
being created its identity.If you add additional arguments—for instance,
 a name and age for your animal—setting each of those equal to self.name
 and self.age in the body of __init__() will make it so that when you create
 an instance object of your Animal class, you need to give each instance a 
 name and an age, and those will be associated with the particular instance
 you create."""
class Animal1(object):
  def __init__(self):
    pass

class Animal2(object):
  def __init__(self,name):
    self.name = name
#Defining Object
zebra = Animal2("Jeffrey")
print (zebra.name)

class Animal3(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal3("Jeffrey", 2, True)
giraffe = Animal3("Bruce", 1, False)
panda = Animal3("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

"""Class Scope:- all variables are accessible to all parts of a Python
 program at all times. When dealing with classes, you can have variables
 that are available everywhere (global variables), variables that are only
 available to members of a certain class (member variables), and variables
that are only available to particular instances of a class (instance variables).
The same goes for functions: some are available everywhere, some are only
available to members of a certain class, and still others are only available 
to particular instance objects."""
#member is_alive accessible by all objects
class Animal4(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal4("Jeffrey", 2)
giraffe = Animal4("Bruce", 1)
panda = Animal4("Chad", 7)

print (zebra.name, zebra.age, zebra.is_alive)
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)

"""When a class has its own functions, those functions are called methods. """
class Animal5(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print (self.name)
    print (self.age)
    
hippo = Animal5("Simon", 3)
hippo.description() 

"""Multiple Members: A class can have any number of member variables. 
These are variables that are available to all members of a class.
Change in any member of variable will only change that varibale not others
Ex:-
In the example above, we create two instances of an Animal.
Then we print out True, the default value stored in hippo's is_alive member variable.
Next, we set that to False and print it out to make sure.
Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.
"""
hippo1 = Animal5("Jake", 12)
cat = Animal5("Boots", 3)
print (hippo1.is_alive)
hippo1.is_alive = False
print (hippo1.is_alive)
print (cat.is_alive)

"""Exmaple:- Shopping Cart"""

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")

my_cart = ShoppingCart("Hemant")
my_cart.add_item("Rice", 5)


"""INheritence: Inheritance is the process by which one class takes
 on the attributes and methods of another, and it's used to express 
 an is-a relationship. For example, a Panda is a bear, so a Panda class
 could inherit from a Bear class. However, a Toyota is not a Tractor, 
 so it shouldn't inherit from the Tractor class (even if they have a lot
 of attributes and methods in common). Instead, both Toyota and Tractor 
 could ultimately inherit from the same Vehicle class.
EX:-  We've defined a class, Customer, as well as a ReturningCustomer
 class that inherits from Customer. Note that we don't define the 
 display_cart method in the body of ReturningCustomer, but it will 
 still have access to that method via inheritance. 
 
 SYNTAX:- class DerivedClass(BaseClass):
 where DerivedClass is the new class you're making and BaseClass
 is the class from which that new class inherits."""
 
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


""" Override:- Sometimes you'll want one class that inherits from another 
to not only take on the methods and attributes of its parent, but to override 
one or more of them.
EX:- Rather than have a separate greet_underling method for our CEO, 
we override (or re-create) the greet method on top of the base Employee.greet
 method. This way, we don't need to know what type of Employee we have before
 we greet another Employee."""
 
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print ("Hello, %s" % other.name)

class CEO(Employee):
  def greet(self, other):
    print ("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!


"""Super Call:- On the flip side, sometimes you'll be working 
with a derived class (or subclass) and realize that you've overwritten
 a method or attribute defined in that class' base class (also called a
 parent or superclass) that you actually need. Have no fear! You can directly
 access the attributes or methods of a superclass with Python's built-in super call.
The syntax looks like this:
class Derived(Base):
  def m(self):
    return super(Derived, self).m()
Where m() is a method from the base class."""

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def full_time_wage(self, hours):
    return super(PartTimeEmployee,self).calculate_wage( hours)
  
milton = PartTimeEmployee("Roham")
print (milton.full_time_wage(10))


# Class Example: TRiangle

class  Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  def check_angles(self):
    sum = 0
    sum = self.angle1 + self.angle2 + self.angle3
    if(sum == 180):
      return True
    else:
      return False
    
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


"""Class member variables

Classes can have member variables that store information about each 
class object. We call them member variables since they are information 
that belongs to the class object.
class ClassName(object):
  memberVariable = "initialValue"
"""

"""BUilding Your own Car"""
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    print ("This is a " +self.color + " " +self.model + " with "+ str(self.mpg)+ " MPG.")
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, battery_type, model, color, mpg):
    self.battery_type = battery_type
    self.model = model
    self.color = color
    self.mpg   = mpg
  def drive_car(self):
    self.condition = "like new"
#Override Methods
my_car = ElectricCar("molten salt","DeLorean", "silver", 88)
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)


"""__repr__ Method:- class method to override is the built-in __repr__() method, 
which is short for representation; by providing a return value in this method, 
we can tell Python how to represent an object of our class (for instance, 
when using a print statement)."""

class Point3D(object):
  def __init__(self, x,y,z):
    self.x = x
    self.y =y
    self.z=z
  def __repr__(self):
    return("(%d, %d, %d)" % (self.x, self.y, self.z))
  
my_point = Point3D(1,2,3)
print (my_point)




