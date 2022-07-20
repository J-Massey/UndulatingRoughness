#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import array
import os
from tokenize import Double
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors

plt.style.use(["science", "grid"])

from lotusvis.assign_props import AssignProps
from os.path import exists
from tqdm import tqdm


def vorticity_x(flow):
    dv_dz = np.gradient(flow.V, axis=2, edge_order=2)
    dw_dy = np.gradient(flow.W, axis=1, edge_order=2)
    return dw_dy - dv_dz


def vorticity_y(flow):
    du_dz = np.gradient(flow.U, axis=2, edge_order=2)
    dw_dx = np.gradient(flow.W, axis=0, edge_order=2)
    return du_dz - dw_dx


def vorticity_z(flow):
    dv_dx = np.gradient(flow.V, axis=1, edge_order=2)
    du_dy = np.gradient(flow.U, axis=0, edge_order=2)
    return dv_dx - du_dy


def vorticity_mag(flow) -> array:
    try:
        mag = np.sqrt(vorticity_x(flow) ** 2 + vorticity_y(flow) ** 2 + vorticity_z(flow) ** 2)
    except ValueError:
        mag = np.sqrt(vorticity_z(flow) ** 2)
    return mag


def extract_zet(fp):
    with open(fp, "r") as fileSource:
        fileLines = fileSource.readlines()
    txt = fileLines[24]
    return float([s for s in txt.split(' ')][-2][:-1])


def plot_enstrophy():
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.set_ylabel(r'$ E $')
    ax.set_xlabel(r"$ \zeta/U $")

    total_int_r, total_int_s, zetas = get_enstrophy()

    mean_r, max_r, min_r = np.mean(total_int_r, axis=0), np.max(total_int_r, axis=0), np.min(total_int_r, axis=0)
    mean_s, max_s, min_s = np.mean(total_int_s, axis=0), np.max(total_int_s, axis=0), np.min(total_int_s, axis=0)

    colours_r = sns.color_palette('Reds_r', 5)
    ax.fill_between(zetas, max_r, min_r, color=colours_r[2], alpha=0.5, linewidth=0)
    ax.plot(zetas, mean_r, marker="d", color=colours_r[0], ls='-', label='Rough')

    colours_s = sns.color_palette('Blues_r', 5)
    ax.fill_between(zetas, max_s, min_s, color=colours_s[2], alpha=0.5, linewidth=0)
    ax.plot(zetas, mean_s, marker="s", color=colours_s[0], ls='-.', label='Kinematic eq. smooth')

    ax.legend()
    plt.savefig(
        f"{cwd}/figures/enstrophy.pdf", dpi=200, transparent=True
    )
    plt.close()


def pre_check() -> None:
    for idx, case in enumerate(cases):
        if not exists(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy"):
            print(f"Nothing in {cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
            # raise FileNotFoundError
        if not exists(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy"):
            print(f"Nothing in {cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")


def get_enstrophy():
    zetas = [1 / extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90") for idx, case in
             enumerate(cases)]
    total_int_r, total_int_s = [], []
    pre_check()
    for idx, case in enumerate(cases):
        phase_average_r = np.load(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
        phase_average_s = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")

        temp_r, temp_s = [], []
        for snap_r, snap_s in zip(phase_average_r, phase_average_s):
            enstrophy_r = enstrophy(snap_r)
            enstrophy_s = enstrophy(snap_s)

            temp_r.append(enstrophy_r)
            temp_s.append(enstrophy_s)

        total_int_r.append(temp_r)
        total_int_s.append(temp_s)
        del phase_average_r, phase_average_s
    total_int_r, total_int_s = np.array(total_int_r), np.array(total_int_s)
    total_int_r, total_int_s = total_int_r.T, total_int_s.T
    print('f\n', total_int_r, total_int_s, zetas)
    return total_int_r, total_int_s, zetas


def enstrophy(snap: np.array) -> np.array:
    dv = 4 * 2 * 4
    flow = AssignProps(snap)
    vort = vorticity_mag(flow)
    ke = 0.5 * vort ** 2
    scaling = ((np.shape(ke)[1] / 3) * np.shape(ke)[2] * (0.1 * np.shape(ke)[0] / 1.8) * (
            1 / np.sqrt(12000)))  # LxSxAx(1/sqrt(Re))
    scaled_enstrophy = np.sum(ke) / scaling
    del flow
    return scaled_enstrophy


def plot_enstrophy_diff():
    fig, ax = plt.subplots(figsize=(7, 3))

    ax.set_ylabel(r'$ (E_r - E_s)/E_s $')
    ax.set_xlabel(r"$ L/\lambda $")
    colours = sns.color_palette('Reds', 10)
    total_int_r, total_int_s = [], []

    # Find the volume a box of c, c, z takes up to normalise the enstrophy
    for idx, case in enumerate(cases):

        phase_average = np.load(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
        phase_average_2d = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")
        cell_volume = 4 / cs[idx] * 2 / cs[idx] * 4 / cs[idx]

        temp = []
        for ident, (snap, snap_2d) in enumerate(zip(phase_average, phase_average_2d)):
            flow = AssignProps(snap)
            flow_2d = AssignProps(snap_2d)

            enst = enstrophy(cell_volume, flow)
            enst_2d = enstrophy(cell_volume, flow_2d)
            enst_diff = (enst - enst_2d) / enst_2d

            temp.append(enst_diff)
            del flow, flow_2d

        total_int_r.append(temp)
        del phase_average

    total_int_r = np.array(total_int_r)
    total_int_r = total_int_r.T

    ax.plot(cases, np.mean(total_int_r, axis=0), marker="+", color=colours[2])

    plt.savefig(
        f"{cwd}/figures/enstrophy_diff.pdf", dpi=300, transparent=True
    )
    plt.close()


if __name__ == '__main__':
    global cwd
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])

    cases = np.array([52, 48, 44, 40, 36, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    # cases = np.array([0, 4])
    # cs = np.array([1024, 1024])

    plot_enstrophy()
    # plot_enstrophy_diff()
    # pre_check()
    # np.save(f"{cwd}/enstrophies", np.array(get_enstrophy()))
