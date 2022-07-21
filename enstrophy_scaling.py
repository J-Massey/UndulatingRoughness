#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np
from get_vort import vorticity_mag
from inout import extract_zet

import seaborn as sns
from matplotlib import pyplot as plt

plt.style.use(["science", "grid"])

from lotusvis.assign_props import AssignProps
from os.path import exists


def plot_e_scale():
    fig, ax = plt.subplots(figsize=(5, 3))

    ax.set_ylabel(r'$ E $')
    ax.set_xlabel(r"$ \zeta/U $")

    mean_r, max_r, min_r = np.mean(total_int_r, axis=0), np.max(total_int_r, axis=0), np.min(total_int_r, axis=0)
    mean_s, max_s, min_s = np.mean(total_int_s, axis=0), np.max(total_int_s, axis=0), np.min(total_int_s, axis=0)

    colours_r = sns.color_palette('Reds_r', 5)
    ax.fill_between(zetas, max_r, min_r, color=colours_r[2], alpha=0.5, linewidth=0)
    ax.plot(zetas, mean_r, marker="d", color=colours_r[0], ls='-', label='Rough')

    colours_s = sns.color_palette('Blues_r', 5)
    ax.fill_between(zetas, max_s, min_s, color=colours_s[2], alpha=0.5, linewidth=0)
    ax.plot(zetas, mean_s, marker="s", color=colours_s[0], ls='-.', label='Kinematic eq. smooth')

    print(np.array([zetas, mean_s, mean_r]))
    np.save(f"{cwd}/enstrophy", np.array([zetas, mean_s, mean_r]))

    ax.legend()
    plt.savefig(
        f"{cwd}/figures/enstrophy.pdf", dpi=200, transparent=True
    )
    plt.close()


def scaling_test():
    zetas, mean_s, mean_r = np.load(f"{cwd}/enstrophy.npy")
    return mean_s, mean_r


def _get_vort_max():
    for idx, case in enumerate(cases):
        phase_average_2d = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")
        temp = []
        for ident, snap in enumerate(phase_average_2d):
            flow = AssignProps(snap)
            vort_max = vorticity_mag(flow)
            print(np.shape(vort_max))
            x_pos = np.mean(flow.X[np.where((flow.X>0.25)&(flow.X<0.26))])
            print(np.shape(x_pos))


            x_pos = np.mean(flow.X[np.where(np.max(vort_max))])
            temp.append(x_pos)

    return temp


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


if __name__ == '__main__':
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])

    # plot_enstrophy()
    _get_vort_max()
