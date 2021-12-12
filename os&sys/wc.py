#!/usr/bin/python3

import sys
import argparse
if len(sys.argv) == 1:
    print("Usage: {} FILENAMEs".format(sys.argv[0]))
else:
    if sys.argv[1] == "l" or sys.argv[1] == "w" or sys.argv[1] == "c":
        filenames = sys.argv[2:]
    else:
        filenames = sys.argv[1:]
    all_lines = 0
    all_words = 0
    all_chars = 0
    for filename in filenames:
        lines = 0
        words = 0
        chars = 0
        with open(filename) as file:
            for line in file:
                lines += 1
                words += len(line.split())
                chars += len(line)
        if sys.argv[1] == "l":
            print(lines, filename)
        elif sys.argv[1] == "w":			print(words, filename)
        elif sys.argv[1] == "c":
            print(chars, filename)
        else:
            print(lines, words, chars, filename)
        all_lines += lines
        all_words += words
        all_chars += chars
    if sys.argv[1] == "l":
        print(all_lines, "total")
    elif sys.argv[1] == "w":
        print(all_words, "total")
    elif sys.argv[1] == "c":
        print(all_chars, "total")
    else:
        print(all_lines, all_words, all_chars, "total")
