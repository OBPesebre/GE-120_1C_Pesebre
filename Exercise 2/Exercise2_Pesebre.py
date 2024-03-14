"""
GE 120
Omar Pesebre
2023-06343
Exercise 2
"""

#Sentinel controlled loop that asks for the distance of the line
counter = 1
lines = []

while True:
    print()
    print("LINE NO.", counter)

    beginnerin_ge = False
    while not(beginnerin_ge):
        distance = input("Distance: ")
        if beginnerin_ge:
            print("TRY AGAIN")
            continue
        if not(beginnerin_ge):
            break

    azimuth = input("Azimuth from the South: ")

    if "-" in azimuth:
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + int(minutes)/60 + (float(seconds)/3600))
        azimuth = round(azimuth,5)
    else:
        azimuth = float(azimuth)%360
   

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {} W' .format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {} W' .format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {} E' .format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {} E' .format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "NA"

    line = (counter, distance, bearing) #store tuple of a line
    lines.append(line)

#Ask user if he/she wants to create a new line
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("LINES")
print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

print("--------END--------")