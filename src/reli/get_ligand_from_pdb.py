# -*- coding: utf-8 -*-
def get_ligand_number(PDB, LIG):

    with open(PDB, 'r') as filePDB:

        LIG_NR = []

        for line in filePDB:
            if LIG in line:
                ATOM_ID = line[6:11].strip()
                ATOM_NAME = line[12:16].strip()
                CHAIN_NAME = line[21:22].strip()
                LIG_ID = line[23:26].strip()
                x = line[30:38].strip()
                y = line[38:46].strip()
                z = line[46:54].strip()

                LIG_NR.append(LIG_ID)
                LIG_NR.sort()
                LIG_MIN = min(LIG_NR)
                LIG_MAX = max(LIG_NR)

                # LIG_NR.extend([LIG_MIN, LIG_MAX, CHAIN_NAME])

        return LIG_MIN, LIG_MAX, CHAIN_NAME

LIG = 'LIG'
PDB = '/home/magdalena/Desktop/MGR_substrate_only/RecLigInter/pdb/SS_40560.pdb'
lst = get_ligand_number(PDB, LIG)
print lst