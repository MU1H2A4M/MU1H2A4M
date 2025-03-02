class employee:
    def __init__(self,name,e_id,salary):
        self.name=name
        self.e_id=e_id
        self.salary=salary
        self.increment=0.05

    def apply_increment(self):
        self.salary+=self.salary*self.increment

    def show_detail(self):
        return f"{self.salary} , {self.name}, {self.e_id}"

emp1=employee("Benjamin",230012,80000)
print(emp1.show_detail())

emp1.apply_increment()
print(emp1.show_detail())