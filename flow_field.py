#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import array
import os
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors
plt.style.use(["science", "grid"])

from lotusvis.assign_props import AssignProps

from tqdm import tqdm


def plot_vort_mag(fn_save: str, flow: object, mag: array, **kwargs) -> None:
    x = np.mean(flow.X, axis=2)
    y = np.mean(flow.Y, axis=2)    

    fig, ax = plt.subplots(figsize=(7, 4))
    divider = make_axes_locatable(ax)

    ax.set_xlim(kwargs.get("xlim", (-0.1, 2.0)))
    ax.set_ylim(kwargs.get("ylim", (np.min(y), np.max(y))))

    lim = [0., 0.14]

    norm = colors.Normalize(vmin=lim[0], vmax=lim[1])
    levels = np.linspace(lim[0], lim[1], 31)

    _cmap = sns.color_palette("Reds", as_cmap=True)

    cs = ax.contourf(
        x,
        y,
        mag,
        levels=levels,
        vmin=lim[0],
        vmax=lim[1],
        norm=norm,
        cmap=_cmap,
        extend="both",
    )

    # ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    # fig.add_axes(ax_cb)
    # plt.colorbar(cs, cax=ax_cb)
    # ax_cb.yaxis.tick_right()
    # ax_cb.yaxis.set_tick_params(labelright=True)
    # ax_cb.set_ylabel("$ | \Omega | $", rotation=0)

    # # plt.setp(ax_cb.get_yticklabels()[::2], visible=False)
    ax.set_aspect(1)

    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    plt.savefig(fn_save, dpi=300, transparent=True)
    plt.close()


def plot_zoomed_z(fn_save: str, flow: object, vortz: array, **kwargs) -> None:
    x = np.mean(flow.X, axis=2)
    y = np.mean(flow.Y, axis=2)    

    fig, ax = plt.subplots(figsize=(14, 4))
    divider = make_axes_locatable(ax)

    ax.set_xlim(kwargs.get("xlim", (0., 0.5)))
    ax.set_ylim(kwargs.get("ylim", (-0.1, 0.1)))

    lim = [-0.2, 0.2]

    norm = colors.Normalize(vmin=lim[0], vmax=lim[1])
    levels = np.linspace(lim[0], lim[1], 61)

    _cmap = sns.color_palette("seismic", as_cmap=True)

    cs = ax.contourf(
        x,
        y,
        vortz,
        levels=levels,
        vmin=lim[0],
        vmax=lim[1],
        norm=norm,
        cmap=_cmap,
        extend="both",
    )

    # ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    # fig.add_axes(ax_cb)
    # plt.colorbar(cs, cax=ax_cb)
    # ax_cb.yaxis.tick_right()
    # ax_cb.yaxis.set_tick_params(labelright=True)
    # ax_cb.set_ylabel("$ \omega_z $", rotation=0)

    # plt.setp(ax_cb.get_yticklabels()[::2], visible=False)
    ax.set_aspect(1)

    plt.savefig(fn_save, dpi=600)
    plt.close()


def vorticity_x(flow) -> array:
    dv_dz = np.gradient(flow.V, axis=2, edge_order=2)
    dw_dy = np.gradient(flow.W, axis=1, edge_order=2)
    return dw_dy - dv_dz


def vorticity_y(flow) -> array:
    du_dz = np.gradient(flow.U, axis=2, edge_order=2)
    dw_dx = np.gradient(flow.W, axis=0, edge_order=2)
    return du_dz - dw_dx


def vorticity_z(flow) -> array:
    dv_dx = np.gradient(flow.V, axis=1, edge_order=2)
    du_dy = np.gradient(flow.U, axis=0, edge_order=2)
    return dv_dx - du_dy


def vorticity_mag(flow) -> array:
    try:
        mag = np.sqrt(vorticity_x(flow)**2 + vorticity_y(flow)**2 + vorticity_z(flow)**2)
    except ValueError:
        print('2D field, falling bag to mag of vortZ')
        mag =  np.sqrt(vorticity_z(flow)**2)
    return mag


def plot_phase_avg() -> None:
    for idx, case in enumerate(cases):
        os.system(f'mkdir -p {cwd}/{case}x{case}/vort_mag')
        phase_average = np.load(f"{cwd}/{case}x{case}/{str(cs[idx])}/phase_average.npy")
        for ident, snap in tqdm(enumerate(phase_average)):
            flow = AssignProps(snap)
            mag = vorticity_mag(flow)
            mag = np.mean(mag, axis=2)
            plot_vort_mag(f'{cwd}/{case}x{case}/vort_mag/{str(ident)}.pdf', flow, mag)


def plot_phase_avg_2d() -> None:
    for idx, case in enumerate(cases):
        os.system(f'mkdir -p {cwd}/{case}x{case}/vort_mag_2d')
        phase_average = np.load(f"{cwd}/{case}x{case}/2D/phase_average.npy")
        for ident, snap in tqdm(enumerate(phase_average), ascii=True):
            flow = AssignProps(snap)
            mag = vorticity_mag(flow)
            mag = np.mean(mag, axis=2)
            plot_vort_mag(f'{cwd}/{case}x{case}/vort_mag_2d/{str(ident)}.pdf', flow, mag)


def plot_phase_avg_diff() -> None:
    for idx, case in enumerate(cases):
        os.system(f'mkdir -p {cwd}/{case}x{case}/diff')
        phase_average_r = np.load(f"{cwd}/{case}x{case}/{str(cs[idx])}/phase_average.npy")
        phase_average_s = np.load(f"{cwd}/{case}x{case}/2D/phase_average.npy")

        for ident, (snap_r, snap_s) in tqdm(enumerate(zip(phase_average_r, phase_average_s)), ascii=True):
            flow_r = AssignProps(snap_r)
            mag_r = vorticity_mag(flow_r)
            mag_r = np.mean(mag_r, axis=2)

            flow_s = AssignProps(snap_s)
            mag_s = vorticity_mag(flow_s)
            mag_s = np.mean(mag_s, axis=2)

            plot_vort_mag(f'{cwd}/{case}x{case}/diff/{str(ident)}.png', flow_s, mag_r-mag_s)


def plot_zoomed() -> None:
    for idx, case in enumerate(cases):
        os.system(f'mkdir -p {cwd}/{case}x{case}/zoomed')
        phase_average = np.load(f"{cwd}/{case}x{case}/{str(cs[idx])}/phase_average.npy")
        for ident, snap in tqdm(enumerate(phase_average)):
            flow = AssignProps(snap)
            vortz = vorticity_z(flow)
            vortz = np.mean(vortz, axis=2)
            plot_zoomed_z(f'{cwd}/{case}x{case}/zoomed/{str(ident)}.eps', flow, vortz)

def plot_zoomed_2d() -> None:
    for idx, case in enumerate(cases):
        os.system(f'mkdir -p {cwd}/{case}x{case}/zoomed_2d')
        phase_average = np.load(f"{cwd}/{case}x{case}/2D/phase_average.npy")
        for ident, snap in tqdm(enumerate(phase_average)):
            flow = AssignProps(snap)
            vortz = vorticity_z(flow)
            vortz = np.mean(vortz, axis=2)
            plot_zoomed_z(f'{cwd}/{case}x{case}/zoomed_2d/{str(ident)}.eps', flow, vortz)


def main() -> None:
    plot_phase_avg()
    # plot_phase_avg_2d()
    # plot_phase_avg_diff()
    # plot_zoomed()
    # plot_zoomed_2d()

if __name__ == "__main__":
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    # z_size = np.array([32, 32, 32, 32, 16, 16, 16, 16, 16, 4, 4, 4, 4, 2])
    cases = np.array([0, 16, 32, 48])
    cs = np.array([1024, 1024, 1024, 1056])
    main()