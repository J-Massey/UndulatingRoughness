# -*- coding: utf-8 -*-
"""
@author: Jonathan Massey
@description: This script will read all the .png files in one folder,
              sort them in some sensible order, then make a gif called 
              'movie.gif'.
              
              To use it `cd /path/to/folder && python3 /path/to/gif_generation.py`
@contact: masseyjmo@gmail.com
"""


import imageio
import os
from tkinter import Tcl


def fns(dirn):
    fns = [fn for fn in os.listdir(dirn) if fn.endswith(f".png")]
    fns = Tcl().call("lsort", "-dict", fns)
    return fns


def main():
    cwd = os.getcwd()
    images = []
    for filename in fns(cwd):
        images.append(imageio.imread(filename))
    imageio.mimsave(f"{cwd}/movie.gif", images)


if __name__ == "__main__":
    main()