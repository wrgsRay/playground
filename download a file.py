import os, requests

targetURL = 'https://centurytimer.com/product_resources/BNQ-T7BC/Instruction-Manuals-for-Web-BNQ-T7BC.pdf'
downloadURL = 'C:\\Python'
filename = targetURL[targetURL.rfind('/') + 1:]
os.chdir(downloadURL)

res = requests.get(targetURL)
try:
    res.raise_for_status()
    print('Downloading ' + filename)
    playFile = open(filename, 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
    print('Done!')
except Exception as exc:
    print('There was a problem: %s' % (exc))

