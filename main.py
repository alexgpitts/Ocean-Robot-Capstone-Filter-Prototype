
import matplotlib.pyplot as plt # importing module for creating a graph

import csv
from helpers import * # importing helper module

import sys





def main(argv):
    i = 0
    #initial AS
    data = [] #2d array for all the x and y values. Format = [[frequency1, PSD1], [frequency2, PSD2], [frequency3, PSD3], ...., [frequency1, PSD1]]
    
    with open(argv[0], newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(len(row)<6):
                continue
            
            if(row[0] == "Period" or float(row[0]) <= 0):
                continue
    
            if(len(row)>6 and i < 1026):
                data.append([1/float(row[0]), float(row[7])])
                i+=1

            else:
                break
    
    sorted_date=sorted(data, key=lambda k: [k[0], k[1]])
    
    plot1 = plt.figure(1)
    plt.plot([i[0] for i in sorted_date], [i[1] for i in sorted_date], color='purple', linewidth=.35)   
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((ms^(-2))^(2)/Hz)')
    plt.title('Acceleration Spectrum Density (U)')

    #cleaned up AS
    data2 = clean_up(sorted_date)

    plot2 = plt.figure(2)
    plt.plot([i[0] for i in data2], [i[1] for i in data2],color='blue', linewidth=.35)     
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((ms^(-2))^(2)/Hz)')
    plt.title('Cleaned Up Acceleration Spectrum Density (U)')

    #DS
    data3 = getDS(data2)
    
    
    plot3 = plt.figure(3)
    plt.plot([i[0] for i in data3], [i[1] for i in data3], color='green', linewidth=.35)    
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PSD ((m^2)/Hz)')
    plt.title('Displacement Spectrum Density (U)')

    

    with open('displacement.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data3)


    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])