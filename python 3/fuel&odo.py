class FuelGauge():
    def __init__(self, fuel: float):
        self.fuel = fuel

    def __str__(self):
        return "Current fuel quant: " + str(self.fuel) + " gallons"

    def refuel(self):
        if self.fuel < 15:
            self.fuel += 1

    def consump(self):
        if self.fuel > 0:
            self.fuel -= 1

class Odometer():
    def __init__(self, mile: float, fuel: FuelGauge, count: int):
        self.mile = mile
        self.fuel = fuel
        self.count = count
        self.consumed()

    def __str__(self):
        return "Current miles: " + str(self.mile) 

    def move(self):
        self.count += 1
        self.consumed()
        if self.mile == 999999:
            self.mile = 0 
        else: 
            self.mile += 1
    
    def consumed(self):
        if self.count == 12:
            self.count == 0
            self.fuel.consump()

if __name__ == "__main__":
    fuel = FuelGauge(6)
    current = Odometer(12, fuel, 0)
    print(current, fuel)
    for i in range(13):
        current.move()
    print(current, fuel)
        