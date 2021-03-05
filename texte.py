# texte
# coding=UTF-8

def extractmetadata(metadata, filepath):
    
    nbr_lignes = 0
    for ligne in open(filepath, "r"):
        nbr_lignes +=1

    metadata['texte_nbr_lignes'] = nbr_lignes

    return metadata