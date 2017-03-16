#!/usr/bin/python
import ftplib, sys

print "Please enter your credentials:"
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

	else:
		print "Command not found"
