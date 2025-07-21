cc_number = "4401-881022-88810"
cc_number = cc_number.replace("-", " ")
print(cc_number)

phone_number = "555-555-1234"
phone_number = phone_number.replace("-", "")
print(phone_number)

phone_number = "555-555-1234"
phone_number = phone_number.replace("-", "", 1)
print(phone_number)

phone_number = "(" + phone_number[0:3] + ")" + phone_number[3:]
print(phone_number)
