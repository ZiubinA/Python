#Calculate the average temperature for Sensor "S1" only. You must skip any rows where the temperature is not a valid number.

raw_readings = [
    ["S1", 1700001, "23.5"],
    ["S2", 1700002, "24.1"],
    ["S1", 1700003, "ERR"],   
    ["S3", 1700004, "22.0"],
    ["S2", 1700005, "NULL"],  
    ["S1", 1700006, "23.9"],
    ["S3", 1700007, "22.5"]
]

average = 0
count = 0
for sensor in raw_readings:
    if sensor[0] == "S1":
        try:
            average += float(sensor[2])
            count += 1
        except:
            continue

print("average: ", average / count)