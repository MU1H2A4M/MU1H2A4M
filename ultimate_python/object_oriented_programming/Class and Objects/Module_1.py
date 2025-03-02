class programmer:
    def __init__(self,name,salary,eid):
        self.name=name
        self.salary=salary
        self.eid=eid


    def display_info(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the employee id of the employee is {self.eid}")


p1=programmer("TAHA",55000,1221)
p2=programmer("MUDASSIR",50000,1211)
p3=programmer("JOHN",65000,1222)

programmer=[p1,p2,p3]

for p in programmer:
    p.display_info()
