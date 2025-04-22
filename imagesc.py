#!/usr/bin/env python3

from PIL import Image
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import sys

# check input arguments
if len(sys.argv) < 5:
    print("This program requires some arguments!")
    sys.exit(1)

# set filename
filename = sys.argv[1]

# open file
with open(filename, 'r') as f:
    # read raw data
    rawdata = np.loadtxt(f)

    # read data
    size = np.array(rawdata[0:2]).astype(int)
    data = rawdata[8:]
    
    # reshape data
    data = np.reshape(data, size, 'F')
    data = data[::-1, :]

# clip data
data = np.maximum(data, float(sys.argv[3]))
data = np.minimum(data, float(sys.argv[4]))

# normalize data to [0, 1] interval
min_val = np.minimum(np.min(data), float(sys.argv[3])) 
max_val = np.maximum(np.max(data), float(sys.argv[4])) 
data = data - min_val
data = data / (max_val - min_val) 

if len(sys.argv) > 2:
    str_steps = [x for x in sys.argv[2].split(";") if x]
    num_steps = len(str_steps)
    cdict = {'red': [], 'green': [], 'blue': []}
    color = dict()

    for color_idx in range(num_steps):
        str_colors = str_steps[color_idx].split(",")

        pos = color_idx/(num_steps - 1)

        color['red'] = float(str_colors[0])
        color['green'] = float(str_colors[1])
        color['blue'] = float(str_colors[2])

        for key in cdict.keys():
            cdict[key].append((pos, color[key], color[key],))

    cm.register_cmap(name="custom", data=cdict)

    colormap = cm.get_cmap("custom")
else:
    colormap = cm.get_cmap("jet")

# create image
print(sys.argv[5])
im = Image.fromarray(colormap(data, bytes=True))
im.save(sys.argv[5], "PNG")

