import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog

target_file_name = '[JoJo no Kimyou na Bouken Ougon no Kaze][01][BDRIP][1080P][H264_FLAC_DTS-HDMA].ass'
raw_formats = ['.ASS', '.SRT']  # Include raw formats to scan

def main():
    root = tk.Tk()
    root.withdraw()
    path_base = filedialog.askdirectory()  # Ask user for folder
    if path_base == '':
        print('It looks like you did not select a folder. The program will end in 5 seconds.')
        time.sleep(5)
        quit()


if '__name__' == '__main__':
    main()
    