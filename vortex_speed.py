#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np
from tqdm import tqdm

import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.colors as colors

plt.style.use(["science", "grid"])

from lotusvis.flow_field import ReadIn
from lotusvis.decompositions import Decompositions
from lotusvis.assign_props import AssignProps


def ddx(u, x=None, acc=1):
    """
	:param u: n-dimensional field.
	:return: the first- or second-acc derivative in the i direction of (n>=1 dimensional) field.
	"""
    return np.gradient(u, axis=0, edge_order=2)


def ddy(u, y=None, acc=1):
    """
	:param u: n-dimensional field.
	:return: the first-acc derivative in the j direction of (n>=2 dimensional) field.
	"""
    return np.gradient(u, axis=1, edge_order=2)


def ddz(u, z=None):
    """
	:param u: n-dimensional field.
	:return: the first-acc derivative in the j direction of (n>=2 dimensional) field.
	"""
    return np.gradient(u, axis=2, edge_order=2)


def _J3(flow: object) -> np.array:
    """
	Calculate the velocity gradient tensor
	:param u: Horizontal velocity component
	:param v: Vertical velocity component
	:param w: Spanwise velocity component
	:return: np.array (tensor) of the velocity gradient
	"""
    a11, a12, a13 = ddx(flow.U), ddy(flow.U), ddz(flow.U)
    a21, a22, a23 = ddx(flow.V), ddy(flow.V), ddz(flow.V)
    a31, a32, a33 = ddx(flow.W), ddy(flow.W), ddz(flow.W)
    return np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])


def Q3(flow) -> np.array:
    J = _J3(flow)
    S = 0.5 * (J + np.transpose(J, (1, 0, 2, 3, 4)))
    R = 0.5 * (J - np.transpose(J, (1, 0, 2, 3, 4)))

    S_mag = np.linalg.norm(S, ord='fro', axis=(0, 1))  # Falta sqrt(2)
    # S_mag2 = np.sqrt(np.trace(np.dot(S, S.T))) # Falta sqrt(2)
    # S_mag3 = np.sqrt(np.tensordot(S,S,axes=2)) # Falta sqrt(2)

    # print(np.sum(S_mag))
    # print(np.sum(S_mag2))
    R_mag = np.linalg.norm(R, ord='fro', axis=(0, 1))

    Q = 0.5 * (R_mag ** 2 - S_mag ** 2)

    return Q


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


def vorticity_mag(flow):
    try:
        mag = np.sqrt(vorticity_x(flow) ** 2 + vorticity_y(flow) ** 2 + vorticity_z(flow) ** 2)
    except ValueError:
        print('2D field, falling bag to mag of vortZ')
        mag = np.sqrt(vorticity_z(flow) ** 2)
    return mag


def plot_quantmax(fn_save: str, flow: object, quantity: np.array, **kwargs) -> None:
    x = np.mean(flow.X, axis=2)
    y = np.mean(flow.Y, axis=2)

    fig, ax = plt.subplots(figsize=(14, 4))

    ax.set_xlim(kwargs.get("xlim", (0., 1.5)))
    ax.set_ylim(kwargs.get("ylim", (-0.12, 0.12)))

    lim = [-0.2, 0.2]

    norm = colors.Normalize(vmin=lim[0], vmax=lim[1])
    levels = np.linspace(lim[0], lim[1], 61)

    _cmap = sns.color_palette("seismic", as_cmap=True)

    cs = ax.contourf(
        x,
        y,
        quantity,
        levels=levels,
        vmin=lim[0],
        vmax=lim[1],
        norm=norm,
        cmap=_cmap,
        extend="both",
    )

    _, xbox, ybox = max_box(quantity, x, y)

    ax.scatter(xbox, ybox, zorder=999, c='orange')

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


def max_box(quantity, x, y):
    quantity_box, xbox, ybox = quantity[x > 0.2], x[x > 0.2], y[x > 0.2]
    quantity_box, xbox, ybox = quantity_box[ybox > 0], xbox[ybox > 0], ybox[ybox > 0]
    quantity_box, xbox, ybox = quantity_box[xbox < 0.35], xbox[xbox < 0.35], ybox[xbox < 0.35]
    return quantity_box, xbox[np.argmax(quantity_box)], ybox[np.argmax(quantity_box)]


def _get_Q():
    for idx, case in tqdm(enumerate(cases), ascii=True):
        os.system(f"mkdir -p {cwd}/{str(case)}x{str(case)}/vort_speed")
        phase_average = np.load(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
        # phase_average_2d = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")
        cell_volume = 4 / cs[idx] * 2 / cs[idx] * 4 / cs[idx]

        temp = []
        for ident, snap in enumerate(phase_average):
            flow = AssignProps(snap)
            # flow_2d = AssignProps(snap_2d)
            q_field = Q3(flow)
            plot_quantmax(f"{cwd}/{str(case)}x{str(case)}/vort_speed/q_{str(ident)}.png", flow,
                          np.mean(q_field, axis=2))
            x_pos = np.mean(flow.X[np.where(np.max(q_field))])
            temp.append(x_pos)

    return temp


def _get_vort_max():
    for idx, case in tqdm(enumerate(cases), ascii=True):
        os.system(f"mkdir -p {cwd}/{str(case)}x{str(case)}/vort_speed")
        phase_average = np.load(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
        phase_average_2d = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")
        cell_volume = 4 / cs[idx] * 2 / cs[idx] * 4 / cs[idx]

        temp = []
        for ident, (snap, snap_2d) in enumerate(zip(phase_average, phase_average_2d)):
            flow = AssignProps(snap)
            flow_2d = AssignProps(snap_2d)

            vort_max = vorticity_mag(flow)
            plot_quantmax(f"{cwd}/{str(case)}x{str(case)}/vort_speed/vortmax_{str(ident)}.png", flow,
                          np.mean(vort_max, axis=2))
            vort_max_2d = vorticity_mag(flow_2d)
            # plot_quantmax(f"{cwd}/{str(case)}x{str(case)}/vort_speed/2d_vortmax_{str(ident)}.png", flow_2d, np.mean(vort_max_2d, axis=2))

            x_pos = np.mean(flow.X[np.where(np.max(vort_max))])
            temp.append(x_pos)

    return temp


def plot_max_vort(x_pos: list, t: list) -> None:
    colors = sns.color_palette('husl', len(cases))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ t $")
    ax.set_ylabel(r"$ x $")

    for idx, case in enumerate(cases):
        print(indicies[idx], x_pos[idx])
        # position = [x_pos[idx][p] for p in indicies[idx]]
        ax.scatter(indicies[idx], x_pos[idx], color=colors[idx], label=str(case))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(
        f"{cwd}/figures/vort_speed.eps", bbox_inches="tight", dpi=300
    )


def plot_vort_speed(x_pos: list, t: list) -> None:
    colors = sns.color_palette('husl', len(cases))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ c/\lambda $")
    ax.set_ylabel(r"$ \Gamma_{\vec{u}} $")

    for idx, case in enumerate(cases):
        grad = np.mean(np.gradient(indicies[idx], x_pos[idx]))
        ax.scatter(case, grad, color=colors[idx], label=str(case))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(
        f"{cwd}/figures/vort_speed.eps", bbox_inches="tight", dpi=300
    )


def plot_vort_speed_diff(x_pos: list, x_pos_2d: list) -> None:
    colors = sns.color_palette('husl', len(cases))

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.set_xlabel(r"$ c/\lambda $")
    ax.set_ylabel(r"$ \Gamma_{\vec{u}} $")

    for idx, case in enumerate(cases):
        grad = np.mean(np.gradient(indicies[idx], x_pos[idx]))
        grad_2d = np.mean(np.gradient(indicies_2d[idx], x_pos_2d[idx]))
        diff = grad - grad_2d

        ax.scatter(case, diff, color=colors[idx], label=str(case))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(
        f"{cwd}/figures/vort_speed_diff.pdf", bbox_inches="tight", dpi=300
    )


def max_vort_position() -> list:
    x_coords, x_coords_2d = [], []
    for idx, case in tqdm(enumerate(cases), ascii=True):
        os.system(f"mkdir -p {cwd}/{str(case)}x{str(case)}/vort_speed")
        phase_average = np.load(f"{cwd}/{str(case)}x{str(case)}/{str(cs[idx])}/phase_average.npy")
        phase_average_2d = np.load(f"{cwd}/{str(case)}x{str(case)}/2D/phase_average.npy")
        cell_volume = 4 / cs[idx] * 2 / cs[idx] * 4 / cs[idx]

        temp, temp2d = [], []
        for ind in indicies[idx]:
            flow = AssignProps(phase_average[ind])
            flow_2d = AssignProps(phase_average_2d[ind])

            vort_max = vorticity_mag(flow)
            vort_max_2d = vorticity_mag(flow_2d)

            _, xbox, ybox = max_box(np.mean(vort_max, axis=2), np.mean(flow.X, axis=2), np.mean(flow.Y, axis=2))
            _, xbox2d, ybox2d = max_box(np.mean(vort_max_2d, axis=2), np.mean(flow_2d.X, axis=2),
                                        np.mean(flow_2d.Y, axis=2))
            temp.append(xbox)
            temp2d.append(xbox2d)

        x_coords.append(temp)
        x_coords_2d.append(temp2d)
    return x_coords, x_coords_2d


def main():
    # _get_vort_max()
    # _get_Q()
    # plot_max_vort(max_vort_position(), indicies)
    plot_vort_speed(max_vort_position()[0], indicies)
    # plot_vort_speed_diff(max_vort_position()[0], max_vort_position()[1])


if __name__ == "__main__":
    cwd = os.getcwd()
    cases = np.array([52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0])
    cs = np.array([1040, 1056, 1012, 1040, 1044, 1024, 1036, 1056, 1020, 1024, 1008, 1024, 1024, 1024])
    indicies = np.array([[5, 6, 7], [5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8], [6, 7, 8], [6, 7, 8, 9],
                         [5, 6, 7, 8, 9], [3, 4, 5, 6, 8, 9], [3, 4, 5, 8], [7, 8, 9], [4, 8, 9],
                         [6, 7, 9], [0, 1, 3, 4], [3, 4, 5, 6, 7]], dtype=object)
    indicies_2d = np.array([[5, 6, 7, 8], [6, 7, 8], [6, 7, 8, 9], [6, 7, 8, 9], [6, 7, 8, 9],
                            [3, 4, 5, 6, 7, 8, 9], [6, 7, 9], [6, 7, 9], [6, 7, 9], [6, 7, 9],
                            [5, 6, 7, 9], [4, 5, 6, 9], [3, 4, 5, 6, 7], [3, 4, 5, 6, 7]], dtype=object)

    # cases = np.array([52, 48])
    # cs = np.array([1040, 1056],dtype=object)
    # indicies = np.array([[5,6,7], [5,6,7,8]], dtype=object)
    # indicies_2d = np.array([[5,6,7,8], [6,7,8]], dtype=object)
    main()
