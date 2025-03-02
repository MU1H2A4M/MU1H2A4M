class two_d_vector:
   def  __init__(self,x,y):
      self.x=x
      self.y=y

   def magnitude(self):
         return (self.x**2 + self.y**2) **0.5
      
   def add(self):
         return (self.x+self.y)


class three_d_vector(two_d_vector):
   def  __init__(self,x,y,z):
      super().__init__(x,y)
      self.z=z
      
   def magnitude(self):
         return(self.x**2 + self.y**2 + self.z**2)**0.5
      
   def add(self):
         return(self.x+self.y+self.z)
      

v2 = two_d_vector(2, 4)
print(f"The magnitude of the 2D vector is {v2.magnitude()}")  
print(f"The sum of components in 2D vector is {v2.add()}")

v3 = three_d_vector(2, 4, 6)
print(f"The magnitude of the 3D vector is {v3.magnitude()}")
print(f"The sum of components in 3D vector is {v3.add()}")



         