from datetime import date, time, datetime, timedelta

three_weeks = timedelta(weeks=3)
print(three_weeks)

two_hours_thirty_minutes = timedelta(hours=3, minutes=30)
print(two_hours_thirty_minutes)

time_span = timedelta(weeks=2, days=3, hours=8, minutes=14)
print(time_span)

three_weeks_from_today = date.today() + three_weeks
print(three_weeks_from_today)

three_weeks_ago = date.today() - three_weeks
print(three_weeks_ago)

three_hours_from_now = datetime.now() + timedelta(hours=3)
print(three_hours_from_now)
