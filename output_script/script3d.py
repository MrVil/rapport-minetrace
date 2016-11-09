# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import json
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.set_aspect("equal")
import argparse


# PROCESS THE PARAMETERS
parser = argparse.ArgumentParser(description='Plot Minecraft Obsels in 2D.')
parser.add_argument('obsels_file', metavar='N', type=str, help='the path to the file containing the obsels')
args = parser.parse_args()


# OPEN THE JSON FILE CONTAINING THE OBSELS
with open(args.obsels_file) as obselsJson:
    obsels = json.load(obselsJson)


# BROWSE THE OBSELS AND PLOT THE INTERESTING ONES (GOLD, DIAMOND AND REDSTONE)
min_x = 1000
max_x = -1000
min_y = 1000
max_y = -1000
min_z = 1000
max_z = -1000

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
        if obsels[i]["m:z"] < min_z :
            min_z = obsels[i]["m:z"]
        if obsels[i]["m:z"] > max_z :
            max_z = obsels[i]["m:z"]
        if obsels[i]["m:itemName"] == "DIAMOND":
            color = "blue"
        elif obsels[i]["m:itemName"] == "REDSTONE":
            color = "red"
        elif obsels[i]["m:itemName"] == "GOLD":
            color = "yellow"
        elif obsels[i]["m:itemName"] == "IRON_ORE":
            color = "lightgrey"
        elif obsels[i]["m:itemName"] == "COAL":
            color = "black"
        r = [0,1]
        X, Y = np.meshgrid(r, r)
        ax.plot_surface(X + obsels[i]["m:x"],Y + obsels[i]["m:z"],1 + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],Y + obsels[i]["m:z"],0 + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],0 + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],1 + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(1 + obsels[i]["m:x"],X + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(0 + obsels[i]["m:x"],X + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)


#ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
ax.set_xlim([min_x - 1, max_x + 2])
ax.set_ylim([min_z - 1, max_z + 2])
ax.set_zlim([min_y - 1, max_y + 2])
plt.show()
