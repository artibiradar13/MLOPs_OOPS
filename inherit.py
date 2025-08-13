#base class-parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create Dog object
d = Dog()
d.speak()  # From parent class
d.bark()   # From child class

## TYPES OF INHERITANCE
#Single Inheritance – One child inherits from one parent.
# -------above example

#Multiple Inheritance – One child inherits from multiple parents.
class Father:
    def skills(self):
        print("Car driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Father’s skill (first in MRO)

#Multilevel Inheritance – A class inherits from a child of another class.
class Grandparent:
    def legacy(self):
        print("Land and House")

class Parent(Grandparent):
    def guidance(self):
        print("Life lessons")

class Child(Parent):
    def dreams(self):
        print("Start a company")

c = Child()
c.legacy()
c.guidance()
c.dreams()



#overriding Parent Methods------
# A Child can replace a parent's method by definig it again---
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):  #defining again
        print("Bark bark")

d = Dog()
d.speak()


#super() is used to call methods from the parent class without explicitly naming it.


#Hierarchical Inheritance – Multiple children inherit from the same parent.

#Hybrid Inheritance – Combination of the above.



