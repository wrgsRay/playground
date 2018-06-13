import os

root = 'C:\\Users\\Century Products #4\\Documents\\FBA Shipment'
for item in os.listdir(root):
    if os.path.isfile(os.path.join(root, item)):
        print(item)
