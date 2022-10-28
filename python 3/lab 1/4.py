from datetime import datetime
class DateHandler():
    def __init__(self):
        pass

    def format_date(self, date: datetime):
        return date.strftime('%Y-%m-%d')

    def get_days_between(self, start_date, end_date):
        return (end_date - start_date).days

start_date = datetime(int(input("Start year: ")), int(input("Start month: ")), int(input("Start day: ")))
end_date = datetime(int(input("End year: ")), int(input("End month: ")), int(input("End day: ")))
print("Start:", DateHandler().format_date(start_date))
print("End:", DateHandler().format_date(end_date))
print("Days between:", DateHandler().get_days_between(start_date, end_date))


