import re

def run(txt):
    pattern = re.compile(r'```[^`]*```')
    return pattern.sub(process, txt)

def process(match):
    txt = match.group()[3:-3]
    try:    
        out = str(eval(txt))
    except: 
        exec(txt, globals(), globals())
        out = ''
    return out
