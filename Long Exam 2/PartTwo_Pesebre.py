class Parcel:

    def __init__(self, owner, area):
        self.owner = owner
        self.area = area
    
    def getClassification(self):
        '''
        It determines the type of parcel.

        Input:
        Size of the lot - integer

        Output:
        Type of parcel - string
        '''
        if self.area < 10000:
            classification = "Residential"
        elif self.area > 10000 and self.area < 120000:
            classification = "Private Agricultural"
        else:
            classification = "Public Agricultural"

        return classification

    def __str__(self):
        return("A parcel of land owned by" + self.owner + " and " + self.owner + "with a total area of" + self.area)    

class Riparian(Parcel):
    def __init__(self,owner,area,type):
        self.owner = owner
        self.area = area
        self.type = type

    def getAdjoiningWaterbody(self):
        '''
        It determines if the parcel is adjacent to a waterbody.

        Input:
        Type - integer

        Output:
        Adjacent waterbody in the parcel - string
        '''
        if type == 1:
            print("Adjacent to River - can be subject to titling")
        elif type == 2:
            print("Adjacent to Ocean (Littoral) - cannot be subject to titling")
        else:
            print("Invalid Riparian Parcel")

        return getAdjoiningWaterbody

owner = input("Name of the owner: ")
area = int(input("Area (in sqm): "))