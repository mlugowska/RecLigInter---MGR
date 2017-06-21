# -*- coding: utf-8 -*-
from reli.externals import HBADD, HBPLUS, LIGPLOT, PRM
from reli.get_ligand_from_pdb import get_ligand_number
from reli.add_chain_name import add_chain
from reli.renaming_pdbs import rename_pdb_file
from reli.make_hhb import hhb_list
from reli.make_nnb import nnb_list
from reli.call import call
import tempfile
import shutil


def make_interactions(PDB, LIG): # należy podać ścieżkę do .pdb i nazwę liganda

    # -------------------- katalog tymczasowy --------------------------------------------------------------------------

    tmp = tempfile.mkdtemp() # zwraca '/tmp/nazwa_katalogu np. '/tmp/tmpeBGxfs'
    shutil.copy2(PDB, tmp) # kopiowanie pliku pdb do katalogu tmp

    # -------------------- polecenia hbadd, hbplus, hbplus -------------------------------------------------------------

    runHBADD = [HBADD, PDB, '/usr/local/lib/pdbsum/components.cif', '-wkdir', tmp]
    call(runHBADD, cwd=tmp)

    runHBPLUS = [HBPLUS, '-L', '-f', 'hbplus.rc', '-h', '2.90', '-d', '3.90', '-N', PDB, '-wkdir', tmp]
    call(runHBPLUS, cwd=tmp)

    runHBPLUS_again = [HBPLUS, '-L', '-f', 'hbplus.rc', '-h', '2.70', '-d', '3.35', PDB, '-wkdir', tmp]
    call(runHBPLUS_again, cwd=tmp)

    # -------------------- numer liganda (min i max) -------------------------------------------------------------------

    add_chain(PDB)
    LIG_MIN, LIG_MAX, CHAIN_NAME = get_ligand_number(PDB, LIG)

    # -------------------- polecenie ligplot ---------------------------------------------------------------------------

    runLIGPLOT = [LIGPLOT, '-prm', PRM, PDB, LIG_MIN, LIG_MAX, CHAIN_NAME, '-wkdir', tmp, '-ctype', '1']
    call(runLIGPLOT, cwd=tmp)

    # -------------------- lista oddziaływań ---------------------------------------------------------------------------

    interactions_HH = list(hhb_list('ligplot.hhb'))
    interactions_NN = list(nnb_list('ligplot.nnb', LIG))

    interactions = interactions_HH + interactions_NN

    # --------------------- usunięcie tmp ------------------------------------------------------------------------------
    shutil.rmtree(tmp)

    return interactions




