# tables
# coding=UTF-8
import pandas as pd
import csv


# fonction d'extraction des métadonnées issues d'un csv
def extractmetadata(metadata, filepath):
    
    with open(filepath, "r") as csv_file:
        dReader = csv.DictReader(csv_file)
        header = dReader.fieldnames
        metadata['chiffres_nbr_colonnes'] = len(list(dReader))
        metadata['chiffres_entete'] = header

    nbr_lignes = 0
    for chiffre in '0123456789':
        metadata['chiffres_occurence_de_' + chiffre] = 0
    for ligne in open(filepath, "r"):
        nbr_lignes +=1
        try:
            for chiffre in '0123456789':
                metadata['chiffres_occurence_de_' + chiffre] = metadata['chiffres_occurence_de_' + chiffre] + ligne.count(chiffre)
        except:
            pass

    metadata['chiffres_nbr_lignes'] = nbr_lignes



    return metadata