class Animal():
    # hàm khởi tạo Constructor
    def __init__(self, weight: float = 10, height: float = 10):
        self.weight = weight
        self.height = height

    # phương thức method
    def cat_weight(self):
        return self.weight

    def cat_height(self):
        return self.height

# if __name__ == "__main__":
#     cat = Animal(10, 5)
#     height = cat.cat_height()
#     print(height)
#     print(cat.height)

class Dog(Animal):
    def __init__(self, weight: float, height: float, breed: str):
        super().__init__(weight, height)
        self.breed = breed

    # ghi đè từ hàm cha
    def speak(self):
        print(self.breed)
        print("Woof woof.")

    def __str__(self) -> str:
        return str(self.weight) + " " + str(self.height) + " " + str(self.breed)

if __name__ == "__main__":
    dog = Dog(10, 10, "Pitbull")
    dog.speak()
    