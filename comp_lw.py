#!/usr/bin/python

import numpy as np
import sys
import argparse

def approx(width, latitude, zoom_lvls):
    C = 40075016
    line_width = width * 2**(zoom_lvls+8) / (C * np.cos(latitude))
    output = ""
    for i,z in enumerate(zoom_lvls):
        if i != 0:
            output += ';'
        output += f"{z}:{line_width[i]:.2f}" 
    
    return output



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Computes the piecewise linear approximation to the scaling ot linewidths. Relevant zoom levels range from 13 to 18")
    parser.add_argument("width", metavar='w', type=float, help="width of the object (road, tracks, river) in the real worl in meters")
    parser.add_argument("latitude", metavar='l', type=float, help="latitude, at which this should be computed")
    parser.add_argument("zoom_lvls", metavar='z', type=int, nargs='+', help="list of zoom levels for which the approximation should be computed")
    
    args = parser.parse_args()
    
    output = approx(args.width, args.latitude, np.asarray(args.zoom_lvls))
    print(output)