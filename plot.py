# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:39:04 2022

@author: ilmar
"""
import matplotlib.pyplot as plt

with open('results2.txt', 'r') as f:
    lines = f.readlines()

names = []
ratios = []
times = []

for i in range(14):
    names.append(lines[i * 17].split()[0])
    optimal = int(lines[i * 17 + 2].split()[0])
    res = dict()
    res_t = dict()
    for j in range(8):
        name = lines[i * 17 + 1 + 2 * j]
        result = int(lines[i * 17 + 2 + 2 * j].split()[0])
        time = float(lines[i * 17 + 2 + 2 * j].split()[1])
        if j > 1:
            res[name] = result / optimal
        res_t[name] = time
    ratios.append(res)
    times.append(res_t)

for i in range(14):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 15))
    fig.suptitle(names[i], fontsize=30)
    algs = list(ratios[i].keys())
    rat = list(ratios[i].values())
    ax1.bar(algs,rat, color='black')
    ax1.set_ylabel('Ratio', fontsize=20)
    ax1.tick_params(labelrotation=20, labelsize=14)
    algs = list(times[i].keys())
    time = list(times[i].values())
    ax2.bar(algs, time, color='black')
    ax2.set_ylabel('Execution time(s)', fontsize=20)
    ax2.tick_params(labelrotation=20, labelsize=14)
    plt.savefig(f'plots/{names[i]}.png')