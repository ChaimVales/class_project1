class Rectangle:
    def __init__(self,width,reight):
        self.width = width
        self.reight = reight
    
    def area(self):
        area =  self.width * self.reight
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.width + self.reight)
        return perimeter
    
    
