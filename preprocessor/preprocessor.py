#!/usr/bin/python3.3

import sys
import os
import subprocess
from subprocess import PIPE

scriptPath = os.path.dirname(os.path.realpath(__file__))
passesPath = os.path.join(scriptPath, 'passes')

def main():

    passes = (os.listdir(passesPath))
    
    name       = sys.argv[1]
    inputPath  = sys.argv[2]
    outputPath = sys.argv[3]

    with open(inputPath, "r") as file:
        input = file.read()

    with open(outputPath, "w") as file:
        input = file.write(input)

    for fpass in passes:
        out = subprocess.Popen([os.path.join(passesPath,fpass), name, outputPath, outputPath], stdout=PIPE).stdout.read()

main()