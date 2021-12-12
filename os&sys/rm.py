#!/usr/bin/python3

import sys
import shutil
import os

if sys.argv[1] == "r":
    for i in range(2, len(sys.argv)):
        print(sys.argv[i])
        shutil.rmtree(sys.argv[i])
else:
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
        os.remove(sys.argv[i])
