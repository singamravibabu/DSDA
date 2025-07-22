quotation = "These are the times that try men's souls."
words = quotation.split()
print(words)

print(words[0])
print(words[1])
print(words[5])


date = "11/9/1995"
date = date.split("/")
print(date)

month = int(date[0])
day = int(date[1])
year = int(date[2])

print(year, day, month)


address = "Kiran Kumar|10-25 Malkajgiri|Hyderabad|Telangana|500047"
address = address.split("|")
print(address)
