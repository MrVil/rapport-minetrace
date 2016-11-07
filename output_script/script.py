import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import matplotlib as mpl
import json
import argparse

parser = argparse.ArgumentParser(description='Plot Minecraft Obsels in 2D.')
parser.add_argument('obsels_file', metavar='N', type=str,
                    help='the path to the file containing the obsels')

args = parser.parse_args()


# OPEN THE JSON FILE CONTAINING THE OBSELS
with open(args.obsels_file) as obselsJson:
    obsels = json.load(obselsJson)

# print(obsels)


# BROWSE THE OBSELS AND SEARCH FOR THE INTERESTING ONES (GOLD, DIAMOND AND REDSTONE), AND FOR INTERESTING VALUES SUCH AS MIN X, Y AND Z
if len(obsels) > 0:
    min_x = obsels[0]['m:x']
    max_x = obsels[0]['m:x']
    min_y = obsels[0]['m:y']
    max_y = obsels[0]['m:y']
    min_z = obsels[0]['m:z']
    max_z = obsels[0]['m:z']

centers = []
colorsarray = []

for i in range(len(obsels) - 1, -1, -1):
    if obsels[i]["m:itemName"] == "STONE":
        obsels.pop(i)
    else:
        if obsels[i]['m:x'] < min_x:
            min_x = obsels[i]['m:x']
        if obsels[i]['m:x'] > max_x:
            max_x = obsels[i]['m:x']
        if obsels[i]['m:y'] < min_y:
            min_y = obsels[i]['m:y']
        if obsels[i]['m:y'] > max_y:
            max_y = obsels[i]['m:y']
        if obsels[i]['m:z'] < min_z:
            min_z = obsels[i]['m:z']
        if obsels[i]['m:z'] > max_z:
            max_z = obsels[i]['m:z']
        centers.append([[obsels[i]['m:x'], obsels[i]['m:y']], [obsels[i]['m:x'] + 1, obsels[i]['m:y']], [obsels[i]['m:x'] + 1, obsels[i]['m:y'] + 1], [obsels[i]['m:x'], obsels[i]['m:y'] + 1]] )
        if obsels[i]["m:itemName"] == "DIAMOND":
            colorsarray.append("lightblue")
        if obsels[i]["m:itemName"] == "REDSTONE":
            colorsarray.append("red")
        if obsels[i]["m:itemName"] == "GOLD":
            colorsarray.append("yellow")
        if obsels[i]["m:itemName"] == "IRON_ORE":
            colorsarray.append("grey")
        if obsels[i]["m:itemName"] == "COAL":
            colorsarray.append("black")


# Generate data. In this case, we'll make a bunch of center-points and generate
# verticies by subtracting random offsets from those center-points
#numpoly, numverts = 100, 4
#centers = [[[10, 20, 20, 10, 20, 30, 30, 20], [10, 10, 20, 20, 20, 20, 30, 30]]]
#centers = [[[min_x, min_y], [min_x + 1, min_y], [min_x + 1, min_y + 1]]]
#centers = [[10, 10], [20, 10], [20, 20], [10, 20]], [[20, 20], [30, 20], [30, 30], [20, 30]]
#centers = [[[10, 10], [20, 10], [20, 20], [10, 20]], [[20, 20], [30, 20], [30, 30], [20, 30]]]
#centers = [[[10, 10, 10], [20, 10, 10], [20, 20, 10], [10, 20, 10]], [[20, 20, 10], [30, 20, 10], [30, 30, 10], [20, 30, 10]]]
#offsets = 10 * (np.random.random((numverts,numpoly,2)) - 0.5)
#verts = centers + offsets
#verts = np.swapaxes(verts, 0, 1)
#centers = np.swapaxes(centers, 0, 1)

# In your case, "verts" might be something like:
# verts = zip(zip(lon1, lat1), zip(lon2, lat2), ...)
# If "data" in your case is a numpy array, there are cleaner ways to reorder
# things to suit.

# Color scalar...
# If you have rgb values in your "colorval" array, you could just pass them
# in as "facecolors=colorval" when you create the PolyCollection
#z = np.random.random(numpoly) * 500

fig, ax = plt.subplots()

# Make the collection and add it to the plot.
coll = PolyCollection(centers, edgecolors='black', facecolors=colorsarray)
#coll = PolyCollection(centers, array=z, cmap=mpl.cm.jet, edgecolors='black')
ax.add_collection(coll)
#ax.autoscale_view()
ax.set_xlim([min_x - 1, max_x + 2])
ax.set_ylim([min_y - 1, max_y + 2])


# Add a colorbar for the PolyCollection
plt.show()
