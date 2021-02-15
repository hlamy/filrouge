# coding=UTF-8
from pathlib import Path
import json
import os

# dossiers nécessaires au bon fonctionnement
temporary_files_folder = './temp'

# pictures_folder = Path('./pictures')
# alerts_folder = Path('./alerts')
# passwordfolder = Path('./pswd')
# statusfolder = Path('./status')
# failurefolder = Path('./failures')
# passwordfile = Path("mailpassword")
# passwordpath = passwordfolder / passwordfile

# port d'accès à l'application
applicationportnumber = '5555'







def readsettings():
    with open("/data/settings.json", 'r') as jsonsettings:
        allsettings = json.load(jsonsettings)
    
    temporary_files_folder = allsettings['temporary_files_folder']
    applicationportnumber = allsettings['applicationportnumber']

    return temporary_files_folder, applicationportnumber

def writesettings():
    
    with open("/data/settings.json", 'r') as jsonsettings:
        allsettings = json.load(jsonsettings)

    allsettings['temporary_files_folder'] = temporary_files_folder
    allsettings['applicationportnumber'] = applicationportnumber

    with open("./settings.json", 'w') as jsonsettings:
        json.dump(allsettings,jsonsettings,  indent=4)

    return True


temporary_files_folder, applicationportnumber = readsettings()



try:
    os.mkdir(temporary_files_folder)
except:
    pass

