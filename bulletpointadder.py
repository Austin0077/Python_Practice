#! /usr/bin/python3.5

# this program will get text from clipboard , then add bullets or stars infront
# then return the text back to the clipboard for pasting.
''' bulletpointadder.py --Adds Wikipedia bullet points to the start 
of each line of text on the clip board.'''

import pyperclip
text = pyperclip.paste()

#separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):#loop through all indexes in the "lines" list
	lines[i] = '*' + lines[i]  #add star to each string in 'lines' list.
#TODO: Separate lines and add stars

pyperclip.copy(text)