class person(object):
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)

class employee(person):
    def __init__(self,name,id_number,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id_number)

a = employee("Rahul", 886012, 200000, "Intern")
a.display()