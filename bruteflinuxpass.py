#!/usr/bin/python
import socket
import sys
import crypt

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "-------------PYNET-TOOLS - bruteflinuxpass.py-----------"
    print "--------------------------------------------------------"
    print "-----------usage: ./bruteflinuxpass.py wordlist---------"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)

def bruteflinuxpass():
    
    file = open(sys.argv[1])
    salt = raw_input("type the salt: ")
    chash = raw_input("type the hash: ")

    for i in file:
        i = i.replace("\n","")
        ci = crypt.crypt(i,salt)
        if ci==chash:
            print "the password is: " + i
        else:
            pass

def main():

    if not len(sys.argv[1:]):
        help()
    else:
        arg1 = sys.argv[1]

    if (arg1 == "-h" or arg1 == "--help"):
        help()
    else:
        bruteflinuxpass()

main()


