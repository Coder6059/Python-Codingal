class parrot:
    species = "bird"
    
    def __init__(self, name,age):
        self.name = name
        self.age = age

ob1 = parrot("Blu", 10)
ob2  = parrot("Woo", 15)

print("The first parrot is a ", ob1.species)
print("The second parrot is a ", ob2.species)

print(ob1.name, "is", ob1.age, "years old")
print(ob2.name, "is", ob2.age, "years old")