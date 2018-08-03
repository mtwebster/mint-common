#!/usr/bin/python3

import sys
import subprocess

try:
    subprocess.run(["rm", "-f", sys.argv[1]])
    subprocess.run(["rm", "-f", "%s.desktop" % sys.argv[1]])
except Exception as e:
    if len(sys.argv) != 2:
        print("Not enough arguments")
    else:    
        print("Could not remove %s: %s" % (sys.argv[1], e.message))

sys.exit()