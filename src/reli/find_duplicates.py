# -*- coding: utf-8 -*-
from reli.run_multi_pdbs import multi_pdbs
import os


# iterate over dictionary to check if interactions duplicate
def check_duplicates(PDB_source, LIG):

    interactions_in_time = multi_pdbs(PDB_source, LIG) # zwraca słownik oddziaływań
    inter_set = set()

    out = open('interactions_table.csv', "w")

    for key, values in interactions_in_time.iteritems():
        inter_set = inter_set.union(set(values)) # nagłówki do tabeli

    inter_set = list(inter_set) # żeby kolejność się nie zmieniała
    out.write('frame,' + ','.join(inter_set) + os.linesep)
    schema = '%s,' + ','.join(['%d']*len(inter_set))

    for key, values in interactions_in_time.iteritems():
        count_values = [values.count(x) for x in inter_set]
        print >> out, schema % tuple([key]+count_values)

    out.close()

f = '/home/magdalena/Desktop/MGR_substrate_only/RecLigInter/pdb'
ligand = 'LIG'
check_duplicates(f, ligand)

