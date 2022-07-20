#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np

from lotusvis.flow_field import ReadIn
from lotusvis.decompositions import Decompositions


def save_phase_avg():
    cwd = os.getcwd()
    
    for idx, case in enumerate(cases):
        fns = os.listdir(f"{cwd}/{case}/{str(cs[idx])}")
        if 'phase_average.npy' in fns:
            print(f'{case} has a np binary')
        else:
            phase_av = Decompositions(f"{cwd}/{case}/{str(cs[idx])}", "fluid", length_scale=cs[idx]).phase_average(4)
            np.save(f"{cwd}/{case}/{str(cs[idx])}/phase_average.npy", phase_av)
            print(f'Saved phase_average.npy for {case}')
            del phase_av


def save_phase_avg_2d():
    for idx, case in enumerate(cases):
        fns = os.listdir(f"{cwd}/{case}/2D")
        if 'phase_average.npy' in fns:
            print(f'{case} has a np binary')
        else:
            phase_av = Decompositions(f"{cwd}/{case}/2D", "fluid", length_scale=cs[idx]).phase_average(4)
            np.save(f"{cwd}/{case}/2D/phase_average.npy", phase_av)
            print(f'Saved phase_average.npy for {case}')
            del phase_av


def main():
    # save_phase_avg()
    save_phase_avg_2d()


if __name__ == "__main__":
    cwd = os.getcwd()
    cases = ['32x32', '20x20', '16x16', '12x12']
    cs = np.array([1024, 1020, 1024, 1008])
    cases = ['16x16']
    cs = np.array([1024])
    main()
