class dog_breed:

    colour = "brown"
    
    def __init__(self, breed, size, price, age):
        self.breed = breed
        self.size = size
        self.price = price
        self.age = age

ob1 = dog_breed("Golden Retriever", "Medium", 1000, 3)
ob2 = dog_breed("Poodle", "Small", 500, 1)

print("The first dog's breed is ", ob1.breed, ", its size is ", ob1.size, ", it costs ", ob1.price, ", and is ", ob1.age, "year(s) old")
print("The second dog's breed is ", ob2.breed, ", its size is ", ob2.size, ", it costs ", ob2.price, ", and is ", ob2.age, "year(s) old")   