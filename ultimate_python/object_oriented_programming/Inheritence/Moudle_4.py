class complex:
      def __init__(self,real,imag):
            self.real=real
            self.imag=imag
        
      def __add__(self,other):
            return complex(self.real+other.real , self.imag+other.imag)
      
      def __mul__(self,other):
            real_part=self.real*other.real-self.imag*other.imag
            imag_part=self.real*other.real+self.imag*other.imag
            return complex(real_part,imag_part)
      
      def __str__(self):
        return f"{self.real} + {self.imag}i"
  
            

c1=complex(4,7)
c2=complex(5,9)

sum_result=c1+c2
mul_result=c1*c2

print("the sum result of the " ,sum_result)
print("the mul result of the ",mul_result)