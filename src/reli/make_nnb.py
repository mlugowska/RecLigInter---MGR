# -*- coding: utf-8 -*-
def nnb_list(filename, LIG):
    listoflists = []
    with open(filename, 'r') as fileNNB:

        for line in fileNNB.readlines()[3:]:

            atom1 = line[0:10].split()
            atom2 = line[21:31].split()

            if LIG in line[21:26]:
                atom1, atom2 = atom2, atom1
            else:
                atom1, atom2 = atom1, atom2

            atom1 = '_'.join(atom1)
            atom2 = '_'.join(atom2)

            yield '_'.join([atom1, atom2, 'NN'])


#
# file = 'ligplot.nnb'
# print list(nnb_list(file, 'LIG'))



