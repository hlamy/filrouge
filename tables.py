# tables
# coding=UTF-8
import pandas as pd
import csv


# fonction d'extraction des métadonnées issues d'un csv
def extractmetadata(metadata, filepath):
    
    with open(filepath, "r") as csv_file:
        dReader = csv.DictReader(csv_file)
        header = dReader.fieldnames
        metadata['csv_nbr_colonnes'] = len(list(dReader))
        metadata['csv_header'] = header

    nbr_lignes = 0

    for ligne in open(filepath, "r"):
        nbr_lignes +=1

    metadata['csv_nbr_lignes'] = nbr_lignes

    return metadata