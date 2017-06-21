from shutil import move


def add_chain(PDB):
    with open(PDB, 'r+') as filePDB, open('temp.pdb', 'w') as temp:

        lines = filePDB.readlines()
        # lines = (row.rstrip() for row in filePDB)
        # lines.remove('TER')

        for line in lines:
            if 'TER' not in line:

                temp.writelines(
                    [line[0:4], line[4:6], line[6:11], line[11:12], line[12:16], line[16:17], line[17:21], 'A',
                     line[22:26], line[26:30], line[30:38], line[38:46], line[46:54], line[54:60], line[60:66], '\n'])

    move(temp.name, PDB)

