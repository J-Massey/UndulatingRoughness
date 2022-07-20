#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from turtle import color
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
plt.style.use(["science", "grid"])

from lotusvis.flow_field import ReadIn
# from lotusvis.plot_flow import Plots
from lotusvis.decompositions import Decompositions
from lotusvis.assign_props import AssignProps

from inout import read_forces
from scipy.interpolate import interp1d
from tqdm import tqdm


def extract_zet(fp):
    with open(fp,"r") as fileSource:
        fileLines = fileSource.readlines()
    txt = fileLines[24]
    return float([s for s in txt.split(' ')][-2][:-1])
    

def plot_amax():
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlabel(r"$ zeta/U $")
    ax.set_ylabel(r"$ \alpha_{max}^{\circ} $")

    t = np.linspace(0, 2*np.pi)
    a, b, c = 0.28, 0.13, 0.05
    for idx, case in enumerate(cases):
        zet = extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        x = 0
        y = (a*x**2+b*x+c)*np.sin(t+zet*x)
        y_prime = b*np.sin(t)-c*np.cos(t)*zet

        ax.scatter(case, np.max(y_prime)*180/np.pi, color=colors[idx], marker='d')
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/alpha_max.pdf", dpi=300
    )


def plot_curvature():
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlabel(r"$ zeta/U $")
    ax.set_ylabel(r"$ \kappa $")

    t = np.linspace(0, 2*np.pi)
    a, b, c = 0.28, 0.13, 0.05
    for idx, case in enumerate(cases):
        zet = extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        x = 0
        y = (a*x**2+b*x+c)*np.sin(t+zet*x)
        y_pprime = a*np.sin(t) - 2*b*np.cos(t)*zet - c*np.sin(t)*zet**2
        ax.scatter(case, np.max(y_pprime), color=colors[idx], marker='d')
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/curvature.pdf", dpi=300
    )


def plot_ydot():
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlabel(r"$ zeta/U $")
    ax.set_ylabel(r"$ \dot{y}(0, t)|_{max} $")

    t = np.linspace(0, 2*np.pi)
    a, b, c = 0.28, 0.13, 0.05
    for idx, case in enumerate(cases):
        zet = extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        x = 0
        y = (a*x**2+b*x+c)*np.sin(t+zet*x)
        y_dot = (+c)*np.cos(t) + np.sin(t)

        ax.scatter(case, np.max(y_dot), color=colors[idx], marker='d')
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/y_dot.pdf", dpi=300
    )


def main():
    plot_amax()
    plot_curvature()
    plot_ydot()


if __name__ == "__main__":
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    z_size = np.array([32, 32, 32, 32, 16, 16, 16, 16, 16, 4, 4, 4, 4, 2])

    cases = np.array([52, 48, 44, 40, 36, 28, 24, 20, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1036, 1056, 1020, 1024, 1024, 1024])
    # main()
    dummy = np.random.rand(10,3)
    max = np.max(dummy, axis=0)
    print(dummy, '\n', max)


