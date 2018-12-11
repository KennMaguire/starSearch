#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import csv
import numpy as np
import time
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
            idName = "Unnamed star " + row[0]
            starDict[idName] = (row[17], row[18], row[19])


#print(starDict)
#print(starDict['Sol'])
#print(starDict['Alpheratz'])
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
    #print(dist1)
    if(dist1 <= 10):
        total += 1
        starList.append((key,value))
print(starList)
print("\n\n\n")
print("The total number of stars within 10 parsecs of Sol is " + str(total))
distList = []

# find the shortest distance from sol first time
# change i to value with shortest value
# get shortest distance for next
i = 0
starsTraversalOrder = []
while starList:
    for j in range(0, len(starList)):
        x1 = float(starList[i][1][0])
        y1 = float(starList[i][1][1])
        z1 = float(starList[i][1][2])
        if j == i:
            pass
        else:
            x2 = float(starList[j][1][0])
            y2 = float(starList[j][1][1])
            z2 = float(starList[j][1][2])
            dist2 = getDist(x1,y1,z1,x2,y2,z2)
            distList.append((j,dist2))          #get all distance from the star and append to list


    if distList:
        nextStar = min(distList, key = lambda t: t[1])      #get the minimum distance in the list by the second value in the tuple
        #print(distList)
    #print(nextStar)
    starsTraversalOrder.append((starList[i], nextStar[1])) #append starList[]
    #print(starsTraversalOrder)
    starList.remove(starList[i])
    if i < nextStar[0]:
        i = (nextStar[0]-1) #get the index of the next star to get distances for
    else:
        i = nextStar[0]
    #print(starList)
#    print(starsTraversalOrder)
    distList.clear()


#print(starsTraversalOrder)
totalDist = 0
print("\n")
for i in range(0,10):
    totalDist += starsTraversalOrder[i][1]
    print(str(starsTraversalOrder[i][0][0]) + " -> " + str(starsTraversalOrder[i+1][0][0]) + ": Distance = " + str(round(starsTraversalOrder[i][1], 2)) + ", Total Distance = " + str(round(totalDist, 2)))

print("...")

for i in range(10, len(starsTraversalOrder)-11): #add to the total distance for all stars between index 10 and (size of list of Stars in Order - 10)
    totalDist += starsTraversalOrder[i][1]

for i in range(len(starsTraversalOrder)-11,len(starsTraversalOrder)-1):
    totalDist += starsTraversalOrder[i][1]
    print(str(starsTraversalOrder[i][0][0]) + " -> " + str(starsTraversalOrder[i+1][0][0]) + ": Distance = " + str(round(starsTraversalOrder[i][1], 2)) + ", Total Distance = " + str(round(totalDist, 2)))

print("The total distance traversed is " + str(totalDist) + " parsecs.")

"""
    print(i[0])
    print(i[1][0])
    print(i[1][1])
    print(i[1][2])
"""
