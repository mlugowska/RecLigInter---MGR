import os


def rename_pdb_file(path):

    files = os.listdir(path)
    # i = 1

    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, str(i+1)+'.pdb'))
        # i = i+1



# path = '/home/magdalena/Desktop/MGR_substrate_only/RecLigInter/pdb'
# rename_pdb_file(path)