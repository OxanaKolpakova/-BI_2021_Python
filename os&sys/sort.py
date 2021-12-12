#!/usr/bin/python3
 
import sys
import argparse

filenames = sys.argv[1:]
all_list = []
for filename in filenames:
	with open(filename) as file:
		for line in file:
			all_list.append(line)
print(*sorted(all_list))
