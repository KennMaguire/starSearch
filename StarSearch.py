#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import csv
import numpy as np

#properName 6
#x 17
#y 18
#z 19
starDict = {}


def getDist(_x1, _y1, _z1, _x2, _y2, _z2):
    dist = np.sqrt(((_x2-_x1)**2)+ ((_y2-_y1)**2) + ((_z2-_z1)**2))
    return dist

with open("hygxyz.csv", "r") as xyzfile:
    next(xyzfile)
    xyzRead = csv.reader(xyzfile, delimiter=',')
    for row in xyzRead:
        if row[6] != '':
            starDict[row[6]] = (row[17],row[18], row[19])
        elif row[4] != '':
            glName = "Gliese " + row[4]
            starDict[glName] = (row[17],row[18], row[19])
        elif row[5] != '':
            bfName = "BF " + row[5]
            starDict[bfName] = (row[17],row[18], row[19])
        else:
            idName = "Unknown star " + row[0]
            starDict[idName] = (row[17], row[18], row[19])


#print(starDict)
print(starDict['Sol'])
print(starDict['Alpheratz'])
starList = []



#print(starList)
total = 0
for key,value in starDict.items():
    x1 = float(starDict["Sol"][0])
    y1 = float(starDict["Sol"][1])
    z1 = float(starDict["Sol"][2])
    x2 = float(starDict[key][0])
    y2 = float(starDict[key][1])
    z2 = float(starDict[key][2])

    dist1 = getDist(x1,y1,z1,x2,y2,z2)
    print(dist1)
    if(dist1 <= 10):
        total += 1
        starList.append((key,value))
print(starList)
print("The total number of stars within 10 parsecs of Sol is " + str(total))
