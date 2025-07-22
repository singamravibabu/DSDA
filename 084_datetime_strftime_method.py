from datetime import datetime

dt1 = datetime.datetime(2025, 7, 30, 0, 0)
dt2 = datetime.datetime(2025, 8, 14, 0, 0)
dt3 = datetime.datetime(2025, 8, 19, 0, 0)
dt4 = datetime.datetime(2026, 4, 20, 10, 30)
dt5 = datetime.datetime(2027, 1, 8, 11, 35)
dt6 = datetime.datetime(2027, 1, 8, 11, 35)

print(dt1.strftime("%B %d, %Y (%A)"))
print(dt2.strftime("%Y-%m-%d (%a)"))
print(dt3.strftime("%A - %B %d, %Y"))
print(dt3.strftime("%a - %b %d, %Y"))
print(dt4.strftime("Morning at %H hours, and %M minutes, Lets meet on %Y year, on %B %d"))
print(dt5.strftime("At %H:%M on %B %d, %Y"))
print(dt6.strftime("%Y-%m-%d - %H:%M"))
print(dt6.strftime("%Y-%m-%d - %H:%M %p"))


