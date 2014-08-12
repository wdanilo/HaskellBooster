import re

def run(txt):
    ws       = r'''[ \t]'''
    name     = r'''[\w']+'''
    instPat1 = re.compile(r'(?P<decl>instance{ws})(?P<head>.*)<=(?P<premise>.*)(?P<end>where)'.format(**locals()))
    instPat2 = re.compile(r'(?P<decl>instance{ws})(?P<head>.*)<=(?P<premise>.*)(?P<end>$)'.format(**locals()), re.MULTILINE)
    funcPat  = re.compile(r'(?P<decl>({name}{ws}::){ws})(?P<head>.*)<=(?P<premise>.*)(?P<end>$)'.format(**locals()), re.MULTILINE)
    txt      = instPat1.sub(process, txt)
    txt      = instPat2.sub(process, txt)
    txt      = funcPat.sub(process, txt)

    return txt

def process(match):
    return match.group('decl') + match.group('premise') + '=>' + match.group('head') + ' ' + match.group('end')
    
# tst = '''instance AllArgs (Arg name val, args) out <= AllArgs args out'''

# print(run(tst))