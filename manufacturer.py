import json
import time
import random

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)

with open("./json/manufacturer.json", "r") as file:
    data = json.load(file)

for obj in data:
    obj["NAME"] =  obj["NAME"].upper()
    obj["FOUNDED_DATE"] = random_date("1990/01/01", "2000/02/03", random.random())
    obj["COUNTRY_ID"] = random.randint(1, 12)

sql_cmd = "INSERT ALL\n"

for manu in data:
    name = manu["NAME"]
    website_url = manu["WEBSITE_URL"]
    founded_date = manu["FOUNDED_DATE"]
    country_id = manu["COUNTRY_ID"]
    sql_cmd += f"\tINTO MANUFACTURER(NAME, WEBSITE_URL, FOUNDED_DATE, COUNTRY_ID) VALUES ('{name}', '{website_url}', TO_DATE('{founded_date}', 'YYYY/MM/DD'),  {country_id})\n"

sql_cmd += "SELECT * FROM dual;"

with open("./json/manufacturer.json", "w") as file:
    json_obj = json.dumps(data, indent=4)
    file.write(json_obj)

with open("./sql-cmd/insert-manufacturer-1.txt", "w") as file:
    file.write(sql_cmd)