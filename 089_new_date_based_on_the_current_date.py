from datetime import date, datetime

today = date.today()
last_year = today.year - 1

one_year_ago = date(last_year, today.month, today.day)
print(f"Today's date: {today}")
print(f"Date one year ago: {one_year_ago}")


now = datetime.now()

this_time_next_year = datetime(now.year + 1, 
                            now.month, now.day,
                            now.hour, now.minute, now.second)

print(f"Current time: {now}")
print(f"Same time next year: {this_time_next_year}")