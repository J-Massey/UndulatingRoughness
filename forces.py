#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np

from inout import read_forces, extract_zet
from scipy.interpolate import interp1d

from scipy.optimize import curve_fit

import seaborn as sns
from matplotlib import pyplot as plt

plt.style.use(["science", "grid"])


def plot_power():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(f"$ t $")
    ax.set_ylabel(r"$ C_P $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        ax.plot(t[t > 0.5], ux[t > 0.5], color=colors[idx], label=f'{str(case)}x{str(case)}')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(
        f"{cwd}/figures/power_ts.pdf", bbox_inches="tight", dpi=300
    )


def plot_phase_av():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(f"$ t $")
    ax.set_ylabel(r"$ C_P $")

    power = np.array
    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        t, ux = t[t > 3], ux[t > 3]
        t = t % 1
        f = interp1d(t, ux, fill_value='extrapolate')
        t = np.linspace(0, 1, 300)
        ux = f(t)

        ax.plot(t, ux, color=colors[idx], label=f'{str(case)}x{str(case)}')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(
        f"{cwd}/figures/power_phase.pdf", bbox_inches="tight", dpi=300
    )


def plot_power_avg():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ L/\lambda $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        print(case)
        ax.scatter(case, np.mean(ux[t > 4]), color=colors[idx])

    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/power_avg.pdf", bbox_inches="tight", dpi=200
    )


def plot_power_diff():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ \zeta/U $")
    ax.set_ylabel(r"$ \overline{C_{P}} $")

    zets = [1 / extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90") for idx, case in
            enumerate(cases)]

    smooth, rough = np.empty(len(cases)), np.empty(len(cases))
    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/2D/fort.9", interest='cp')
        t_r, ux_r, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        smooth[idx] = np.mean(ux[t > 4])
        rough[idx] = np.mean(ux_r[t_r > 4])

    ax.plot(zets, rough, ls='-', color=sns.color_palette('Reds_r', 4)[0], label='Rough')
    ax.plot(zets, smooth, ls='-.', color=sns.color_palette('Blues_r', 4)[0], label='Kinematic eq. smooth')
    print(zets, cases)

    ax.legend()
    plt.savefig(
        f"{cwd}/figures/power_diff.pdf", bbox_inches="tight", dpi=200
    )


def plot_thrust_diff():
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ \zeta/U $")
    ax.set_ylabel(r"$ \overline{C_{T}} $")

    zets = [1 / extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90") for idx, case in
            enumerate(cases)]

    smooth, rough = np.empty(len(cases)), np.empty(len(cases))
    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/2D/fort.9", interest='p')
        t_r, ux_r, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='p')
        smooth[idx] = np.mean(ux[t > 4])
        rough[idx] = np.mean(ux_r[t_r > 4])

    ax.plot(zets, rough, ls='-', color=sns.color_palette('Reds_r', 4)[0], label='Rough')
    ax.plot(zets, smooth, ls='-.', color=sns.color_palette('Blues_r', 4)[0], label='Kinematic eq. smooth')

    ax.legend()
    plt.savefig(
        f"{cwd}/figures/thrust_diff.pdf", bbox_inches="tight", dpi=200
    )


def plot_side_diff():
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ \zeta/U $")
    ax.set_ylabel(r"$ RMS(\overline{C_{L}}) $")

    zets = [1 / extract_zet(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/lotus.f90") for idx, case in
            enumerate(cases)]

    smooth, rough = np.empty(len(cases)), np.empty(len(cases))
    for idx, case in enumerate(cases):
        t, _, ux = read_forces(f"{cwd}/{str(case)}x{str(case)}/2D/fort.9", interest='p')
        rms = np.sqrt((ux - np.mean(ux)) ** 2)
        t_r, _, ux_r = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='p')
        rms_r = np.sqrt((ux_r - np.mean(ux_r)) ** 2)
        smooth[idx] = np.mean(rms[t > 4])
        rough[idx] = np.mean(rms_r[t_r > 4])

    ax.plot(zets, rough, ls='-', color=sns.color_palette('Reds_r', 4)[0], label='Rough')
    ax.plot(zets, smooth, ls='-.', color=sns.color_palette('Blues_r', 4)[0], label='Kinematic eq. smooth')

    ax.legend()
    plt.savefig(
        f"{cwd}/figures/side_diff.pdf", bbox_inches="tight", dpi=200
    )


def fit_sine(t, a, b, c):
    return a + b * np.sin(4 * np.pi * t + c)


def find_offset(t, ux):
    t, ux = t[t > 3], ux[t > 3]
    t = t % 1
    f = interp1d(t, ux, fill_value='extrapolate')
    t = np.linspace(0.001, 0.999, 500)  # Bring it in to avoid /0
    ux = f(t)
    popt, pcov = curve_fit(fit_sine, t, ux)  # Find offset position
    return popt[-1]


def plot_absolutephase_diff():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ L/\lambda $")
    # ax.set_ylabel(r"$ \phi_{r}-\phi_{{s}_{SPS}}/degrees $")
    ax.set_ylabel(r"$ \phi_{r}/deg $")

    t, ux, *_ = read_forces(f"{cwd}/0x0/1024/fort.9", interest='cp')
    s_sps = find_offset(t[t > 3], ux[t > 3])
    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        phi_r = find_offset(t[t > 3], ux[t > 3])  # - s_sps

        ax.scatter(case, phi_r * 180 / np.pi, color=colors[idx])

    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(
        f"{cwd}/figures/power_phase_diff_abs.pdf", bbox_inches="tight", dpi=300
    )


def plot_phase_diff():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(r"$ L/\lambda $")
    ax.set_ylabel(r"$ (\phi_{r}-\phi_{s})/deg $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='cp')
        phi_r = find_offset(t[t > 3], ux[t > 3])

        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/2D/fort.9", interest='cp')
        phi_s = find_offset(t[t > 3], ux[t > 3])

        ax.scatter(case, (phi_r - phi_s) * 180 / np.pi, color=colors[idx])

    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(
        f"{cwd}/figures/power_phase_diff.pdf", bbox_inches="tight", dpi=300
    )


def plot_thrust_avg():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ k_r/c $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='p')
        ax.scatter(case, np.mean(ux[t > 4]), color=colors[idx])

    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/thrust_avg.pdf", bbox_inches="tight", dpi=200
    )


def plot_thrust_rms():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ k_r/c $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='p')
        rms = np.sqrt((ux - np.mean(ux)) ** 2)
        ax.scatter(case, np.mean(rms[t > 4]), color=colors[idx])

    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/thrust_rms.pdf", bbox_inches="tight", dpi=200
    )


def plot_side_force_rms():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ k_r/c $")
    ax.set_ylabel(r"$ \overline{C_P} $")

    for idx, case in enumerate(cases):
        t, _, ux = read_forces(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/fort.9", interest='p')
        rms = np.sqrt((ux - np.mean(ux)) ** 2)
        ax.scatter(case, np.mean(rms[t > 4]), color=colors[idx])

    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/side_rms.pdf", bbox_inches="tight", dpi=200
    )


def main():
    # plot_power()
    # plot_phase_av()
    # plot_power_avg()
    plot_power_diff()
    plot_thrust_diff()
    plot_side_diff()
    # plot_absolutephase_diff()
    # plot_phase_diff()
    # plot_thrust_rms()
    # plot_side_force_rms()


if __name__ == "__main__":
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    z_size = np.array([32, 32, 32, 32, 16, 16, 16, 16, 16, 4, 4, 4, 4, 2])
    main()
