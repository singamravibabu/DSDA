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

print(countries.get("CAN"))
print(countries.get("ESP", "Country not found"))
