from shutil import move
import os


def add_chain(PDB_source):
    for root, dirs, filenames in os.walk(PDB_source):

        for name in filenames:

            PDB = os.path.join(PDB_source, name)

            with open(PDB, 'r+') as filePDB, open('temp.pdb', 'w') as temp:

                lines = filePDB.readlines()

                for line in lines[1:]:
                    # if 'TER' not in line:

                        temp.writelines(
                            [line[0:4], line[4:6], line[6:11], line[11:12], line[12:16], line[16:17], line[17:21], 'A',
                             line[22:26], line[26:30], line[30:38], line[38:46], line[46:54], line[54:60], line[60:66], '\n'])

            move(temp.name, PDB)

# add_chain('/home/magdalena/Desktop/MGR_substrate_only/1nww/model-5/cMD/38470.Panda_1nww+model-5/pdb_test')


