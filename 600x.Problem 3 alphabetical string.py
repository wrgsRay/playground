#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:35:02 2017

@author: raymond
"""
# s = ''


s = 'teavdbdsudczhdak'

# initialise tracker variables
maxLen = 0
current = s[0]
longest = s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        # if current length is bigger update
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current = s[i + 1]


print('Longest substring in alphabetical order is: ' + longest)
# tmp_ss = '' #temporary substring while checking for the substring
# ss_can = '' #substring candidate for final output
# p_letter = ' ' #previous letter(currently a space) for start of the loop
#
# for letter in s:
# #used during debug
# #    print("checking " + letter)
#     if p_letter <= letter: #if last letter is less than or equal to the current letter
#         p_letter = letter #set current letter as previous letter for next loop
#         tmp_ss += letter #set tmp_ss to include one more letter
#         ss_len =+ len(tmp_ss) #check length of tmp_ss
#     elif p_letter > letter: #if last letter is greater than current letter(start next substring)
#         if len(tmp_ss) > len(ss_can): #if length of the current tmp_ss is longer than the candidate
#             ss_can = tmp_ss #set ss_can as tmp_ss #if yes, refresh the new candidate as the current tmp_ss
#             tmp_ss = '' #clear tmp_ss
#             #tmp_ss += letter #start a new sub string for tmp_ss
#             p_letter = " " #set previous letter as empty for next loop
#         else: #if the current tmp_ss is shorter than the current candidate, start over
#             tmp_ss = '' #clear tmp_ss
#            # tmp_ss += letter #start a new sub string for tmp_ss
#             p_letter = " " #set previous letter as empty for next loop
# #used during debug
# #    print("current p_letter " + p_letter + " current tmp_ss " + tmp_ss + " and current ss_can " + ss_can)