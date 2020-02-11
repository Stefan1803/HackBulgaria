import math

# filename = "sensors.txt"
filename = input("Filename: ")
radius = int(input("Neighbours distance: "))
max_error = int(input("Max error: "))

faulty_sensors = []
lines = []

with open(filename) as file:
    for line in file:
        (x, y, z) = line.strip().split(",")
        lines.append([int(x),int(y),int(z)])

current_sensor_list = lines
# print(current_sensor_list)

for current_sensor in current_sensor_list:
    lines.remove(current_sensor)
    other_sensors = lines
    for other_sensor in other_sensors:
        (x1, y1, value1) = current_sensor
        (x2, y2, value2) = other_sensor
        if abs(x1 - x2) <= radius and abs(y1 - y2) <= radius:
            # print("sensors are neighbours")
            # print(current_sensor)
            # print(other_sensor)
            if abs(value1 - value2) > max_error:
                faulty_sensors.append((x1, y1))
    # lines.insert(lines.index(current_sensor), current_sensor)
    lines.append(current_sensor)

if faulty_sensors == []:
    print("All sensors are OK.")
else:
    print("Please check sensors at:")
    print(faulty_sensors)
