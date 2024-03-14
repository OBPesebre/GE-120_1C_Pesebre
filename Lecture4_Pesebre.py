#FUNCIONS uphold the DRY principle

# print("Hello World")


# a=1
# b=str(a)
# print(type(b))

#Defining own functions
# def shout(word):
#         print(word + "!")
#         print("I created this function")



# shout("OMAR")
# shout("BEN 10")
# shout("DC")

# def shout():
#         print(word + "!")

# word = "HELLO"

# shout()

# def shout(word1, num_ulitin_last_letter):
#     '''
#     Description of the function
#     Argument meaning / What type of data
#     Ano yung return

#     '''
#     print:(word1.upper()+word1[-1].upper()*(num_ulitin_last_letter-1)+"!!!!!")
#     # print(list_of_names)

# shout("Mafe",5)

# help(shout)

# def convertDMStoDEG(name ="Omar", dms="61-30-19"):
#     '''
#     Convert DMS to degrees

#     Arguments:
#         dms - string
    
#     '''

#     degrees, minutes, seconds = dms.split("-")
#     dd = degrees + (minutes/60) + (seconds/3600)
#     print(name + ", ETO YUNG VALUE:", round(dd,6))
#     return round(dd,6)

# def print_as_table(*lines):
#     print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))

#     for line in lines:
#         print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

# line1 =(1, '112.13', 'N     30.0    E')


def getDirection(degrees):
    '''
    Gives the quadrant of an angle

    Input:
    degrees - float

    Output
    quadrant - string
    '''

    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 0 and degrees < 180:
        return "NW"
    elif degrees > 0 and degrees < 270:
        return "NE"
    elif degrees > 0 and degrees < 360:
        return "SE"
    else:
        return "ERROR"

    print("HELLO")

direction = getDirection(100)
print(direction)

