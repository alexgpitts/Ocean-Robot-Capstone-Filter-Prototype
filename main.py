
import matplotlib.pyplot as plt # importing module for creating a graph

import csv
from helpers import * # importing helper module



def main():

    #initial AS
    data = [] #array for all the Frequency values (Hz)
    y1 = [] #array for all the PSD values ((ms^(-2))^(2)/Hz)
    with open('AS190520.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(len(row)>6 and row[0] != "Period" and float(row[0]) > 0):
                # print(row[0], "  ", row[7])
                data.append([1/float(row[0]), float(row[7])])
                # print(1/float(row[0]), "  ", float(row[7]))
    
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
    main()