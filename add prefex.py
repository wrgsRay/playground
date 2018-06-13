import os, shutil

workFolder = 'C:\\Python\\New_backup\\'

for object in os.listdir(workFolder):
    if os.path.isfile(os.path.join(workFolder, object)):
        print('Renaming "%s" to "%s"...' % (object, os.path.join('PREFIX_' + object)))
        shutil.move(os.path.join(workFolder, object), os.path.join(workFolder, 'PREFIX_' + object))
    
