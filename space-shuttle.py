import random
import json

from generator import random_date

WORD_LIST = ["Discovery", "Exploration", "New", "World", "Space", "Galaxy", "Travel", "Learn", "Experiment", "Build", "Research"]

data = []

for i in range(20):
    name = f"{random.choice(WORD_LIST)} {random.choice(WORD_LIST)} {i + 2}"
    date = random_date("1990/01/01", "2000/04/05", random.random())
    manufacturer_id = random.randint(1, 9)
    obj = {"NAME": name, "MANUFACTURED_DATE": date, "MANUFACTURER_ID": manufacturer_id}
    data.append(obj)

random.shuffle(data)

sql_cmd = "INSERT ALL\n"

for obj in data:
    name = obj["NAME"]
    date = obj["MANUFACTURED_DATE"]
    manufacturer_id = obj["MANUFACTURER_ID"]
    sql_cmd += f"\tINTO SPACE_SHUTTLE(NAME, MANUFACTURED_DATE, MANUFACTURER_ID) VALUES ('{name}', TO_DATE('{date}', 'YYYY/MM/DD'), {manufacturer_id})\n"

sql_cmd += "SELECT * FROM dual;"

with open("./json/space-shuttle.json", "w") as file:
    json_obj = json.dumps(data, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-space-shuttle-1.txt", "w") as file:
    file.write(sql_cmd)
