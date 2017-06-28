# -*- coding: utf-8 -*-
from shutil import move
import os


def renumber_pdb(PDB):

    # for root, dirs, filenames in os.walk(PDB_source):
    #
    #     for name in filenames:
    #
    #         PDB = os.path.join(PDB_source, name)

            with open(PDB, 'r') as filePDB, open('temp.pdb', 'w') as temp:
                lines = filePDB.readlines()

                for line in lines[1:]:

                        if 'ATOM' in line:
                            RES_ID = line[22:26].rstrip()

                            if 'LIG' in line:
                                RES_ID = 9999 - 3

                            new_RES_ID = '    ' + str(int(RES_ID) + 3)
                            new_RES_ID = new_RES_ID[-4:]

                            print line

                            new_line = line[:22] + new_RES_ID + line[26:]

                            temp.write(new_line)
                        else:
                            temp.write(line)


                        # if 'LIG' in line:
                        #
                        #     new_lig = line.replace(RES_ID, str(0))
                        #     temp.writelines(
                        #         [new_lig])
                        # else:
                        #     temp.writelines(
                        #         [line])

                # move(temp.name, PDB)

renumber_pdb('/home/magdalena/Desktop/MGR_substrate_only/RecLigInter/pdb/WT846.pdb')
