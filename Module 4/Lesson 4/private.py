class myClass:

    __privateVAR = 27

    def __privMeth(self):
        print("Im inside class myClass")

    def hello(self):
        print("Private variable value: ", myClass.__privateVAR)

foo = myClass()
foo.hello()
# foo.__privMeth()
print(foo.__privateVAR)