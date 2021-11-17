import matplotlib.pyplot as plt # importing module for creating a graph
from helpers import * # importing helper module

def main():
    plot1 = plt.figure(1)
    
    #initial AS
    x1 = [0,1,2,3,4,5,6,7,8,9] #array for all the Frequency values (Hz)
    y1 = [1,3,5,2,3,5,2,3,4,3] #array for all the PSD values ((ms^(-2))^(2)/Hz)

    #cleaned up AS
    x2 = x1 
    y2 = clean_up(x1, y1) 

    #DS
    x3 = x2 
    y3 = getDS(x2, y2) 

    plt.plot(x1, y1)      
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((ms^(-2))^(2)/Hz)')
    plt.title('Acceleration Spectrum Density (U)')

    plot2 = plt.figure(2)
    plt.plot(x2, y2)      
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((ms^(-2))^(2)/Hz)')
    plt.title('Cleaned Up Acceleration Spectrum Density (U)')


    plot3 = plt.figure(3)
    plt.plot(x3, y3)      
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((m^2)/Hz)')
    plt.title('Displacement Spectrum Density (U)')


    plt.show()


if __name__ == "__main__":
    main()