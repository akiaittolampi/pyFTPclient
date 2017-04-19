#!/usr/bin/python

import pexpect

child = pexpect.spawn("python scripts/ftp_client.py")

child.expect("Server: ")
child.sendline("localhost")

child.expect("Username: ")
child.sendline("testikeke")

child.expect("Password: ")
child.sendline("foobar")

child.expect("$")
child.sendline("get test.txt")

child.expect("OK")
child.sendline("quit")



