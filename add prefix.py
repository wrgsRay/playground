import os, shutil

workFolder = 'C:\\Python\\New_backup\\'
addPrefix = 'PREFIX_'

for object in os.listdir(workFolder):
    if os.path.isfile(os.path.join(workFolder, object)):
        print('Renaming "%s" to "%s"...' % (object, os.path.join(addPrefix + object)))
        shutil.move(os.path.join(workFolder, object), os.path.join(workFolder, addPrefix + object))
    
