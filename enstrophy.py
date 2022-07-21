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

    print(np.array([zetas, mean_s, mean_r]))
    np.save(f"{cwd}/enstrophy", np.array([zetas, mean_s, mean_r]))

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


if __name__ == '__main__':
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])

    plot_enstrophy()

