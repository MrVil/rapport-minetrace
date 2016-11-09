import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import matplotlib as mpl
import json
import argparse


# PROCESS THE PARAMETERS
parser = argparse.ArgumentParser(description='Plot Minecraft Obsels in 2D.')
parser.add_argument('obsels_file', metavar='N', type=str, help='the path to the file containing the obsels')
args = parser.parse_args()

# OPEN THE JSON FILE CONTAINING THE OBSELS
with open('obselsFull.json') as obsels_file:
    obsels = json.load(obsels_file)

# print(obsels)

# OPEN THE JSON FILE CONTAINING THE OBSELS
with open(args.obsels_file) as obselsJson:
    obsels = json.load(obselsJson)


# BROWSE THE OBSELS AND SEARCH FOR THE INTERESTING ONES (GOLD, DIAMOND AND REDSTONE)
centers = []
colorsarray = []

min_x = 1000
max_x = -1000
min_y = 1000
max_y = -1000

for i in range(len(obsels)):
    if obsels[i]["m:itemName"] in {"DIAMOND","REDSTONE","GOLD","IRON_ORE","COAL"}:
        if obsels[i]["m:x"] < min_x :
            min_x = obsels[i]["m:x"]
        if obsels[i]["m:x"] > max_x :
            max_x = obsels[i]["m:x"]
        if obsels[i]["m:y"] < min_y :
            min_y = obsels[i]["m:y"]
        if obsels[i]["m:y"] > max_y :
            max_y = obsels[i]["m:y"]        
        centers.append([[obsels[i]['m:x'], obsels[i]['m:y']], [obsels[i]['m:x'] + 1, obsels[i]['m:y']], [obsels[i]['m:x'] + 1, obsels[i]['m:y'] + 1], [obsels[i]['m:x'], obsels[i]['m:y'] + 1]] )
        if obsels[i]["m:itemName"] == "DIAMOND":
            colorsarray.append("blue")
        elif obsels[i]["m:itemName"] == "REDSTONE":
            colorsarray.append("red")
        elif obsels[i]["m:itemName"] == "GOLD":
            colorsarray.append("yellow")
        elif obsels[i]["m:itemName"] == "IRON_ORE":
            colorsarray.append("grey")
        elif obsels[i]["m:itemName"] == "COAL":
            colorsarray.append("black")


#create a subplot
fig, ax = plt.subplots()


# Make the collection and add it to the plot.

coll = PolyCollection(centers, edgecolors="none", facecolors=colorsarray)
ax.add_collection(coll)
#ax.autoscale_view()
ax.set_xlim([min_x - 1, max_x + 2])
ax.set_ylim([min_y - 1, max_y + 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
