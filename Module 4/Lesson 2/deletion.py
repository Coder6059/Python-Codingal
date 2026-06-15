class employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Employee destructed")

def create_obj():
    print("Creating object")
    obj = employee()
    print("Function end")
    return obj

print("Calling create_obj function")
create = create_obj()
print("Program end")
