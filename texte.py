# texte
# coding=UTF-8
import PyPDF2 as pdf


# fonction d'extraction des métadonnées issues d'un fichier texte
def extractmetadata(metadata, filepath):
    
    nbr_lignes = 0
    alltext = ''
    for ligne in open(filepath, "r"):
        nbr_lignes +=1
        alltext += ligne
    alltext = alltext.lower()
    metadata['texte_nbr_lignes'] = nbr_lignes
    
    try:
        for letter in 'abcdefghijklnopqrstuvwxyz':
            metadata['texte_occurence_de_' + letter] = alltext.count(letter)
    except:
        pass

    return metadata

# fonction d'extraction des métadonnées issues d'un fichier PDF
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
        author = 'Unknown'
    metadata['texte_auteur'] = author
    
    nbr_lignes = 0


    for letter in 'abcdefghijklnopqrstuvwxyz':
        metadata['texte_occurence_de_' + letter] = 0

    try:
        for i in range(pdfReader.numPages):
            page = pdfReader.getPage(i) 
            for ligne in page.extractText():
                nbr_lignes +=1
                ligne = ligne.lower()
                try:
                    for letter in 'abcdefghijklnopqrstuvwxyz':
                        metadata['texte_occurence_de_' + letter] = metadata['texte_occurence_de_' + letter] + ligne.count(letter)
                except:
                    pass
    except:
        pass

    metadata['texte_nbr_lignes'] = nbr_lignes
   
    return metadata
