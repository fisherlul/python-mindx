class Solution:
    def dayOfTheWeek(day: int, month: int, year: int):
        import datetime as d
        day_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
        4: "Friday", 5: "Saturday", 6: "Sunday"}
        dateTimeInstance = d.datetime(year, month, day, 00, 00, 00)
        return day_dict.get(dateTimeInstance.weekday())

print(Solution.dayOfTheWeek(24, 7, 2022))