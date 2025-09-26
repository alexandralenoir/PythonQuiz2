class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        return self.__age
    
    def get_role(self):
        return "Person"
    
    def print_role(self):
        print(f"{self.name} is my {self.get_role()} who's age is {self.get_age()} years old.")

class Me(Person):
    def __init__(self, name, age, car):
        super().__init__(name, age)
        self.car = car

    def get_role(self):
        return "name"
    
class Brother(Person):
    def __init__(self, name, age, instrument):
        super().__init__(name, age)
        self.instrument = instrument

    def get_role(self):
        return "Brother"
    

me = Me("Alex", 18, "1993 Buick Roadmaster.")
brother = Brother("Mason", 16, "piano.")

print(f"I own a {me.car}")
print(f"Mason loves music and plays the {brother.instrument}")
      
print(me.get_role())
print(brother.get_role())

me.print_role()
brother.print_role()

# my terminal on vs studio code is not working correctly so I ran it through github to make sure it worked.
# I also had issues getting the code to transfer over in the file when creating the repository so I had to copy and paste it to this.
