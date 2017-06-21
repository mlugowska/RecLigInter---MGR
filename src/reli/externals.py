# -*- coding: utf-8 -*-
import os.path
from reli.call import call

# root = raw_input('Enter the path of root: ')
root = '/usr/local/lib'

HBADD = os.path.join(root, 'LigPlus', 'lib', 'exe_linux', 'hbadd')
assert os.path.isfile(HBADD), 'File not exists. ' + str(HBADD)

HBPLUS = os.path.join(root, 'LigPlus', 'lib', 'exe_linux', 'hbplus')
assert os.path.isfile(HBPLUS), 'File not exists. ' + str(HBPLUS)

LIGPLOT = os.path.join(root, 'LigPlus', 'lib', 'exe_linux', 'ligplot')
assert os.path.isfile(LIGPLOT), 'File not exists. ' + str(LIGPLOT)

PRM = os.path.join(root, 'LigPlus', 'lib', 'params', 'ligplot.prm')
assert os.path.isfile(PRM), 'File not exists. ' + str(PRM)

# call(['ls', HBADD])

