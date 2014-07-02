import re

def run(txt):
    pattern = re.compile(r'"""[^"]*"""')
    return pattern.sub(process, txt)

def process(match):
    txt = match.group()[3:-3]
    return 'unlines [\n\t"' + '",\n\t"'.join(txt.split('\n')) + '"]'
