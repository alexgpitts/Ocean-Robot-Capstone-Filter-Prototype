import math

#takes two arrays representing the x (frequency) and y (PSD) coordinates for an acceleration spectrum density graph. 
#returns the PSD array cleaned up
def clean_up(frequency, PSD):
    newArr = list(PSD)
    GU = (0.01 + 0.02)/2.0
    NC = 0
    #loop that runs through the points and updates the PSD value based on the Data-dependent noise function. 
    for i in range(len(frequency)): 
        if(frequency[i]<0.15):
            NC = newArr[i] = 13*GU*(0.15-frequency[i])
            if((frequency[i] > .05 and newArr[i] - NC <= 0) or frequency[i] <= 0.05):
                newArr[i] = 0
            elif(frequency[i] > 0.05 and newArr[i] - NC > 0):
                newArr[i] = newArr[i] - NC
    return newArr


#takes two arrays representing the x (frequency) and y (PSD) coordinates for an acceleration spectrum density graph. 
#returns the Displacement spectrum density data from AS
def getDS(frequency, PSD):
    newArr = list(PSD)
    for i in range(len(frequency)): 
        if(frequency[i] > 0):
            FAS = PSD[i]
            #print(FAS,"\n")
            newArr[i] = FAS/(math.pow((2*math.pi*frequency[i]), 2))
            #print(newArr[i],"\n\n")
    return newArr

