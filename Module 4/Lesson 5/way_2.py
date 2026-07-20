from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human():
    def move(self):
        print("I can walk and run")
class snake():
    def move(self):
        print("I can crawl")
class dog():
    def move(self):
        print("I can bark and run")
class lion():
    def move(self):
        print("I can roar and run")

obj_1 = human()
obj_2 = snake()
obj_3 = dog()
obj_4 = lion()

obj_1.move()
obj_2.move()
obj_3.move()
obj_4.move()