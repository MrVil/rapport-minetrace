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
with open(args.obsels_file) as obselsJson:
    obsels = json.load(obselsJson)


# BROWSE THE OBSELS AND SEARCH FOR THE INTERESTING ONES (GOLD, DIAMOND AND REDSTONE)
centers = []
colorsarray = []

for i in range(len(obsels)):
    if obsels[i]["m:itemName"] in {"DIAMOND","REDSTONE","GOLD","IRON_ORE","COAL"}:
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
coll = PolyCollection(centers, edgecolors='black', facecolors=colorsarray)
ax.add_collection(coll)
ax.autoscale_view()
plt.show()
