import argparse
import os
import numpy as np
import pandas as pd

from apt_importers import *

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pos-file', dest='pos_file', required=True)
parser.add_argument('-r', '--rrng-file', dest='rrng_file', required=True)
parser.add_argument('-t', '--input-type', dest='input_type', required=True)
options = parser.parse_args()

input_type = options.input_type
pos_file = options.pos_file
rrng_file = options.rrng_file
filename = os.path.split(pos_file)[-1].replace('.','_')

# Convert the binary pos file to a readable csv file.
if input_type == 'pos':
    pos = read_pos(pos_file)
    ions, rrngs = read_rrng(rrng_file)
    pos_comp = label_ions(pos, rrngs)
    pos_elements = deconvolve(pos_comp)
    # pos.to_csv('output/{fn}_raw.csv'.format(fn=filename))
    # pos_comp.to_csv('output/{fn}_comp.csv'.format(fn=filename))
    pos_elements.to_csv('output/{fn}.csv'.format(fn=filename))

elif input_type == 'epos':
    epos = read_epos(pos_file)
    ions, rrngs = read_rrng(rrng_file)
    epos_comp = label_ions(epos, rrngs)
    epos_elements = deconvolve(epos_comp)
    # epos.to_csv('output/{fn}_raw.csv'.format(fn=filename))
    # epos_comp.to_csv('output/{fn}_comp.csv'.format(fn=filename))
    epos_elements.to_csv('output/{fn}.csv'.format(fn=filename))