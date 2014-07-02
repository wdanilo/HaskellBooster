#!/usr/bin/python3.3

import sys
import re

def main():

    name       = sys.argv[1]
    inputPath  = sys.argv[2]
    outputPath = sys.argv[3]

    with open(inputPath, "r") as file:
        txt = file.read()

    pat = re.compile(r'^[ \t]*!{-#\s*LANGUAGE\s*(?P<name>[a-zA-Z]*)\s*(?P<opts>.*)#-}', re.MULTILINE)

    matches = []
    for match in pat.finditer(txt):
        name = match.group('name')
        matches.append(match)
    names = [match.group('name') for match in matches]
    
    matches.reverse()
    for match in matches:
        txt = txt[:match.start()] + txt[match.end():]

    for name in names:
        modname = 'passes.'+name
        __import__(modname)
        module = sys.modules[modname]
        txt = module.run(txt)

    with open(outputPath, "w") as file:
        file.write(txt)

main()

