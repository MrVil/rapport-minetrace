# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import json
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.set_aspect("equal")


# OPEN THE JSON FILE CONTAINING THE OBSELS
with open('obselsTardi2.json') as obsels_file:
    obsels = json.load(obsels_file)

color = "black"

# BROWSE THE OBSELS AND PLOT THE INTERESTING ONES (GOLD, DIAMOND AND REDSTONE)
for i in range(len(obsels) - 1, -1, -1):
    if obsels[i]["m:itemName"] != "STONE":
        if obsels[i]["m:itemName"] == "DIAMOND":
            color = "blue"
        if obsels[i]["m:itemName"] == "REDSTONE":
            color = "red"
        if obsels[i]["m:itemName"] == "GOLD":
            color = "yellow"
        if obsels[i]["m:itemName"] == "IRON_ORE":
            color = "lightgrey"
        if obsels[i]["m:itemName"] == "COAL":
            color = "black"
        # for s,e in combinations(np.array(list(product([obsels[i]['m:x'], obsels[i]['m:x']+1],[obsels[i]['m:y'], obsels[i]['m:y']+1],[obsels[i]['m:z'], obsels[i]['m:z']+1]))), 2):
        #     if np.sum(np.abs(s-e)) == 1:
        #         ax.plot_surface([10, 20, 20, 10], [10, 10, 20, 20], [0, 0, 0, 0], color=color, facecolors=color)
        #         ax.plot_surface([10, 20, 20, 10], [10, 10, 20, 20], [10, 10, 10, 10], color=color, facecolors=color)
        r = [0,1]
        X, Y = np.meshgrid(r, r)
        ax.plot_surface(X + obsels[i]["m:x"],Y + obsels[i]["m:z"],1 + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],Y + obsels[i]["m:z"],0 + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],0 + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(X + obsels[i]["m:x"],1 + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(1 + obsels[i]["m:x"],X + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)
        ax.plot_surface(0 + obsels[i]["m:x"],X + obsels[i]["m:z"],Y + obsels[i]["m:y"], alpha=0.75, color = color, linewidths=0)


# r = [0,1]
# X, Y = np.meshgrid(r, r)
# ax.plot_surface(X,Y,1, alpha=0.5)
# ax.plot_surface(X,Y,0, alpha=0.5)
# ax.plot_surface(X,0,Y, alpha=0.5)
# ax.plot_surface(X,1,Y, alpha=0.5)
# ax.plot_surface(1,X,Y, alpha=0.5)
# ax.plot_surface(0,X,Y, alpha=0.5)


#ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print(obsels)

#draw cube
#r = [-10, 1]
#for s,e in combinations(np.array(list(product(r,r,r))), 2):
#    if np.sum(np.abs(s-e)) == r[1]-r[0]:
#        ax.plot3D(*zip(s,e), color="b")
