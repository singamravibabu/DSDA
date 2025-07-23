from datetime import date

today = date.today()

if today.month == 7 and today.day == 23:
    print("Today is the 23rd of July!")
else:
    print("Today is not the 23rd of July.")