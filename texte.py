# texte
# coding=UTF-8
import PyPDF2 as pdf



def extractmetadata(metadata, filepath):
    
    nbr_lignes = 0
    for ligne in open(filepath, "r"):
        nbr_lignes +=1

    metadata['texte_nbr_lignes'] = nbr_lignes



    return metadata


def extractmetadata_pdf(metadata, filepath):
    document = open(filepath, "rb")

    pdfReader = pdf.PdfFileReader(document)

    try:
        nbr_pages = pdfReader.numPages
    except:
        nbr_pages = 1
    metadata['texte_nbr_pages'] = nbr_pages
    
    try:
        author = pdfReader.author
    except:
        author = None
    
    nbr_lignes = 0
    try:
        for i in range(pdfReader.numPages):
            page = pdfReader.getPage(i) 
            for ligne in page.extractText():
                nbr_lignes +=1
    except:
        pass

    metadata['texte_nbr_lignes'] = nbr_lignes
   

    return metadata
