import math

#takes two arrays representing the x (frequency) and y (PSD) coordinates for an acceleration spectrum density graph. 
#returns the PSD array cleaned up
def clean_up(data):
    newArr = list(data)
    GU = (0.01 + 0.02)/2.0
    NC = 0
    #loop that runs through the points and updates the PSD value based on the Data-dependent noise function. 
    for i in range(len(data)): 
        if(data[i][0]<0.15):
            NC = newArr[i][1] = 13*GU*(0.15-data[i][0])
            if((data[i][0] > .05 and newArr[i][1] - NC <= 0) or data[i][0] <= 0.05):
                newArr[i][1] = 0
            elif(data[i][0] > 0.05 and newArr[i][1] - NC > 0):
                newArr[i][1] = data[i][1] - NC
    return newArr


#takes two arrays representing the x (frequency) and y (PSD) coordinates for an acceleration spectrum density graph. 
#returns the Displacement spectrum density data from AS
def getDS(data):
    newArr = list(data)
    for i in range(len(data)): 
        if(data[i][0] > 0):
            FAS = data[i][1]
            #print(FAS,"\n")
            newArr[i][1] = FAS/(math.pow((2*math.pi*data[i][0]), 2))
            #print(newArr[i],"\n\n")
    return newArr


def getSH(data):
    temp = []
    for i in data: 
        pass

    return temp
