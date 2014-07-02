import re

def run(txt):
    pattern = re.compile(r'--.*')
    return pattern.sub('', txt)
    