'''
List all folders and files in a folder
'''

import os
targetPath = 'D:\\Python' #Set path here

for folderName, subfolders, filenames in os.walk(targetPath):
   # print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
