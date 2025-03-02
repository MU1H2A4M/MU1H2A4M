import  math

class calculator:
      def __init__(self,num):
        self.num=num

      def square(self):
        return self.num * self.num
        
      def cube(self):
        return self.num * self.num * self.num
        
      def square_root(self):
        return self.num**0.5
      
      @staticmethod
      def greet():
         print("welcome!")



calculator.greet()
num=4
cal=calculator(num)

print(f"Square of {num}: {cal.square()}")
print(f"Cube of {num}: {cal.cube()}")
print(f"squre root of {num}:{cal.square_root()}")




