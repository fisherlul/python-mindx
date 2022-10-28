class Employee():
    def __init__(self, name: str, position: str = ""):
        self.name = name
        self.position = position

    def say_hi(self):
        print(f"Hi, my name is {self.name}")
    def tell_position(self):
        print(f"I am a {self.position}")

if __name__ == "__main__":
    fullname = Employee(input("Input your name: "), input("Input your position: "))
    fullname.say_hi()
    fullname.tell_position()