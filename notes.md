#Problem : Downloads -> ALL Files (png , jpeg : Images , docs , pdf :Documents)
# Misorganised Downloads Folder

#Solution : Agent that can organise the files in the downloads folder and also able to check their type when I download a file and move it to the correct folder

#OOPS Concepts :

#Class : Structure , No real world instantiation
#Object : Real World Entity
#Enscapulation : Hiding data + methods together and controlling access to it
class BankAccount:
    def __init__(self):
        self.__balance = 0 #Private Variable
        
    def get_balance(self):
        return self.__balance #Getter Method to provide access of private variable(__balance) to outside class and methods
    
#Inheritance : Reusing properties and behaviors of a parent class in a child class (code -> Parent , child -> code resue)
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self): -> Method signature
        return "Meow!"-> Method implementation
    
#Abstraction : Hiding complex implementation details and showing only the necessary features to the user

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 
    
    #behavior : method
    #attribute : variable
    
#Polymorphism : Ability of an object to take many forms (method overloading , method overriding)
Method overloading : Same method name but different parameters (not supported in Python)
**kargs , *args 

Mehtod overrriding : Same method name and same parameters but different implementation in child class (supported in Python)


#Supporting concepts :
#Constructor : Special method used to initialize objects 
# (in Python : __init__) 

class Example:
    
    def instance_method(self):
        print("This is an instance method.")
        print("It can access instance variables and other instance methods.")
        print("It works on objects of the class.")
        
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print("It can access class variables and other class methods.")
        print("It works on the class itself, not on instances.")
    
    @staticmethod
    def static_method():
        print("This is a static method.")
        print("It cannot access instance variables or class variables")
        print("It works independently of any class or instance")
        
    # Composition : A design principle where a class is composed of one or more objects of other classes, rather than inheriting from them (has-a relationship)
    class Engine:
        pass 
    
    class Car:
        def __init__(self):
            self.engine = Engine() #Car has an Engine (Composition)
            
    #Aggregation : A special form of composition where the contained objects can exist independently of the container (has-a relationship but with weaker coupling)
    class Department:
        pass
    
    class University:
        def __init__(self):
            self.department = Department() #University has a Department (Aggregation)
            
    Access Modifier : Enscapulation concept that controls the visibility and accessibility of class members (variables and methods) to outside code (public , private , protected)
    
    Public : balance = 1000 (Accessible from anywhere)
    Private : __balance = 1000 (Accessible only within the class)
    Protected : _balance = 1000 (Accessible within the class and its subclasses)
    
    # -> Getter and Setter Methods : Methods used to access and modify private variables (getters to retrieve value , setters to set value)