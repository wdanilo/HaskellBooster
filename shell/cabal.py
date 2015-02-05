# coding=utf-8
import subprocess
import os
import sys

subprocess.Popen(['cabal', '--ghc-options="-F -pgmF%s/preprocessor/preprocessor.py"' % os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))] + sys.argv[1:])