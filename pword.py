#! /usr/bin/python3.5
'''the program will run in cmd, being able to save unknown passwords for the user.
account passwords will be saved in clipboard for user to paste in password field in the browser.
#pword,py- An insecure password locker program.'''

PASSWORDS = {'email' :'F7min1fjhjgflgfgjlsf',
			 'blog' : 'Thbdhetu455uuhhrr774',
			 'facebook' :'76895itjhdghghhhh',
			 'twitter' : 'ytt75ejdhty5uu765',
			 'luggage' : '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
	print('Usage: python pword.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]  #first command line arg is the account name.

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account +'copied to clipboard.')
else:
	print('There is no account named' + account)