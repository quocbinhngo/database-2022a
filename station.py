import random
import json

from generator import random_date

NAME_LIST = ["Kamubada", "Sakake", "Hierachy", "Emotional", "Tacatada", "Tika", "Saki", "Hie", "Namu", "Toko", "Kichi"]

data = []

for i in range(30):
    name = f"{random.choice(NAME_LIST)} {random.choice(NAME_LIST)} {i + 2}"
    date = random_date("1990/01/01", "2000/04/05", random.random())
    country_id = random.randint(1, 12)
    obj = {"NAME": name, "FOUNDED_DATE": date, "COUNTRY_ID": country_id}
    data.append(obj)

random.shuffle(data)

sql_cmd = "INSERT ALL\n"

for obj in data:
    name = obj["NAME"]
    date = obj["FOUNDED_DATE"]
    country_id = obj["COUNTRY_ID"]
    sql_cmd += f"\tINTO STATION(NAME, FOUNDED_DATE, COUNTRY_ID) VALUES ('{name}', TO_DATE('{date}', 'YYYY/MM/DD'), {country_id})\n"

sql_cmd += "SELECT * FROM dual;"

with open("./json/station.json", "w") as file:
    json_obj = json.dumps(data, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-station-1.txt", "w") as file:
    file.write(sql_cmd)
    