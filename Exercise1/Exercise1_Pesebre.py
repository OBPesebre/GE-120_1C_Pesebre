"""
GE 120
Omar Pesebre
2023-06343
Exercise 1
"""

dd = float(input("Provide the dd: "))

# get the degree part
degree = int(dd)

#print("DEGREE:", degree)

# get the minutes
minutes = (dd - degree) * 60
minutes_fractional = int(minutes)
#print("MINUTES", minutes)

# get the seconds
seconds = (minutes - minutes_fractional) * 60
#print("SECONDS", seconds)

print("DMS: " + str(degree) + "-" + str(minutes_fractional) + "-" + str(round(seconds,2)))

# convert dms to dd

dms = (input("Provide the dms: "))
values = dms.split("-")

#print("list: ", values)

#get the degrees
degrees = int(values[0])

#get the minutes
minutes = int(values[1])

#get the seconds
seconds = float(values[2])

#combine degrees, minutes, and seconds
dd = degrees + (minutes/60) + (seconds/3600)

print("Converted to DD: ", round(dd,5))