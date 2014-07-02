import re

def run(txt):
    pattern = re.compile(r'instance(?P<head>.*)<=(?P<premise>.*)where')
    txt     = pattern.sub(process, txt)
    return txt

def process(match):
    return "instance " + match.group('premise') + '=>' + match.group('head') + " where"
    