# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:06:05 2022

@author: ilmar
"""
import subprocess
import glob

filenames = glob.glob("graphs/trees/*")

with open('results2.txt', 'w') as f:
    for file in filenames:
        print(f'{file[13:-4]}')
        subprocess.check_call(['python', 'ground_truth.py',
                               '--input', file], stdout=f)
        
        try:
            subprocess.check_call(['python', 'spectral_sequencing.py',
                               '--input', file], stdout=f)
        except Exception as e:
            # probably due to memmory insufficiency
            print(e)
    
        subprocess.check_call(['python', 'random_normal.py',
                               '--input', file], stdout=f)
        subprocess.check_call(['python', 'local_search.py',
                               '--input', file], stdout=f)
        