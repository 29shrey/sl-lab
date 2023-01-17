class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

    
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
a1 = Rectangle(l, b)
print("The area of rectangle is: ", a1.area())