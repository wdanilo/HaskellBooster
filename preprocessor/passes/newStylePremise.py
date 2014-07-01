#!/usr/bin/python3.3
import sys
import os
from copy import deepcopy
import re

scriptPath = os.path.dirname(os.path.realpath(__file__))
boostPath  = os.path.dirname(scriptPath)
sys.path.append(boostPath)


from utils.extensions import consumeExt, langExtension


def main():
    inputPath  = sys.argv[2]
    outputPath = sys.argv[3]

    with open(inputPath, "r") as file:
        input = file.read()

    txt = deepcopy(input)

    (ok, txt) = consumeExt('NewStylePremise', txt)
    if ok:
        pattern = re.compile(r'instance(?P<head>.*)<=(?P<premise>.*)where')
        txt     = pattern.sub(process, txt)

    with open(outputPath, "w") as file:
        input = file.write(txt)


def process(match):
    return "instance " + match.group('premise') + '=>' + match.group('head') + " where"

main()