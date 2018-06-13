import os, shutil

workFolder = 'C:\\Users\\Century Products #4\\Documents\\FBA Shipment'
os.chdir(workFolder)
"""
for folderName, subfolders, filenames in os.walk(workFolder):
    print('The current folder is ' + folderName)

##    for subfolder in subfolders:
##        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        #print('FILE INSIDE ' + folderName + ': '+ filename)
        if(filename.endswith('.txt') == True):
            #shutil.move(filename, workFolder + '\\Submitted\\' + filename)
            #os.chdir(folderName)
            #print(filename + ' in ' + folderName + ' starts with FBA')
            print(filename + ' is moved')
"""
for things in os.listdir(workFolder):
    if os.path.isfile(os.path.join(workFolder, things)):
        if things.endswith('.txt') == True:
            shutil.move(things, workFolder + '\\Submitted\\' + things)
            print(things + ' is moved to ' + os.path.join(workFolder, '\\Submitted\\'))


