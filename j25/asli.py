class Say:
    x = 5
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Hello")
    @staticmethod
    def isAdult(age):
        if age > 18:
            print("yes")
        else:
            print("no")

