import bdb
from datetime import datetime, time, date

today = date.today()
birthday = date(2025, 10, 28)

if today > birthday:
    print("Your birthday is in the past this year.")
elif today < birthday:
    print("Your birthday is in the future this year.")
elif today == birthday:
    print("Happy Birthday!")
