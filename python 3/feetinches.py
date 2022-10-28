from http.client import NETWORK_AUTHENTICATION_REQUIRED


class FeetInches():
    def __init__(self, feet: int, inches: int): 
        self.feet = feet
        self.inches = inches
        self.simplify()

    def __str__(self):
        return str(self.feet) + " feet " + str(self.inches)

    def simplify(self): 
        converted = self.feet * 12 + self.inches
        self.inches = converted % 12
        self.feet = converted // 12

    def __add__(self, other):
        feet_cal = self.feet + other.feet
        inches_cal = self.inches + other.inches
        return FeetInches(feet_cal, inches_cal)

    def __eq__(self, value: object):
        return value.feet == self.feet and value.inches == self.inches

    def multiply(self, other):
        feet_cal = self.feet * other.feet
        inches_cal = self.inches * other.inches
        return FeetInches(feet_cal, inches_cal)

if __name__ == "__main__":
    print(FeetInches(5,3) == FeetInches(4, 2))