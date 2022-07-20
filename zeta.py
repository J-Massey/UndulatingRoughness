#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
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

from inout import read_forces, extract_zet
from scipy.interpolate import interp1d
from tqdm import tqdm


def plot_lam():
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlabel(r"$ L/\lambda $", fontsize=12)
    ax.set_ylabel(r"$ \zeta $", fontsize=12)

    zets = np.empty(len(cases))
    for idx, case in enumerate(cases):
        zets[idx] = extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
    
    ax.plot(cases, zets, color='purple')
    
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/zeta_lambda.pdf", dpi=300
    )


def plot_power_avg_vs_wavespeed():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ c_{\lambda} = \lambda (\zeta / f)f $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        zet = 1/extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        ax.scatter(zet/case, np.mean(ux[t>4]), color=colors[idx])
    
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/power_wavespeed.pdf", bbox_inches="tight", dpi=200
    )


def plot_power_nbumps():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ c_{\lambda} = 1/\lambda / (\zeta / f) $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        zet = 1/extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        ax.scatter(case/zet, np.mean(ux[t>4]), color=colors[idx])
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ c_{\lambda} = (\zeta / f)/\lambda $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        zet = extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90")
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        ax.scatter(zet*case, np.mean(ux[t>4]), color=colors[idx])
    
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/power_bumps_per_wave.pdf", bbox_inches="tight", dpi=200
    )


def main():
    plot_lam()
    # plot_power_avg_vs_wavespeed()
    # plot_power_nbumps()


if __name__ == "__main__":
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    main()