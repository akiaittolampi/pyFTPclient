#!/usr/bin/python
import ftplib, sys

#print "Please enter your credentials:"
srv = raw_input("Server: ")
user = raw_input("Username: ")
passwd = raw_input("Password: ")

ftp = ftplib.FTP(srv, user, passwd)

print ftp.getwelcome()
session = 1

while session:
	command = raw_input("$")

	if command == "dir": 
		print ftp.dir()

	elif command == "quit":
		sys.exit(0)

	elif "get" in command:
		filepath = command
		first, _, rest = filepath.partition(" ")
		last = rest
	        ftp.retrbinary("RETR " +  last, open(last, 'wb').write)
		print "OK"

	elif "put" in command:
		filepath = command
		first, _, rest = filepath.partition(" ")
		last = rest
		openfile = open(last)
		
		ftp.storbinary("STOR " + last, openfile)
		openfile.close()
		print "OK"

	elif command=="help":
		print " dir = list files \n put = copy files to ftp \n get = copy files to localdir \n quit = leave program \n help = list commands \n cd = change dir \n pwd = print workdir "
 
	elif "cd" in command:
		filepath = command
		first, _,rest = filepath.partition(" ")
		last = rest
		ftp.cwd(last)

	elif command == "pwd":
		print ftp.pwd()
		
	else:
		print "Command not found"
