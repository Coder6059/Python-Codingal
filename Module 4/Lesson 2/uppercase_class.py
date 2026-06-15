class string():

    def __init__(self):
        self.str1 = " "

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_string(self):
        print("The result is ", self.str1.upper())

ob1 = string()
ob1.get_string()
ob1.print_string()