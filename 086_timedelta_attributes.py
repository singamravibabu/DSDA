from datetime import timedelta, date, time, datetime

time_span = timedelta(weeks=2, days=3, hours=8, minutes=14)
print(time_span.days)

print(time_span.seconds)

print(time_span.microseconds)

print(time_span.total_seconds())
