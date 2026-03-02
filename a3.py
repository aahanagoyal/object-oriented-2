class Rect:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def calculate_area(self):
        return self.length*self.breadth
    

    
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
obj=Rect(l,b)
result=obj.calculate_area()
print("Area of Reactangle:",result)