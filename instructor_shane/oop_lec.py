##########
#### OOP (Object Oriented Programming)
############
### THEORY
# OOP (Object Oriented Programming) is a design paradigm
# A design paradigm as the name implies is a way of designing your code, or put another way it is a way of thinking about and organizing your code

## Coupling your Code
# so far you guys have learned about data (i.e array, string, tuple, dictionary, number) and functions 
# when you wanted to use a piece of data in a function you would store the data in a variable and then pass it in as a parameter, and you could manipulate a piece of data in that way

def add1(num)
  num = num + 1
myNum = add1(5)

class myNumber(object):
  def __init__(self, num):
    self.num = num

  def add1():
    self.num +=1

myNum = myNumber(5)
myNum.add1()
print myNum.num
# but how do we know that this piece of data is connected to this function? the data is “decoupled” from the functions that operate on it
# you could name the variable as something related to the function, but they are not intrinsically linked
# this is where OOP comes in, in OOP the data and the functions are “coupled”, in OOP we group certain functions and certain data together

## Hallmarks of OOP
# classes
# instances
# attributes (variables / data), methods (functions)
# inheritance

## Class and Instances - Car blueprint vs an actual Car
# have a class - like a blueprint/factory
     # it specifies what the car will be like - its attributes, and also makes the car object
# and you instantiate objects of that class
# car has methods and car has attributes
    # - it may have attributes like 4 wheels (which all cars share)
    # - or attributes like a given color, which some other cars may share and some others might not
    # - and they may have methods like drive forward. In true oop style, the method drive forward is coupled with the car data which makes a lot of sense because it is a method or action that is very much tied to what it means to be a car
# - * there can be class methods and class attributes - methods and attributes for the blueprint, but you will mostly be working working with instance methods and instance variables
# - * there is also a concept of inheritance, which is a subclass, you might have say a civic class which is a subclass of car with a lot of the same functionality as car but with also some set specifics


#### EXAMPLE
class Human(object): # object means that this class inherits from the object class
  def __init__(self, clan=None):
    clan = 'CodingDojo'
    print "New Human!!!"     # when we create a new human, we'll get self as an output
                             # initialize the clan instance variable by passing in a value
    self.clan = clan
    # initialize more attributes that will be the same for all humans
    
    self.health = 100
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3

  def taunt(self):
    print "You want a piece of me?"

# create an instance of a human, pass in a clan name
michael = Human('CodingDojo')
jimmy = Human('CodingNinjas')

# #running an instance method on the instance michael
michael.taunt()
print michael.health
print michael.clan


# Human.taunt() #cannot do
Human.health #cannot do

# Human.myClassMethod
# Human.classVariable
# michael.myClassMethod # cannot do
