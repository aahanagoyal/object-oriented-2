class Rect:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def calculate_perimeter(self):
        return (self.length+self.breadth)*2
    

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
obj=Rect(l,b)
result=obj.calculate_perimeter()
print("Perimeter of Reactangle:",result)