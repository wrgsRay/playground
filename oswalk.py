import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\Century Products #4\\Documents\\FBA Shipment'):
   # print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
