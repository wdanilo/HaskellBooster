import re

def consumeExt(name, input):
    ext = langExtension(name)
    if ext.search(input): return (True, ext.sub('', input))
    else:                 return (False, input)

def langExtension(name):
    return re.compile(r'^[ \t]*!{-#\s*LANGUAGE\s*' + name + r'\s*#-}', re.MULTILINE)