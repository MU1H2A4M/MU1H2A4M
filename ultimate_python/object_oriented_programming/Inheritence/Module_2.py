class animal:
    def  __init__(self,name):
        self.name=name

    def show_name(self):
        return self.name
        
class pet(animal):
    def __init__(self,name,owner):
        super().__init__(name)
        self.owner=owner

    def show_owner(self):
        return self.owner

    
class dog(pet):
    def  __init__(self, name, owner,breed):
        super().__init__(name,owner)
        self.breed=breed

    def show_breed(self):
        return self.breed

    def bark(self):
            return f"{self.name} says: woof! woof!"


d=dog("buddy","christopher nolan","german shephered")

print(d.show_owner())
print(d.show_breed())
print(d.show_name())
print(d.bark())
