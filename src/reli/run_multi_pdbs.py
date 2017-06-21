# -*- coding: utf-8 -*-
from reli.make_interactions import make_interactions
from reli.renaming_pdbs import rename_pdb_file
import os

def multi_pdbs(PDB_source, LIG): # ścieżka do plików pdb i nazwa liganda

    interactions_in_time = {}

    # rename_pdb_file(PDB_source)

    for root, dirs, filenames in os.walk(PDB_source):

        for name in filenames:

            PDB = os.path.join(PDB_source, name)

            single_pdb_interactions = make_interactions(PDB, LIG)
            interactions_in_time.update({name:single_pdb_interactions})

    return interactions_in_time

                # zwraca listę oddziaływań dla każdego pliku


# iterować po słowniku: klucze i wartości
# sprawdzić czy oddziaływania się powtarzają
# ułożyć tabelkę
#
# f = '/home/magdalena/Desktop/MGR_substrate_only/RecLigInter/pdb'
# ligand = 'LIG'
# print multi_pdbs(f, ligand)