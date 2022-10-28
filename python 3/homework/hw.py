import datetime
#EX 1
class Month():
    def __init__(self, name: str = "January", monthNumber: int = 1):
        self.name = name
        self.monthNumber = monthNumber

    def monthNum(self):
        if self.monthNumber == 1:
            self.name = "January"
        elif self.monthNumber == 2:
            self.name = "February"
        elif self.monthNumber == 3:
            self.name = "March"
        elif self.monthNumber == 4:
            self.name = "April"
        elif self.monthNumber == 5:
            self.name = "May"
        elif self.monthNumber == 6:
            self.name = "June"
        elif self.monthNumber == 7:
            self.name = "July"
        elif self.monthNumber == 8:
            self.name = "August"
        elif self.monthNumber == 9:
            self.name = "September"
        elif self.monthNumber == 10:
            self.name = "October"
        elif self.monthNumber == 11:
            self.name = "November"
        elif self.monthNumber == 12:
            self.name = "December"

    def monNames(self):
        if self.name == "January":
            self.monthNumber == 1
        elif self.name == "February":
            self.monthNumber == 2
        elif self.name == "March":
            self.monthNumber == 3
        elif self.name == "April":
            self.monthNumber == 4
        elif self.name == "May":
            self.monthNumber == 5
        elif self.name == "June":
            self.monthNumber == 6
        elif self.name == "July":
            self.monthNumber == 7
        elif self.name == "August":
            self.monthNumber == 8
        elif self.name == "September":
            self.monthNumber == 9
        elif self.name == "October":
            self.monthNumber == 10
        elif self.name == "November":
            self.monthNumber == 11
        elif self.name == "December":
            self.monthNumber == 12

    def aYear(self):
        if self.monthNumber >= 13:
            self.monthNumber -= 12

    def almostAyear(self):
        if self.monthNumber <= 0:
            self.monthNumber += 12

    def __str__(self):
        return "Month number: " + str(self.monthNumber) + " , month name: " + self.name

#EX 2
class Teachers():
    def __init__(self, id: str, name: str, birthDate: datetime, salary: float, experience: str, basic_salary: int):
        self.id = id
        self.name = name
        self.birthDate = birthDate
        self.salary = salary
        self.experience = experience
        self.basic_salary = basic_salary

    def __str__(self):
        return "Name: " + self.name + " ,birth date: " + self.birthDate + " ,id: " + str(self.id) + " ,experience: " + self.experience
    
    def __mul__(self):
        self.basic_salary *= self.salary

    def salaryLevel(self):
        if self.experience == "Bachelor":
            self.salary == 6.56
        elif self.experience == "Master":
            self.salary == 6.92
        elif self.experience == "Doctor":
            self.salary == 7.28 
        elif self.experience == "Asc.Professor":
            self.salary == 7.64
        elif self.experience == "Professor":
            self.salary == 8