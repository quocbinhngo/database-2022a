import random
import json

from generator import random_date

NAME_LIST = ["Mars", "Jupyter", "Radio", "Kepla", "Saturn", "Mercury"]

data = []

for i in range(30):
    name = f"{random.choice(NAME_LIST)} {i + 2}"
    perihelion = random.randint(1e6, 1e7)
    arphelion = random.randint(1e10, 1e11)
    semi_major_axis = random.randint(1e8, 1e9)
    obj = {"NAME": name, "PERIHELION": perihelion, "ARPHELION": arphelion, "SEMI_MAJOR_AXIS": semi_major_axis}
    data.append(obj)

random.shuffle(data)

sql_cmd = "INSERT ALL\n"

for obj in data:
    name = obj["NAME"]
    perihelion = obj["PERIHELION"]
    arphelion = obj["ARPHELION"]
    semi_major_axis = obj["SEMI_MAJOR_AXIS"]
    sql_cmd += f"\tINTO PLANET(NAME, PERIHELION, ARPHELION, SEMI_MAJOR_AXIS) VALUES ('{name}', {perihelion}, {arphelion}, {semi_major_axis})\n"

sql_cmd += "SELECT * FROM dual;"

with open("./json/planet.json", "w") as file:
    json_obj = json.dumps(data, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-planet-1.txt", "w") as file:
    file.write(sql_cmd)
    