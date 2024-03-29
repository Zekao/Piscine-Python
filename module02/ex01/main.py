def what_are_the_vars(*args, **kwargs):
    """
        @obj: an instance of a class that inherits from `ObjectC`
        we will create an enumerate of all the attributes in kwargs
        and after that we will create add each attribute to the obj instance
    """
    obj = ObjectC()
    for i, arg in enumerate(args):
        setattr(obj, "var_" + str(i), arg)
    for elem in kwargs:
        if hasattr(obj, elem):
            return None
    for key, value in kwargs.items():
        setattr(obj, key, value)
    return obj

# ... Your code here ...
class ObjectC(object):
    def __init__(self):
        pass
# ... Your code here ...
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)