#!/usr/bin/python3

#now importing time library
import time
import subprocess
import webbrowser
import os



option='''
PRESS 1 to play your seacrh in youtube:
Press 2 to search something on google:
Press 3 to send whatsapp message:
Press 4 to check current date and time:
Press 5 to reboot your machine:
'''

print(option)

#taking input from user

choice=input()
#input function will take he input in str format
#condtional Statement
if choice == '4':
	#to connect with bios to get date and time
	current_time=time.ctime()
	print(current_time)
elif choice =='2':
	#to search on google
	data=input("type your search---->>>")
	webbrowser.open_new_tab('https://www.google.com/search?q='+ data)
elif choice =='1':
	#to open youtube with your search
	data=input("type your search---->>>")
	webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+ data)
elif choice=='5':
	#to reboot the system
	os.system('reboot')	
elif choice=='3':
	#to send message through whatsapp
	webbrowser.open_new_tab('https://web.whatsapp.com/')	
else:
	print("wrong choice") 
