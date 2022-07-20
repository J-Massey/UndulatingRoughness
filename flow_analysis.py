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

from inout import read_forces
from scipy.interpolate import interp1d
from tqdm import tqdm



def plot_vortx_integral():
    cwd = os.getcwd()
    fig, ax = plt.subplots(figsize=(4, 4))

    ax.set_ylabel(r'$ \int \omega_x $')
    ax.set_xlabel(r"$ \Delta y/h $")
    colours = sns.color_palette('Greens', 10)
    cases = ['52x52', '44x44', '36x36', '28x28', '24x24', '20x20', '16x16', '12x12', '8x8']
    cs = np.array([1040, 1012, 1044, 1036, 1056, 1020, 1024, 1008, 1024])

    slice_int = np.zeros(len(cs))
    average_int = np.zeros(len(cs))
    total_int = []

    for idx, case in tqdm(enumerate(cases), ascii=True):
        phase_average = np.load(f"{cwd}/{case}/{str(cs[idx])}/phase_average.npy")
        cell_volume = 4/cs[idx] * 2/cs[idx]
        
        temp = []
        for ident, snap in enumerate(phase_average):
            flow = AssignProps(snap)
            vortx = vorticity_x(flow)*cell_volume
            mag = np.sqrt((vortx)**2)
            temp.append(np.trapz(mag.flat))
            del flow
        total_int.append(temp)
        del phase_average

    total_int = np.array(total_int)
    total_int = total_int.T
    for idx, loop in enumerate(total_int):
        ax.plot(range(len(cases)), loop, marker="+", color=colours[idx], label=f"$t={str(idx/10)}$")

    # ax.set_xscale("log")
    ax.set_xticks(range(len(cases)))
    ax.set_xticklabels(cases)
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/vortx_integral.png", dpi=300, transparent=False
    )
    plt.close()


def plot_vortx_body_integral(directory, cs):
    fig, ax = plt.subplots(figsize=(4, 4))

    ax.set_ylabel(r'$ \int \omega_x $ error')
    ax.set_xlabel(r"$ \Delta y/h $")

    slice_int = np.zeros(len(cs))
    average_int = np.zeros(len(cs))
    total_int = np.zeros(len(cs))
    for idx, c in enumerate(cs):
        flow = FlowBase(f"{directory}/re12000/{c}", "fluid", length_scale=c)

        cell_volume = 4/c * 2/c * 4/c
        vortx = vorticity_x(flow)*cell_volume

        # Trim to the body
        vortx = np.ma.masked_where(flow.X>1, vortx).filled(0)
        mag = np.sqrt((vortx)**2)

        slice= mag[ :, np.shape(vortx)[1]//2, :]
        avg = np.mean(mag, axis=1)

        slice_int[idx] = np.trapz(slice.flat)
        average_int[idx] = np.trapz(avg.flat)
        total_int[idx] = np.trapz(mag.flat)

    slice_int = (slice_int-slice_int[-1])/slice_int
    average_int = (average_int-average_int[-1])/average_int
    total_int = (total_int-total_int[-1])/total_int

    # ax.plot(200/np.array(cs), slice_int, marker="+", color="steelblue", label="Midplane slice")
    ax.plot(200/np.array(cs), average_int, marker="*", color="red", label="y average")
    ax.plot(200/np.array(cs), total_int, marker=".", color="green", label="Total field (just body, no wake)")

    # ax.set_xscale("log")
    ax.loglog()
    ax.legend()
    plt.savefig(
        f"{directory}/figures/vortx_body_integral_convergence.pdf", dpi=300, transparent=False
    )
    plt.close()


def plot(fn_save, c, flow, **kwargs):
    cwd = os.getcwd()

    x = np.mean(flow.X, axis=0)
    y = np.mean(flow.Z, axis=0)

    mag = vorticity_x(flow)
    # mag = np.ma.masked_where(flow.X>1, mag).filled(0)
    mag = np.mean(mag, axis=0)
    

    plt.style.use(["science", "grid"])
    fig, ax = plt.subplots(figsize=(14, 4))
    divider = make_axes_locatable(ax)
    # Plot the window of interest
    ax.set_xlim(kwargs.get("xlim", (0.25, 2.0)))
    ax.set_ylim(kwargs.get("ylim", (np.min(y), np.max(y))))

    lim = [-0.013, 0.013]
    # lim = kwargs.get('lims', lim)

    norm = colors.Normalize(vmin=lim[0], vmax=lim[1])
    levels = np.linspace(lim[0], lim[1], 31)

    _cmap = sns.color_palette("seismic", as_cmap=True)

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

    ax_cb = divider.new_horizontal(size="5%", pad=0.05)
    fig.add_axes(ax_cb)
    plt.colorbar(cs, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=True)
    ax_cb.set_ylabel("$ \Omega_x $", rotation=0)

    # plt.setp(ax_cb.get_yticklabels()[::2], visible=False)
    ax.set_aspect(1)

    plt.savefig(fn_save, dpi=200, transparent=True)
    plt.close()


def vorticity_z(flow):
    dv_dx = np.gradient(flow.V, axis=0, edge_order=2)
    du_dy = np.gradient(flow.U, axis=1, edge_order=2)
    return dv_dx - du_dy


def vorticity_x(flow):
    dv_dz = np.gradient(flow.V, axis=2, edge_order=2)
    dw_dy = np.gradient(flow.W, axis=1, edge_order=2)
    return dv_dz - dw_dy


def vorticity_y(flow):
    du_dz = np.gradient(flow.U, axis=2, edge_order=2)
    dw_dx = np.gradient(flow.W, axis=0, edge_order=2)
    return du_dz - dw_dx

def vorticity_mag(flow):
    return np.sqrt(vorticity_x**2 + vorticity_y**2 + vorticity_z**2)


def save_phase_avg():
    cwd = os.getcwd()
    cases = ['52x52', '48x48', '44x44', '40x40', '36x36', '32x32', '28x28', '24x24', '20x20', '16x16', '12x12', '8x8', '4x4']
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024])
    for idx, case in enumerate(cases):
        fns = os.listdir(f"{cwd}/{case}/{str(cs[idx])}")
        if 'phase_average.npy' in fns:
            break
        phase_av = Decompositions(f"{cwd}/{case}/{str(cs[idx])}", "fluid", length_scale=cs[idx]).phase_average(4)
        print(np.shape(phase_av))
        np.save(f"{cwd}/{case}/{str(cs[idx])}/phase_average.npy", phase_av)


def plot_phase_avgs():
    cwd = os.getcwd()
    cases = ['64x64', '52x52', '44x44', '36x36', '28x28', '24x24', '20x20', '16x16', '12x12', '8x8']
    cs = np.array([1020, 1040, 1012, 1044, 1036, 1056, 1020, 1024, 1008, 1024])
    for idx, case in enumerate(cases):
        phase_average = np.load(f"{cwd}/{case}/{str(cs[idx])}/phase_average.npy")
        print(np.shape(phase_average))
        for ident, snap in enumerate(phase_average):
            flow = AssignProps(snap)
            # cell_volume = 4/cs[idx] * 2/cs[idx]
            plot(f'{cwd}/figures/{case}_{str(ident)}.pdf', cs[idx], flow)
    

def _phase_avg(t, force):
    t = t%1
    f = interp1d(t, force, fill_value='extrapolate')
    t_avg, force_cycle_avg = f(np.linspace(0, 1, 200))
    return np.linspace(0, 1, 200), force_cycle_avg


def plot_power():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlabel(f"$ t $")
    ax.set_ylabel(r"$ C_P $")

    power = np.array
    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{case}/{str(cs[idx])}/fort.9", interest='cp')
        ax.plot(t[t>4], ux[t>4], color=colors[idx], label=case)
    
    ax.legend(loc='upper right')
    plt.savefig(
        f"{cwd}/figures/power_phase.png", bbox_inches="tight", dpi=300
    )


def plot_power_avg():
    cwd = os.getcwd()
    colors = sns.color_palette('husl', len(cs))
     
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(f"$ t $")
    ax.set_ylabel(r"$ C_P $")

    for idx, case in enumerate(cases):
        t, ux, *_ = read_forces(f"{cwd}/{case}/{str(cs[idx])}/fort.9", interest='cp')
        ax.scatter(idx, np.mean(ux[t>4]), color=colors[idx])
    
    ax.set_xticks(range(len(cases)))
    ax.set_xticklabels(cases)
    # ax.legend()
    plt.savefig(
        f"{cwd}/figures/power_avg.pdf", bbox_inches="tight", dpi=200
    )


def main():
    cwd = os.getcwd()
    # save_phase_avg()
    plot_power()
    plot_power_avg()
    # plot_vortx_integral()


if __name__ == "__main__":
    cases = ['52x52', '48x48', '44x44', '40x40', '36x36', '32x32', '28x28', '24x24', '20x20', '16x16', '12x12', '8x8', '4x4']
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    # cases = ['0x64', '0x32', '0x16', '0x8', '0x4']
    # cs = np.array([1024, 1024, 1024, 1024, 1024])
    main()
