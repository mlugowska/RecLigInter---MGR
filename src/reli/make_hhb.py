# -*- coding: utf-8 -*-
def hhb_list(filename):

    with open(filename, 'r') as fileHHB:

        for line in fileHHB.readlines()[3:]:

            donor = line[0:10].split()
            donor = '_'.join(donor)
            acceptor = line[21:31].split()
            acceptor = '_'.join(acceptor)

            yield '_'.join([donor, acceptor, 'HH'])



# file = 'ligplot.hhb'
# print list(hhb_list(file))



