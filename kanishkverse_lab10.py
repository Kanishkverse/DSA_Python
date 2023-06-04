"""from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self,species,height):
        self.species = species
        self.height = height



    @abstractmethod
    def print_height(self):
        pass


class dog(Animal):
    def print_height(self):
        print("10")

obj1 = dog("dog",10)
obj1.print_height()
*/
"""

#Question of the lab session
from abc import ABC, abstractmethod
class Shape(ABC):
   @abstractmethod #calling abstract method for area with return 0
   def area(self):
      return 0
class Rectangle(Shape):
   def __init__(self, length,breadth):
      self.l = length
      self.b=breadth

   def area(self): # again calling area but with l,b
      return self.l*self.b
#Testing the code
rect = Rectangle(6,7)
print ('area of the rectangle: ',rect.area())