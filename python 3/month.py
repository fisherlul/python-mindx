class Department():
    def __init__(self, name: str = "", teacherNum: int = 0) -> None:
        self.name = name
        self.teacherNum = teacherNum

    def __str__(self) -> str:
        return "Department: " + self.name + ", number of teachers: " + str(self.teacherNum)

    def setter_name(self, new_name):
        self.name = new_name

    def setter_name(self, new_number):
        self.teacherNum = new_number

    def getter_name(self):
        return self.name

    def getter_teacher_numbers(self):
        return self.teacherNum

# if __name__ == "__main__":
#     dep1 = Department("Maths", 10)
#     print(dep1)
#     dep1.teacherNum = 2
#     print(dep1)

class Faculty():
    #COMPOSITE: 

    # def __init__(self, dep_name1: str = "", dep_num1: int = 0, dep_name2: str = "", dep_num2: int = 0) -> None:
    #     self.depart1 = Department(dep_name1, dep_num1)
    #     self.depart2 = Department(dep_name2, dep_num2)
    
    def __init__(self, dep1 = Department(), dep2 = Department()) -> None:
        self.depart1 = dep1
        self.depart2 = dep2

depart1 = Department("Math", 10)
depart2 = Department("Litterature", 11)
faculty = Faculty(depart1, depart2)