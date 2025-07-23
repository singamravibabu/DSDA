from datetime import datetime, date, time

today = date.today()
birthday = date(2025, 10, 28)

if birthday > today:
    days_until = (birthday - today).days
    print("Days until your birthday next year:", days_until)
