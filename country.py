import json

COUNTRY_LIST = ['United Kingdom', "USA", "Australia", "Vietnam", "China", "Germany", "France", "Russia", "Canada", "Ukraine", "Thailand", "Singapore"]

sql_cmd = "INSERT ALL\n"

for country in COUNTRY_LIST:
    sql_cmd += f"\tINTO COUNTRY(NAME) VALUES ('{country}')\n"

sql_cmd += "SELECT * FROM dual;"

with open("./json/country.json", "w") as file:
    json_obj = json.dumps(COUNTRY_LIST, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-country-1.txt", "w") as file:
    file.write(sql_cmd)
