import random
import time
import json

from data.image_url import IMAGE_URL_LIST

WORD_LIST = ["Fly", "Sky", "Blue", "Green", "Sun", "Moon", "X", "Launch"]
STATUS_LIST = ["success", "fail"]



def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)

"""
FUNCTION FOR INSERT LAUNCH
"""

data = []
sql_cmd = "INSERT ALL\n"

for i in range(50):
    name = f"{random.choice(WORD_LIST)} {random.choice(WORD_LIST)} {i + 2}"
    date = str(random_date("2000/04/14", "2020/05/17", random.random()))
    status = random.choice(STATUS_LIST)
    image_url = random.choice(IMAGE_URL_LIST)
    space_shuttle_id = random.randint(21, 35)
    station_id = random.randint(1, 15)
    planet_id = random.randint(41, 55)
    obj = {"NAME": name, "DATE": date, "STATUS": status, "IMAGE_URL": image_url, 
           "SPACE_SHUTTLE_ID": space_shuttle_id, "STATION_ID": station_id, 
           "PLANET_ID": planet_id}
    data.append(obj)

random.shuffle(data)

for obj in data:
    name = obj["NAME"]
    date = obj["DATE"]
    status = obj["STATUS"]
    image_url = obj["IMAGE_URL"]
    space_shuttle_id = obj["SPACE_SHUTTLE_ID"]
    station_id = obj["STATION_ID"]
    planet_id = obj["PLANET_ID"]
    cmd = f"\tINTO LAUNCH(NAME, STATUS, LAUNCH_DATE, IMAGE_URL, SPACE_SHUTTLE_ID, STATION_ID, PLANET_ID) VALUES ('{name}', '{status}', TO_DATE('{date}', 'YYYY/MM/DD'), '{image_url}', {space_shuttle_id}, {station_id}, {planet_id})\n"
    sql_cmd += cmd

sql_cmd += "SELECT * FROM dual;"

with open("./json/launch.json", "w") as file:
    json_obj = json.dumps(data, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-launch-1.txt", "w") as file:
    file.write(sql_cmd)


