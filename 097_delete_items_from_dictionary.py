countries = {
    "IND": "India",
    "USA": "United States of America",
    "CAN": "Canada",
    "MEX": "Mexico",
    "GBR": "United Kingdom",
    "FRA": "France",
    "DEU": "Germany",
    "ITA": "Italy"
}

del countries["ITA"]
print("After deleting Italy", countries)
print()

item_value = countries.pop("FRA")
print("After popping France", countries)
print("Popped value:", item_value)
print()

countries.clear()
print("After clearing all items", countries)
