from datetime import datetime

# Ex 1
from operator import le, length_hint


class Rectangle():
    def __init__(self, height: float, width: float): 
        self.height = height
        self.width = width
    
    def __str__(self):
        return 'Rectangle object with height = ' + str(self.height) + " and width = " + str(self.width)

rect = Rectangle(2, 1)
print(rect.__str__())

# Ex 2
class MathList():
    def __init__(self, values: list):
        self.values = values
        
    def __add__(self, other):
        temp = MathList([])
        for num in self.values:
            temp.values.append(num + other)
        return temp

    def __str__(self):
        return str(self.values)


math1 = MathList([1, 2, 3, 4, 5])
print(math1)

math2 = math1 + 2
print(math2)

# Ex 3
class Square():
    def __init__(self, length: float):
        self.length = length

    def cal_area(self):
        return (self.length)**2

class Cube(Square):
    def __init__(self, length: float):
        super().__init__(length)

    def cal_area(self):
        return (self.length)**2 * 6

    def cal_volume(self):
        return (self.length)**3

sqr = Square(2)
print('Square area:', sqr.cal_area())

cube = Cube(4)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())

# Ex 4
class User():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def welcome(self):
        print(f"Welcome {self.username}")

    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False

class SubscribedUser(User):
    def __init__(self, username: str, password: str, date: datetime):
        super().__init__(username, password)
        self.date = date

    def is_expired(self):
        if datetime.today() >= self.date:
            return True
        else:
            return False

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2023, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())