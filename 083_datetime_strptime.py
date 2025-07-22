dt1 = "2025-7-30"
dt2 = "8-14-2025"
dt2 = "2025, 8, 19"
dt2 = "8-14-2025"
dt3 = "2025, 8, 19"
dt4 = "10 30 - 20, 4, and 2026"
dt5 = "Meet me on 8th of 1st month, in 2027, at 11 hours, 35 minutes"

from datetime import datetime
datetime.strptime(dt1, "%Y-%m-%d")
datetime.datetime(2025, 7, 30, 0, 0)
dt1 = datetime.strptime(dt1, "%Y-%m-%d")
print(dt1)


datetime.strptime(dt2, "%m-%d-%Y")
datetime.datetime(2025, 8, 14, 0, 0)
dt2 = datetime.strptime(dt2, "%m-%d-%Y")
print(dt2)


dt3 = "2025, 8, 19"
dt3 = datetime.strptime(dt3, "%Y, %m, %d")
print(dt3)


dt4 = "10 30 - 20, 4, and 2026"
dt4 = datetime.strptime(dt4, "%H %M - %d, %m, and %Y")
print(dt4)


dt5 = "Meet me on 8th of 1st month, in 2027, at 11 hours, 35 minutes"
dt5 = datetime.strptime(dt5, "Meet me on %dth of %mst month, in %Y, at %H hours, %M minutes")
print(dt5)

dt6 = "9/30/2018 @ 7 hours and 30 minutes"
dt6 = datetime.strptime(dt6, "%m/%d/%Y @ %H hours and %M minutes")
print(dt6)

