from datetime import datetime
class CustomDate():
    def __init__(self):
        pass
        
    def get_date(self):
        return datetime.now().strftime("%d/%m/%Y")

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

now = CustomDate()
print(now.get_date())
print(now.get_time())
