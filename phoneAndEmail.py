# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:58:00 2017

@author: raymond
"""

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.

emailRegex = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+) # username
        @                  # @ symbol
        [a-zA-Z0-9.-]+     # domain name
        (\.[a-zA-Z]{2,7})  # dot something
        )''', re.VERBOSE)



# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# TODO: Copy results to the clipboard.
