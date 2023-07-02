import datetime
#EX 1
class Month:
    dictionary = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    def __init__(self, name: str = "January", monthNumber: int = 1):
        self.name = name
        self.monthNumber = monthNumber
    
    def __str__(self):
        return self.name + " " + str(self.monthNumber)

    def check(self):
        
        if self.monthNumber > 12:
            self.monthNumber -= 12
        elif self.monthNumber < 0:
            self.monthNumber += 12
        self.name = Month.dictionary[self.monthNumber]

    def __add__(self, other):
        self.monthNumber += other.monthNumber
        self.check()
        return self.name + " " + str(self.monthNumber)
    
    def __sub__(self, other):
        self.monthNumber -= other.monthNumber
        self.check()
        return self.name + " " + str(self.monthNumber)
        
print(Month("September",9)+Month("September",9))        
print(Month()-Month("September",9))


#EX 2
class Lecturer:
    dictionary = {
        "Cu nhan": 6.56,
        "Thac si": 6.92,
        "Tien si": 7.28,
        "Pho giao su": 7.64,
        "Giao su": 8.0
    }

    def __init__(self, code: str, name: str, dob: str, multi: float, level: str, min_wage: int):
        self.code = code
        self.name = name
        self.dob = dob
        self.multi = multi
        self.level = level
        self.min_wage = min_wage
        
    def __str__(self):
        return "Code: " + self.code + "\nName: " + self.name + "\nDate Of Birth" + self.dob + "\nSkill Level: " + self.level
    
    def wage(self):
        return f'{int(self.multi * self.min_wage):,}'
    
    def update_wage(self, other):
        
        if other in Lecturer.dictionary:
            self.multi = Lecturer.dictionary[other]
            
    def update_level(self, other):
        self.level = other
        self.update_wage(other)
            
class PrimaryLecturer(Lecturer):
    def __init__(self, code: str, name: str, dob: str, multi: float, level: str, min_wage: int, year_w: int, hour_w: int, reward: int):
        super().__init__(code, name, dob, multi, level, min_wage)
        self.year_w = year_w
        self.hour_w = hour_w
        self.reward = reward
        self.update_reward()
        self.update_multi()

    def wage(self):
        return f'{self.min_wage * self.multi + self.reward}'

    def update_reward(self):
        self.reward = self.min_wage * (self.year_w * 0.1 + self.hour_w * 0.05)
        
    def update_multi(self):
        add = self.hour_w // 42
        if self.multi + 0.2 * add < 15.6:
            self.multi += 0.2 * add
        
i = PrimaryLecturer("JHd", "Joe", "18.11", 0, "Giao su", 8, 12, 100, 0)
i.update_level("Giao su")
print(i.reward)