class Person():

    def __init__(self, name) -> None:
        self.name = name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)
