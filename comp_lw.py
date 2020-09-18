#!/usr/bin/python

import numpy as np
import sys

def approx(rw, zoom_lvls, lat):
    C = 40075016
    lw = rw * 2**(zoom_lvls+8) / (C * np.cos(lat))
    output = ""
    for i,z in enumerate(zoom_lvls):
        if i != 0:
            output += ';'
        output += f"{z}:{lw[i]:.2f}" 
    
    return output



if __name__ == "__main__":
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(
            """
            Computes piecewise linear approximation for linewidths as function
            of real-life width. Usage:
            
                python comp_lw.py [rw] [zoom_lvls] [lat]
                    rw:         real width in meters
                    zoom_lvls:  zoom levels (comma-delimited without spaces)
                    lat:        latitude at which this is gonna be computed
            """
        )
        
    else:
        try:
            rw = float(sys.argv[1])
            zoom_lvls = sys.argv[2].split(',')
            zoom_lvls = [int(zoom_lvls[i]) for i in range(len(zoom_lvls))]
            zoom_lvls = np.asarray(zoom_lvls, dtype=int)
            lat = float(sys.argv[3])
            
            output = approx(rw, zoom_lvls, lat)
            print(output)
        except:
            print("You've entered bullshit!")