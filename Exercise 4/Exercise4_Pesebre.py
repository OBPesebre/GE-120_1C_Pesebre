"""
GE 120
Omar Pesebre
2023-06343
Exercise 4
"""

from math import cos, sin, radians, sqrt, atan, floor

class Line:

    def __init__(self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth
    
    def latitude(self):
        '''
        Determines the latitude of a line

        Input:
        distance - float
        azimuth - float

        Output
        latitude - float
        '''
        
        latitude = -float(self.distance)*cos(radians(self.azimuth))

        return latitude

    def departure(self):
        '''
        Determines the departure of a line

        Input:
        distance - float
        azimuth - float

        Output
        departure - float
        '''

        departure = -float(self.distance)*sin(radians(self.azimuth))
        
        return departure

    def bearing(self):
        '''
        Determines the DMS bearing of a line

        Input:
        azimuth - float

        Output
        bearing - string
        '''

        if azimuth > 0 and azimuth < 90:
            bearing = 'S {} W' .format(azimuth)
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {} W' .format(180 - azimuth)
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {} E' .format(azimuth - 180)
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {} E' .format(360 - azimuth)
        else:
            bearing = "NA"

        return bearing

class Cardinal(Line):
    def __init__(self,distance,azimuth):
        super().__init__(distance,azimuth)
    
    def bearing(self):
        if azimuth == 0:
            bearing = "DUE SOUTH"
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 180:
            bearing = "DUE NORTH"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "NA"
        return bearing


counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0


while True:
    print()
    print("LINE NO.", counter)

    beginnerin_ge = False
    while not(beginnerin_ge):
        distance = float(input("Distance: "))
        if beginnerin_ge:
            print("TRY AGAIN")
            continue
        if not(beginnerin_ge):
            break

    azimuth = input("Azimuth from the South: ")
    if "-" in str(azimuth): #if user provided DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees)) + (int(minutes)/60) + (float(seconds)/3600)%360
    else: #if user gives DD
        azimuth = float(azimuth)%360
    
    if azimuth % 90 == 0:
        line = Cardinal(distance,azimuth)
    else:
        line = Line(distance,azimuth)
   
    sumLat += line.latitude()
    sumDep += line.departure()
    sumDist += float(line.distance)

    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

#Ask user if he/she wants to create a new line
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("LINES")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], round(line[3],3), round(line[4],3)))


#get the sum of lat, dep, and distance

print("SUMMATION OF LAT:", sumLat)
print("SUMMATION OF DEP:", sumDep)
print("SUMMATION OF DIST:", sumDist)

#get the LEC, REC, BOSE
lec = sqrt((sumLat ** 2) + (sumDep ** 2))
print("LEC:", lec)

rec_denominator_orig = (sumDist/lec)
rec_denominator_orig = int(rec_denominator_orig)
rec_denominator_final = len(str(rec_denominator_orig))

if rec_denominator_final <= 2:
    print("REC: 1:", rec_denominator_orig)
else:
    highest_digit = rec_denominator_orig / (10 ** (rec_denominator_final - 2))
    result = floor(highest_digit)
    final = str(result) + ("0" + (rec_denominator_final - 2))
    print("REC: 1:", final)


BOSE = float(atan(abs(sumDep)/abs(sumLat)))

if sumLat > 0 and sumDep > 0:
    boSe = 'S {} W' .format(BOSE)
elif sumLat < 0 and sumDep > 0:
    boSe = 'N {} W' .format(BOSE)
elif sumLat < 0 and sumDep < 0:
    boSe = 'N {} E' .format(BOSE)
elif sumLat > 0 and sumDep < 0:
    boSe = 'S {} E' .format(BOSE)
else:
    boSe = "NA"

print("BoSE:", boSe)

#get the cLat, cDep, adjLat, adjDep
constCorrLat = -sumLat/sumDist
constCorrDep = -sumDep/sumDist


print('{: ^10} {: ^10} {: ^10}'.format("LINE NO."," ADJUSTED LATITUDE", "ADJUSTED DEPARTURE"))
for line in lines:
    corr_lat = constCorrLat * line [1]
    corr_dep = constCorrDep * line [1]

    adjLat = line [3] + corr_lat
    adjDep = line [4] + corr_dep
    print('{: ^10} {: ^20} {: ^15}'.format(line[0], round(adjLat,7), round(adjDep,7)))
    
print("ADJUSTED LINES:")
print('{: ^10} {: ^10} {: ^10}'.format("LINE NO."," ADJUSTED DISTANCE", "ADJUSTED BEARING"))
for line in lines:
    corr_lat = constCorrLat * line [1]
    corr_dep = constCorrDep * line [1]

    adjLat = line [3] + corr_lat
    adjDep = line [4] + corr_dep

# #Obtain the adjusted distance and bearing
    adjDist = round(sqrt((adjLat ** 2) + (adjDep ** 2)), 3)
    adj_bearing = round(float(atan(abs(adjDep)/abs(adjLat))), 3)
    if adjLat > 0 and adjDep > 0:
        adjBearing = 'N {} E' .format(adj_bearing)
    elif adjLat < 0 and adjDep > 0:
        adjBearing = 'S {} E' .format(adj_bearing)
    elif adjLat < 0 and adjDep < 0:
        adjBearing = 'S {} W' .format(adj_bearing)
    elif adjLat > 0 and adjDep < 0:
        adjBearing = 'N {} W' .format(adj_bearing)
    else:
        adjBearing = "NA"
    
    print('{: ^10} {: ^17} {: ^17}'.format(line[0], adjDist, adjBearing))

print("--------END--------")