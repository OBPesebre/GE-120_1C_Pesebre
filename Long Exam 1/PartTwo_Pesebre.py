"""

My pseudocode:
1. Printing a title - Print(name and description)
2. Initialize variables
3. Ask for the initial BM elevation using float(data)
4. Creating a while loop
    - Backsight and foresight measurements
    - Height of instrument computation using addition
    - Compute for new running elevation using subtraction
    - Add the total distance
    - Print in a levelling table using tuple
5. Ask the user if he/she wants to create a line - Use if, else if, else
"""

from math import sqrt

#Printing a title
print("OMAR B. PESEBRE. This is entitled Leveling Computations as it computes and summarizes the levelling data obtained by geodetic engineers.")

#Initializing the variables

tp_counter = 1
lines = []
total_distance = 0

#Creating a function

def floatInput(prompt):
    '''
    Convert all output to float data type.

    Input:
    prompt - string

    Output
    converted prompt - float
    '''

    floatPrompt = float(prompt)
    
    return floatPrompt


#Ask for the initial elevation of BM1
initial_elevation = floatInput(input("What is the initial elevation of BM1? "))

# create a while loop

print()
print("TP", tp_counter)

foresight = round(floatInput(input("Foresight Reading (m): ")), 3)
backsight = round(floatInput(input("Backsight Reading (m): ")), 3)
distance_between_turning_points = floatInput(input("Distance between turning points (m): "))
elevation = initial_elevation
height_of_instrument = initial_elevation + backsight

while True:
    print()
    print("TP", tp_counter + 1)

    foresight = round(floatInput(input("Foresight Reading (m): ")), 3)
    backsight = round(floatInput(input("Backsight Reading (m): ")), 3)
    distance_between_turning_points = floatInput(input("Distance between turning points (m): "))

    elevation = height_of_instrument - foresight
    height_of_instrument = elevation + backsight

    levelling_table = (tp_counter, backsight, height_of_instrument, foresight, elevation) #store tuple of a line
    lines.append(levelling_table)

    # Ask user if he/she wants to create a new line
    yn = input("Add new station? ")
    if yn == "Y":
        tp_counter = tp_counter + 1
        continue
    elif yn == "n":
        break
    else:
        print("error")

print("LEVELLING TABLE")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("Sta.", "B.S.", "H.I.", "F.S.", "Elev."))

for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], line[3], line[4]))

total_distance += distance_between_turning_points
print("Total Distance of the Circuit: ", total_distance)

error = elevation - initial_elevation
print("Error:", error)

error_in_mm = error *  1000

total_distance_in_km = total_distance / 1000

print ("Relative error: 1/ ", relative_error_denominator)

if error_in_mm>= 4.80 * (sqrt(total_distance_in_km)):
    print("Accuracy: FIRST ORDER")
elif error_in_mm < 4.80 * (sqrt(total_distance_in_km)) and error_in_mm >= 8.40 * (sqrt(total_distance_in_km)):
    print("Accuracy: SECOND ORDER")
elif error_in_mm < 8.40 * (sqrt(total_distance_in_km)) and error_in_mm >= 12 * (sqrt(total_distance_in_km)):
    print("Accuracy: SECOND ORDER")
else:
    print("Accuracy: ERROR TOO LARGE")