#Lab Quiz done by Kanishk
#Done on Wed Nov 9, 2022 

def main():


    class Polygon:
        def __init__(self, sides):
            self.sides = sides

        def perimeter(self):
            
            return sum(self.sides)

        
            
            

    class Triangle(Polygon):
        def __init__(self, sides):
            
            assert len(sides) == 3
            self.sides = sides
        def display(self):
            print("A triangle is a polygon with 3 edges")
    class Rectangle(Polygon):
        def __init__(self, sides):
            assert len(sides) == 4
            self.sides = sides       
        def display(self):
            print("A Quadrilateral is a polygon with 4 sides")

    t1 = Triangle([5, 6, 7])
    print("Perimeter of a Triangle:", t1.perimeter())
        
    t2 = Rectangle([5,6,7,9]) 
    print("Perimeter of a",t2.perimeter())    
    t1.display()

    t2.display()




if __name__ =="__main__":
    main()
