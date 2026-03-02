class fun1():
    def __init__(self):
      self.str1=" "

    def enter(self):
       self.str1=input("Enter string:")
    
    def printfun(self):
       print("Result is:",self.str1.upper())

s1=fun1()
s1.enter()
s1.printfun()