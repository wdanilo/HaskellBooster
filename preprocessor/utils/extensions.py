import re

def consumeExt(name, input):
    ext   = langExtension(name)
    match = ext.search(input)
    if match: 
    	return (True, ext.sub('', input), match.group('opts').split())
    else:     return (False, input, [])

def langExtension(name):
    return re.compile(r'^[ \t]*!{-#\s*LANGUAGE\s*' + name + r'\s*(?P<opts>.*)#-}', re.MULTILINE)