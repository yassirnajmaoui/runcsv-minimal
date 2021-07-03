#!/usr/bin/python3
import runcsv as rcsv
import csv
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Process a CSV file')
parser.add_argument('-i', help='Input csv file')
parser.add_argument('-o', help='Output csv file')
args = parser.parse_args()

input_file = args.i
output_file = args.o

#s_l = []
with open(input_file, 'r', newline='') as file:
	reader = csv.reader(file)
	s_l = list(reader)

s_l_arr = np.array(s_l, dtype=object)
print(s_l_arr.shape)

rcsv.s.resize(s_l_arr.shape,refcheck=False)
rcsv.s[:,:] = np.copy(s_l_arr)
rcsv.p.resize(rcsv.s.shape,refcheck=False)
rcsv.o.resize(rcsv.s.shape,refcheck=False)
rcsv.f.resize(rcsv.s.shape,refcheck=False)

for i in np.arange(rcsv.s.shape[0]):
	for j in np.arange(rcsv.s.shape[1]):
		rcsv.process_cell(i,j)

with open(output_file, 'w+') as file:
	writer = csv.writer(file)
	writer.writerows(rcsv.f)

print(rcsv.f)



